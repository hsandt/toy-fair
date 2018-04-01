label s02:
    jump .intro

    # debug
    scene fbg travel
    jump .end

label .intro:
    scene fbg day

    $ renpy.pause(0.5)
    showd screen illustframe("travel") during 2.0
    shows mc bust big at (-160, 47)
    shows nadia bust big at (120, 7)
    shows glass_plate1_drawn at (160, 135)
    shows glass_plate2_drawn at (160, 135)
    shows glass_plate3_drawn at (160, 135)
    $ renpy.pause(2.0)
    "The next day, Josef was on a trip aboard a
    stage coach for the Eastern city. He left
    without telling his uncle, determined to
    prove there was something worth to see at
    the Toy Fair."
    "Besides him, a young woman was painting
    on a strange combination of glass plates.
    The thing was clearly not a toy, though, so
    Josef looked away."
    "After half an hour, Josef really starting
    getting bored. There was still an hour of
    travel left and he had nothing else to do, so
    he glanced at what the woman was doing."
    "Obviously, she was painting the sunrise they
    were facing, but was doing so layer by layer on
    different glass plates, giving a sense of
    depth to the picture."
    "‘Interested?’ she asked. I call it volumetric
    painting.
    {p}‘It's the first time I see something like this.
    Is that a new trend?’
    {w=0.5}The woman laughed."
    "‘Not really, I invented it last week. I quickly get
    fed up with standard techniques so I try new
    ones quite often.’"
    "Josef looked at the picture again. He liked the
    concept, but found the execution clumsy. In its current
    state, the painting would probably never sell."
    "‘I guess it's a bit early to make it a business.’
    {p=0.5}The woman nodded."
    "‘I could reinforce a specific
    technique if I sticked to it for several months.
    {w=0.5}But for now, I find the biggest thrill in opening new doors for other
    artists.’"
    "Josef kept watching the painter's work until
    they arrived."
    hides mc
    hides nadia
    hided screen illustframe
    $ renpy.pause(2.0)

label .end:
    jump s03
