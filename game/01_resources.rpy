# Images

# GUI
# It would be nice to have a CTC (click-to-continue) icon for all text,
# but I'd need to override the default adv character or to create
# a fictive character with ctc and put its name in front of each and every text.

# Full background
image fbg day = Solid("#fefef8")  # paper white
image fbg sunset = Solid("#fad6a5")  # sunset

# Background frame
image frame = Frame("images/frame-pixabay.png", 20, 20)

# Backgrounds (790x474)
image bg toyshop day = "images/bg/toyshop_day.png"
image bg toyshop evening = "images/bg/toyshop_evening.png"
image bg travel = "images/bg/travel.png"
image bg booth = "images/bg/booth.png"
image bg booth_cover = "images/bg/booth_cover.png"

# CG (790x474)
image cg top = "images/cg/top.png"

# Characters
image mc = "char/mc_stand.png"
image mc bust = "images/char/mc_bust.png"
image mc bust smile= "images/char/mc_bust_smile.png"
image mc bust big = "images/char/mc_bust_big.png"
image mc_hand_right = "images/char/mc_hand_right.png"
image mc_hand_left = "images/char/mc_hand_right.png"  # cheat
image lady = "images/char/lady_stand.png"
image lady look = "images/char/lady_stand_look_around.png"
image uncle bust = "images/char/uncle_bust.png"
image nadia bust big = "images/char/nadia_bust_big.png"

# Item
image top spinning = "item/top_spinning.png"
image top stopped = "item/top_stopped.png"
image ledger = "item/ledger.png"  # unused
image cursed_knight_original = "item/cursed_knight_ori.png"
image glass_plate1_drawn = "item/glass_plate1_drawn.png"
image glass_plate2_drawn = "item/glass_plate2_drawn.png"
image glass_plate3_drawn = "item/glass_plate3_drawn.png"

# FX
image focus ellipse = "images/fx/focus_ellipse.png"
image focus smog = "images/fx/focus_smog.png"
image fx_shout = "images/fx/shout.png"

# Debug
image blackpx = im.Scale("black_background.png", 10, 10)
image red = Solid("#ff0000")
image stage sky = im.Scale("bg/sky_dousetsu.jpg", 790, 474)

# Audio

# BGM
define audio.toyshop = "music/Carpe Diem.mp3"
define audio.conflict = "music/Thinking Music.mp3"

# SFX
define audio.spinning_top = "sfx/spinning_top_raw.mp3"
define audio.chime = "sfx/chime_trimmed.wav"
define audio.hit_table = "sfx/bottle-hitting-a-table.wav"
