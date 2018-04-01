label s03:
    jump .intro

    # debug
    scene fbg travel
    jump .focus

label .intro:
    scene fbg day

    $ renpy.pause(0.5)
    showd screen illustframe("booth_cover") during 2.0
    $ renpy.pause(2.0)
    "Inside the city, Josef looked for the Toy Fair.
    Arrived in the Square, all he could find was a
    range of curtains."
    showd screen illustframe("booth") during 2.0
    "Suddenly, the covers were pulled off and
    Josef was surrounded by stalls presenting
    new toy concepts: bubble games, wooden
    puzzles, dexterity games, mechanical
    devices, even a puppet show."
    "The boy spent some time investigating
    which products would improve his store's
    business."
    "But his mind was quickly saturated with
    the overload of information.
    {w=0.5}Many brands were still unknown to him,
    and he wasn't sure which of them he could trust."
    "His natural reaction was to seek what he was
    the most familiar with: the Cursed Knight.
    {p=0.5}After a dozen minutes, he found the booth
    of his favorite figure brand."
    hided screen illustframe
    $ renpy.pause(1.0)

label .end:
    "To be continued..."
