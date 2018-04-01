python early:
    def parse_showd_screen(l):

        # Parse a name.
        name = l.require(l.name)

        # Parse the list of arguments.
        arguments = renpy.parser.parse_arguments(l)

        duration = 1.0
        predict = True
        transition_expr = None

        while True:

            if l.keyword('during'):
                duration = l.require(l.simple_expression)

            elif l.keyword('nopredict'):
                predict = False

            elif l.keyword('with'):
                transition_expr = l.require(l.simple_expression)

            else:
                break

        l.expect_eol()

        return dict(name=name, arguments=arguments, duration=duration, predict=predict, transition_expr=transition_expr)

    def parse_hided_screen(l):
        name = l.require(l.name)

        duration = 0.5

        if l.keyword('during'):
            duration = l.require(l.simple_expression)

        l.expect_eol()

        return dict(name=name, duration=duration)

    def predict_screen(p):

        if not config.predict_screen_statements:
            return

        predict = p.get("predict", False)

        if not predict:
            return

        name = p["name"]
        a = p["arguments"]

        if a is not None:
            args, kwargs = a.evaluate()
        else:
            args = [ ]
            kwargs = { }

        renpy.predict_screen(name, *args, **kwargs)

    def execute_showd_screen(p):

        name = p["name"]
        a = p["arguments"]
        duration = float(p["duration"])

        if a is not None:
            args, kwargs = a.evaluate()
        else:
            args = [ ]
            kwargs = { }

        renpy.transition(Dissolve(duration))
        renpy.show_screen(name, *args, **kwargs)

    def execute_hided_screen(p):
        name = p["name"]
        duration = float(p["duration"])

        renpy.transition(Dissolve(duration))
        renpy.hide_screen(name)

    def lint_screen(p):
        name = p["name"]
        if not renpy.has_screen(name):
            renpy.error("Screen %s does not exist." % name)

    # Show a screen with dissolve transition
    # Ex: showd screen illustframe("stage toyshop")
    renpy.register_statement("showd screen",
                              parse=parse_showd_screen,
                              execute=execute_showd_screen,
                              predict=predict_screen,
                              lint=lint_screen)

    # Hides a screen with dissolve transition
    # Ex: hided screen illustframe
    renpy.register_statement("hided screen",
                              parse=parse_hided_screen,
                              execute=execute_hided_screen)


    def parse_show_sprite(l):
        # Parse a name using the advanced methods used in show_statement
        # We must adapt the code as show_statement really executes, and we only want to parse
        # It's not possible to catch the ATL block like show_statement because ':' is ignored by this lexer
        # parse_image_specifier returns a tuple for the name components, but seems to work
        # In addition, everything before keywords is included in the image name so you cannot
        # use a custom keyword if you use this. That's why we hack around at to specify a relative position
        # And for "during", you need to add at least one keyword before. We recommend "at ()" to distinguish from "at (0, 0)"
        imspec = renpy.parser.parse_image_specifier(l)

        # We exploit at, always considering the 1st argument as relative coordinates, if any
        image_name, expression, tag, at_list, layer, zorder, behind = imspec
        if at_list:
            # Convert to screen coordinates (caution: we manipulate strings)
            xy = eval(at_list[0])
            if type(xy) is tuple:
                if len(xy) == 2:
                    x, y = xy
                    at_list[0] = "inside_letterbox({}, {})".format(x, y)  # will be evaluated
                elif len(xy) == 0:
                    # "at ()" is just a separator to use "during", do nothing to preserve previous position
                    # so len 0 is OK, but we need to remove it because it's not a transform
                    at_list.pop(0)
                else:
                    l.error("expected tuple of length 2 or 0.")
            else:
                l.error("expected tuple.")
        # we don't default to (0, 0) so we can keep the position of the previous sprite
        # with the same tag, so don't forget to initialize centered sprites at (0, 0)
        imspec = image_name, expression, tag, at_list, layer, zorder, behind

        duration = 0.5
        x, y = 0, 0

        # during must be placed after standard specifiers
        if l.keyword('during'):
            duration = l.require(l.simple_expression)

        l.expect_eol()

        return dict(imspec=imspec, duration=duration, predict=True)

    def parse_hide_sprite(l):
        # Parse full image name for compatibility with hide (but only the tag, the 1st component, matters)
        image_name = l.require(l.name)

        duration = 0.5

        if l.keyword('during'):
            duration = l.require(l.simple_expression)

        l.expect_eol()

        return dict(name=image_name, duration=duration)

    def predict_sprite(p):
        if not config.predict_screen_statements:
            return

        # we could use predict_imspec(p["imspec"]) which does the prediction job
        # and return None, but returning just the name also works

        predict = p.get("predict", False)

        if not predict:
            return

        imspec = p["imspec"]
        name = imspec[0]

        return [name]

    def execute_show_sprite(p):
        imspec = p["imspec"]
        duration = float(p["duration"])

        name, expression, tag, at_list, _, zorder, behind = imspec

        # override layer to "screens" (don't provide a layer when using "shows")
        imspec = name, expression, tag, at_list, "screens", zorder, behind

        # Warning: transitions will apply to anything displayed on screen during that period
        renpy.transition(Dissolve(duration))
        renpy.ast.show_imspec(imspec)

    def execute_hide_sprite(p):
        name = p["name"]
        duration = float(p["duration"])

        renpy.transition(Dissolve(duration))
        renpy.hide(name, layer="screens")

    # Shows a sprite inside the letterbox, in relative coordinates
    # from that center, on the screens layer
    # Ex: shows mysprite 10 -20
    renpy.register_statement("shows",
                              parse=parse_show_sprite,
                              execute=execute_show_sprite,
                              predict=predict_sprite)

    # Hides a sprite from the screens layer
    # Ex: hides mysprite
    renpy.register_statement("hides",
                              parse=parse_hide_sprite,
                              execute=execute_hide_sprite)
