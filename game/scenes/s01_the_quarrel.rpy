# Images

# Full background
image fbg day = Solid("#fefef8")  # paper white
image fbg sunset = Solid("#fad6a5")  # sunset

# Background frame
image frame = Frame("images/frame-pixabay.png", 20, 20)

# Backgrounds (790x474)
image bg toyshop day = "images/bg/toyshop_day.png"
image bg toyshop evening = "images/bg/toyshop_evening.png"

# CG (790x474)
image cg top = "images/cg/top.png"

# Characters
image mc = "char/mc_stand.png"
image mc bust = "images/char/mc_bust.png"
image mc bust smile= "images/char/mc_bust_smile.png"
image lady = "images/char/lady_stand.png"
image lady look = "images/char/lady_stand_look_around.png"
image uncle bust = "images/char/uncle_bust.png"

# Item
image top spinning = "item/top_spinning.png"
image top stopped = "item/top_stopped.png"
image ledger = "item/ledger.png"

# FX
image focus ellipse = "images/fx/focus_ellipse.png"
image fx_shout = "images/fx/shout.png"

# Debug
image blackpx = im.Scale("black_background.png", 10, 10)
image red = Solid("#ff0000")
image stage sky = im.Scale("bg/sky_dousetsu.jpg", 790, 474)

# Audio

# BGM
define audio.toyshop = "music/Carpe Diem.mp3"
define audio.conflict = "music/Thinking Music.mp3"
define audio.spinning_top = "sfx/spinning_top_raw.mp3"

label s01:
    # jump .intro

    # debug
    scene fbg day
    jump .focus

label .intro:
    scene fbg day

    $ renpy.pause(0.5)
    showd screen illustframe("cg top") during 2.0
    play sound spinning_top loop
    $ renpy.pause(2.0)
    "The top had been spinning for a good
    minute, and didn't seem ready to slow down
    any time soon."
    hided screen illustframe
    $ renpy.pause(1.0)

label .focus:
    showd screen illustframe("bg toyshop day")
    shows focus ellipse
    shows mc bust behind a at (0, 0)
    shows top spinning at (5, 45)
    $ renpy.pause(1.0)
    "Josef was staring at the toy, hypnotized. {w}He
    stopped expecting anything more from it a
    moment ago, but he couldn't look away."

label .lady:
    shows lady behind focus at (-160,90)
    $ renpy.pause(1.0)
    hides focus
    "A woman entered and stared at the shelves
    with doubtful eyes. Josef didn't care anyway."

label .end:
    play music toyshop
    "END"
