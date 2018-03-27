# Images

# Full background
image bg white = Solid("#fefef8")  # paper white

# Background frame
image frame = Frame("images/frame-pixabay.png", 20, 20)

# Backgrounds
image bg toyshop = "images/bg/toyshop.png"

# Characters
image mc = "char/mc_stand.png"
image mc bust = "images/char/mc_bust.png"
image lady = "images/char/lady_stand.png"

# Debug
image blackpx = im.Scale("black_background.png", 10, 10)
image red = Solid("#ff0000")
image stage station = im.Scale("station_a.jpg", 790, 474)
image stage sky = im.Scale("sky_dousetsu.jpg", 790, 474)

# Audio

# BGM
define audio.toyshop = "music/Carpe Diem.mp3"
define audio.conflict = "music/Thinking Music.mp3"

label s01:
    jump .intro

label .intro:
    scene bg white
    showd screen illustframe("bg toyshop")
    play music toyshop
    $ renpy.pause(0.5)
    shows mc at 0 0
    "Enter"
    shows lady at 5 40
    "Move"
    shows mc bust at -50 0
    "Exit"
    $ renpy.pause(0.5)
    hides mc
    hides lady
    $ renpy.pause(0.5)
    hided screen illustframe
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    showd screen illustframe("stage sky")
    play music conflict
    'Seppel looked at the sky, and said, "Hurray!"'
