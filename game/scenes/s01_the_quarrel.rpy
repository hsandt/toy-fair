label s01:
    jump .intro

    # debug
    scene fbg sunset
    showd screen illustframe("bg toyshop day")
    jump .end

label .intro:
    scene fbg day

    $ renpy.pause(0.5)
    showd screen illustframe("cg top") during 2.0
    play music spinning_top loop
    $ renpy.pause(2.0)
    "The top had been spinning for {i}a good
    minute{/i}, and didn't seem ready to slow down
    any time soon."
    hided screen illustframe
    $ renpy.pause(1.0)

label .focus:
    showd screen illustframe("bg toyshop day")
    shows cursed_knight_original as knight1 at (-345, 100)
    shows cursed_knight_original as knight2 at (-365, 105)
    shows cursed_knight_original as knight3 at (-355, 170)
    shows cursed_knight_original as knight4 at (-335, 33)
    shows focus smog at (0, 0)
    shows mc bust behind a at (0, 5)
    shows top spinning at (45, 28)
    $ renpy.pause(1.0)
    "Josef was staring at the toy, as hypnotized.
    {w}He stopped expecting anything more from it a moment ago,
    but couldn't look away."

label .lady:
    play sound chime
    pause 1.0
    hides focus
    shows lady behind focus at (-160, 90)
    $ renpy.pause(1.0)
    "A lady entered and started looking at the shelves.
    {w=0.5}Josef remained focused on the spinning object."
    pause 1.0

label .shout:
    shows fx_shout at (230, -100) during 0.
    play sound hit_table
    "‘Sepp!’ shouted a voice from the back shop.
    {p}‘How many times have I told you to welcome customers?!’"
    hides fx_shout during 0.

label .welcome:
    "Josef stopped the top with his hand.\n"
    shows mc_hand_left at (45, 25) during 0.
    shows top stopped at (45, 32) during 0.
    stop music
    pause 1.0
    shows mc bust smile at () during 0.
    play music toyshop
    "‘Welcome! What can I do to help you?’"
    hides mc_hand_left during 0.
    "‘I am looking for a {b}Cursed Knight figure{/b} for my son.’
    {p}‘I have exactly what you need. Please have a look at the collection of Knights on your left.’"
    pause 0.5
    shows lady look at () during 0.
    pause 0.5
    "‘We have the Soldier with the Burnt Face, the Vengeful Dragon,
    the original Cursed Knight of course, but also many others.’"

label .disappointment:
    shows lady at () during 0.
    "‘Interesting,’ the woman started, {w=0.5}‘but I expected something more... {w=0.5} contemporary.
    {w=0.5}Such as the Knight of the Thunder Blade.’"
    shows mc bust at () during 0.
    "‘I see. {w=0.5}Actually, there is a {b}Toy Fair{/b} in the {b}Eastern city{/b} tomorrow.
    {w=0.5}Maybe you will have better luck there.’"
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
    {p}‘You should have insisted to sell her the first generation figures.
    {p=0.5}Or at least a second generation.’"
    "‘She asked for a fifth generation and we didn't have it, {w=0.5}Uncle.
    {p=0.5}No need to redirect her to older toys.’"
    "‘They are not just old, they are classics. Most buyers simply don't get it.’
    {p}Josef was annoyed by the same old words,
    but he preferred avoiding direct confrontation."
    "‘Why not go to that Fair and meet toy makers to make agreements
    on the latest toys in vogue?
    {w=0.5}This will surely bring us more customers.’"
    "‘Out of the question,’ the uncle objected.
    {p=0.5}‘I don't want to sell nicknacks made by people who
    don‘t even understand the basics.’"

label .basics:
    "‘High quality products are our pride, and we contact specialized makers to ensure that quality.’"
    pause 0.5
    shows uncle bust pick at () during 0.
    "The uncle started picking items from the shelves.
    {p}‘See that ball? Soft, yet sturdy. Ideal for indoor and outdoor play.
    {p}And that doll? Highly detailed clothes, like what children play with in noble families."
    shows uncle bust showing at () during 0.
    "‘And that top? Point of contact in metal to reduce friction. Can last
    hours and hours of play.’
    {p}{i}One minute was more than enough{/i}, Josef thought."
    pause 1.0
    "‘It's already five?’ the uncle noticed.
    {p=0.5}‘It's about time we close. {w=0.5}I let you inventory.’"
    hides uncle

# OPTIONAL
label .ledger:

label .cursed_knight:
    stop music fadeout 2.0
    scene fbg sunset with Dissolve(3.0)
    shows mc stand at (-240, 120)
    hides top
    "Half an hour later, Josef was done with the inventory.\n"
    shows cursed_knight_original as knight1 at (-285, 110)
    "He picked one of the Cursed Knight figures to examine it. It was a first
    generation figure, still made in wood and with no movable parts."
    "Sir Victor Écaille introduced the character 15 years go, along with its own story."
    "{i}A knight was bound to a cursed blade that killed every thing it touched.
    {w=0.5}He was banned from the very kingdom he used to fight for because he was deemed too dangerous,
    and now lives between a desire of vengeance and the will to continue protecting people.{/i}"
    "A character like this was a revolution at the time, and it quickly gained tremendous success
    by children and adults alike."
    "But Josef wasn't nostalgic. {w=0.5}It was now time to go and see what novelty awaited him in the real world."
    hides mc
    hides knight1
    hides knight2
    hides knight3
    hides knight4
    hided screen illustframe
    $ renpy.pause(2.0)

label .end:
    jump s02
