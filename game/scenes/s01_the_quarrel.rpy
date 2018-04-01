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

# CG (790x474)
image cg top = "images/cg/top.png"

# Characters
image mc = "char/mc_stand.png"
image mc bust = "images/char/mc_bust.png"
image mc bust smile= "images/char/mc_bust_smile.png"
image mc_hand_right = "images/char/mc_hand_right.png"
image mc_hand_left = "images/char/mc_hand_right.png"  # cheat
image lady = "images/char/lady_stand.png"
image lady look = "images/char/lady_stand_look_around.png"
image uncle bust = "images/char/uncle_bust.png"

# Item
image top spinning = "item/top_spinning.png"
image top stopped = "item/top_stopped.png"
image ledger = "item/ledger.png"  # unused
image cursed_knight_original = "item/cursed_knight_ori.png"

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

label s01:
    jump .intro

    # debug
    scene fbg day
    jump .focus

label .intro:
    scene fbg day

    $ renpy.pause(0.5)
    showd screen illustframe("cg top") during 2.0
    play music spinning_top loop
    $ renpy.pause(2.0)
    "The top had been spinning for a good
    minute, and didn't seem ready to slow down
    any time soon."
    hided screen illustframe
    $ renpy.pause(1.0)

label .focus:
    showd screen illustframe("bg toyshop day")
    shows cursed_knight_original at (-345, 100)
    shows focus smog at (0, 0)
    shows mc bust behind a at (0, 5)
    shows top spinning at (45, 28)
    $ renpy.pause(1.0)
    "Josef was staring at the toy, hypnotized.
    {w}He stopped expecting anything more from it a moment ago,
    but he couldn't look away."

label .lady:
    play sound chime
    pause 1.0
    hides focus
    shows lady behind focus at (-160, 90)
    $ renpy.pause(1.0)
    "A woman entered and stared at the shelves, seemingly unsatisfied.
    {w=0.5}Josef remained focused on the spinning object."
    pause 1.0

label .shout:
    shows fx_shout at (230, -100) during 0.
    play sound hit_table
    "‘Sepp!’ shouted a voice from the back shop.
    {p}‘How many times have I told you to welcome customers?!’"
    hides fx_shout during 0.

label .welcome:
    "Sepp stopped the top with his hand.\n"
    shows mc_hand_left at (45, 25) during 0.
    shows top stopped at (45, 32) during 0.
    shows mc bust smile at () during 0.
    stop music
    play music toyshop
    extend "‘Welcome!’"
    hides mc_hand_left during 0.
    "The woman hesitated.
    {p=1.0}‘I'm looking for a Cursed Knight. {w=1.0}The one with the
    horse.’"
    shows mc bust at () during 0.
    "Sepp sighed.
    {p=1.0}‘My apologies. We don't sell this item.’"

label .disappointment:
    "‘Oh, {w=1.0}of course.’
    {p=0.5}‘That said,’ Josef continued, ‘there is a Toy Fair in the Eastern city tomorrow.
    {w=0.5}You may find what you want there.’"
    "‘Ah, thank you.’
    {p=0.5}She awkwardly glanced at the shelves again."
    shows lady look at () during 0.
    "‘I guess I will just have a quick look at the other toys,
    then.’"
    pause 1.0
    hides lady
    stop music fadeout 3.0
    "A minute later, she was gone."

label .uncle:
    pause 1.0
    shows uncle bust at (190, -15)
    $ renpy.pause(1.0)
    play music conflict
    "A man appeared from the back shop.
    {p}‘You should have shown her our products.’"
    "‘She asked for something and we didn't have it, {w=0.5}Uncle.
    {p=0.5}No need to redirect her to older toys.’"
    "‘They are not just old, they are classics.’
    {p}Josef was annoyed by the same old words,
    but he preferred avoiding direct confrontation."
    "‘Why not go to that Fair and meet toy makers,
    so we can make agreements to sell the latest toys in vogue?
    {w=0.5}This will surely bring us more customers.’"
    "‘Out of the question,’ the uncle objected.
    {p=0.5}‘I don't want to sell nicknacks made by people who
    don‘t even understand the basics.’"

label .basics:
    "The uncle started picking items from the shelves.
    {p}‘See that ball? Soft, yet sturdy. Ideal for indoor and outdoor play.
    {p}And that doll? Highly detailed clothes, close to what children play with in noble families."
    "‘And that top? Point of contact in metal to reduce friction. Can last
    hours and hours of play.’
    {p}{i}One minute was more than enough{/i}, Josef thought."
    pause 1.0
    "‘Already five?’ the uncle noticed. ‘It's about time we close. I let you inventory.’"
    hides uncle

# OPTIONAL
label .ledger:

label .cursed_knight:
    stop music fadeout 2.0
    scene fbg sunset with Dissolve(3.0)
    shows mc stand at (-240, 120)
    hides top
    "Half an hour later, Josef was done with the inventory.\n"
    shows cursed_knight_original at (-285, 110)
    "Still plunged in deep thought, he picked the only Cursed Knight in the shop. It was a first
    generation figure, still made in wood and with no movable
    parts."
    "Sir Victor Écaille introduced the toy 15 years go, along with its own story."
    "{i}A knight was bound to a cursed blade that kills every thing it touches.
    {w=0.5}He was banned from the very kingdom he protected because he was deemed too dangerous,
    yet continues fighting for its people.{/i}"
    "But Josef wasn't nostalgic. {w=0.5}It was now time to go and see what was made in the real world."

label .end:
    "END OF SCENE 1"
    "‘hello’"
    # jump s02
