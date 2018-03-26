python early:
    def parse_showd_screen(l):

        # Parse a name.
        name = l.require(l.name)

        # Parse the list of arguments.
        arguments = renpy.parser.parse_arguments(l)

        predict = True
        transition_expr = None

        while True:

            if l.keyword('nopredict'):
                predict = False

            elif l.keyword('with'):
                transition_expr = l.require(l.simple_expression)

            else:
                break

        l.expect_eol()

        return dict(name=name, arguments=arguments, predict=predict, transition_expr=transition_expr)

    def parse_hided_screen(l):
        name = l.require(l.name)

        l.expect_eol()

        return dict(name=name)

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

        if a is not None:
            args, kwargs = a.evaluate()
        else:
            args = [ ]
            kwargs = { }

        renpy.transition(dissolve)
        renpy.show_screen(name, *args, **kwargs)

    def execute_hided_screen(p):
        name = p["name"]

        renpy.transition(dissolve)
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
        # Parse a name.
        name = l.require(l.name)

        while True:
            if l.keyword('at'):
                # Parse the relative coordinates.
                x = l.require(l.simple_expression)
                y = l.require(l.simple_expression)
                l.expect_eol()
                break
            else:
                # Name has more words, get them all
                name += ' ' + l.require(l.name)


        return dict(name=name, x=x, y=y, predict=True)

    def parse_hide_sprite(l):
        # Parse a name.
        name = l.require(l.name)

        l.expect_eol()

        return dict(name=name)

    def predict_sprite(p):
        if not config.predict_screen_statements:
            return

        predict = p.get("predict", False)

        if not predict:
            return

        name = p["name"]
        x = int(p["x"])
        y = int(p["y"])
        at_list = [inside_letterbox(x,y)]

        return [name]

    def execute_show_sprite(p):
        name = p["name"]
        x = int(p["x"])
        y = int(p["y"])
        at_list = [inside_letterbox(x, y)]

        renpy.show(name, at_list=at_list, layer="screens")

    def execute_hide_sprite(p):
        name = p["name"]
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
