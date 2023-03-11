# START

# CHEAT SHEET
# WAIT, NO WAIT, and TEXT stuff
# {w=0.25} #wait a small amount
# {nw} #no waiting text jumps to next text

# {cps=99}{/cps} #the speed of text 99 is fast 45 is normal 11 is slow
# {cps=11}{/cps}
# {cps=0}{/cps} # 0 = instant

# {i}{/i}
# {b}{/b}
# {size=+04}{/size}


#hi this is the comment to check repo

label start:

scene START
show bg_ship1
show bgblack
pause 0.75

qq "Hey! Are you awake yet?"
hide bgblack with dissolveslow
dd "You awaken to the sound of your heart beginning to pump again, as you stir from the Cold Sleep."
show bgblack with dissolve:
    alpha 0.75
hide bgblack with dissolve
r "Ugh...."
show marnie normal with dissolve:
    zoomnorm
    center
m "Newbie, wake up!"
dd "Standing above you, having pressed the emergency thaw button, is Marnie."

menu:
    "I'm awake!":
        label start_awake:
        r "I'm awake, I'm awake!"
        m "Good. Sometimes you humans can be so fickle."
    "Where am I?":
        label start_whereami:
        r "W-Where am I?"
        m "Seriously? Did the cold sleep scramble your brain?"
        m "You're on a salvager ship hurtling through space and you're late for a team meeting."
        r "R-right!"
    "Who am I?":
        label start_whoami:
        r "W-Who am I?"
        m "Seriously? Did the cold sleep scramble your brain?"
        m "You're our softest squishiest newest rookie human and you're late for a team meeting."
        r "R-right!"
    "...":
        r "..."
        m "Hmmmmm... There does't look like there's anything wrong with you."
        m "Your vitals should be fine... "
        m "Hey are you awake yet?"
        menu:
            "I'm awake!":
                jump start_awake
            "Where am I?":
                jump start_whoami
            "Who am I?":
                jump start_whereami
            "...":
                r "..."
                m "..."
                show marnie with vpunch
                m "I know you're awake! Stop being lazy!"
                r "Ow! OK I'm awake!"

m "Anyways the Captain wants everyone on the bridge pronto."
r "Y-Yes Ma'm!"
hide marnie with dissolve
dd "With this, Marnie leaves the room, and you begin to get out of the Cold Sleep pod, brushing down your jumpsuit."
dd "You grab a SuperValue protein bar, some trihydrated milk and try to ignore the lack of taste as you make your way to the bridge."

scene bg_ship2 with fade
show marnie normal with dissolve:
    zoomnorm
    leftish
m "Hey, look who finally made it!"
show gelato normal with dissolve:
    zoomnorm
    rightish
    wiggle
g "Good morning, Sleeping Beauty!"

r "Morning?{w=0.25} Why is it morning?"
show gelato at wiggle
g "I ask myself that everyday, Newbie!"

r "No, I mean, I’m scheduled for the night shift, right?"
show otus normal with dissolve:
    zoomnorm
    xalign 1.35
show marnie:
    ease 0.5 xalign -0.1
show gelato:
    ease .25 center
pause 0.25
show gelato at wiggle
o "Sorry, new kid. Schedules are made to be broken."

m "Hey, Captain Otus, there you are! Why did you need us all here?"
show gelato at wiggle
g "Can’t you see you made Newbie all grouchy?"

r "I’m fine, I just wanted to moan."

o "You can moan later, kid. We got a new job to do."

m "What?{w=0.25} We just came back from a job!"

m "That Luxury Comet Skipper is the reason we’re in this chartless part of the galaxy in the first place!"
show gelato at wiggle
g "Yeah, who knew an autopilot would be so bad at navigation?"

r "It took a long time salvaging all those parts of the ship from the asteroid field…"

m "Exactly, and union rules specifically state that we don’t have to do shit until we’re back at homebase-"

o "Hey, hey! Don’t start quoting union rules to me! I’ve been scrapping ships longer than your people have been flying them!"

o "I know I can’t make you do anything, but trust me, I think you’ll all want a part of this."

show sprocko normal with dissolve:
    zoomnorm
    xalign -0.45
show marnie:
    ease 0.25 xalign 0.125
show gelato:
    ease .15 xalign 0.625
    wiggle
s "Hey Boss!"

s "We got visual!"

o "Finally! Put in on screen, Sprocko!"

show cg01 with dissolve
# See the space station on screen

g "Woah, what is that?"
o "Sprocko, any ideas?"
s "I…{w=0.25} I don’t know! There’s nothing in the database, and I’ve never seen anything like it!"
m "Then why the hell are we interested in it?"
s "Because I’m getting a very strong Zexacite signal coming from that things engines."
m "... How strong?"
s "200 micro frequencies."

hide cg01 with dissolve
dd "The room is silent, as the magnitude of that statement hangs in the air."

show gelato at wiggle
g "Holy shit! That’s like, what, ten times the latest engine models, right?"

o "Yep! See why I wanted all of us here?"

m "This has got to be a trick of some sort."

r "Who would be tricking us?"

m "I dunno, it’s gotta be some super secret, government bull or something."

m "We step one foot on that thing, and BAM! We’re sent to prison in a pocket dimension and never seen again!"

s "I highly doubt that. There’s no signs of life, and it doesn’t seem to be doing anything but orbiting."

m "Still seems to risky. I say we ping it and report it when we get back to home base."
show gelato at wiggle
g "Aw, come on! We report it without any evidence, we’ll get like a weeks holiday at best!"

o "For once, I agree with Gelato."
show gelato at wiggle
g "Ha, thanks!"
show gelato at wiggle
g "Wait, what do you mean for once-{nw}"

o "We should at least dock, try to gain some evidence…"

s "Maybe some cutting-edge technology to play- I mean, experiment with…"

o "I’ll pretend I didn’t hear that."

m "I want it on record that I think this is a bad idea."

m "But if everyone else is on board, I guess I should make sure you don’t get yourself killed."
show gelato at wiggle
g "Aww, thanks bud!"

o "Good, I don’t need to argue with you then.{w=0.25} Everyone, suit up."

o "It’s time to go scavenging!"
show bgblack2 with dissolve
dd "END FOR NOW"

return
