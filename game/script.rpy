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


label start:

scene START

show bg_ship1
show bgblack
pause 1.5
qq "Hey..."
qq "Hey Rookie!"
play sound heartbeat volume 0.2
show bgblack with dissolveslow:
    alpha 0.5
dd "You awaken to the sound of your heart beginning to pump again, as you stir from the Cold Sleep."
play sound heartbeat volume 0.2
show bgblack with dissolve:
    alpha 0.85
show bgblack with dissolve:
    alpha 0.25
r "Ugh...."
show marnie normal behind bgblack with dissolve:
    zoomnorm
    center
dd "Standing above you, having pressed the emergency thaw button, is Marnie."
play sound heartbeat volume 0.2
show bgblack with dissolve:
    alpha 0.65
show bgblack with dissolve:
    alpha 0.25
m "Come on Rookie, wake up!"
menu(screen ='choice'):
    "I'm awake!":
        label start_awake:
        hide bgblack with dissolve
        r "I'm awake! I'm awake!"
        m "Alright good. I was worried when you didn't respond right away."
        m "I can never tell how long you humans take in there..."
    "Where am I?":
        label start_whereami:
        hide bgblack with dissolve
        r "W-Where am I?"
        m "Seriously? Don't tell me the Cold Sleep messed with your memory..."
        m "I thought they fixed that issue..."
        m "Well what do you remember?"
        menu(screen ='choice'):
            "I'm a salvager":
                r "That I'm a Rookie space salvager?"
                m "Correct!{w=0.25} And...?"
                r "Um...{w=0.25} You're Marnie?"
                m "Yup!{w=0.25} All I needed to hear."
                m "You should be fine."
                r "R-Right..."
            "I don't know":
                r "Oh no!{w=0.25} {size=+06}I don't know anything!!!{/size}"
                m "..."
                r "..."
                m "..."
                show marnie with vpunchnowait
                play sound smack
                r "{size=+06}OW!{/size}"
                m "Stop messing around!"
                r "S-Sorry!"
    "...":
        r "..."
        m "Hmmmmm... Can you hear me?"
        m "Maybe something went wrong with the Cold Sleep pod again..."
        m "..."
        m "{size=+06}Hey Rookie! Wake up!{/size}"
        menu:
            "I'm awake!":
                jump start_awake
            "Where am I?":
                jump start_whereami
            "...":
                r "..."
                m "..."
                hide bgblack with disfastnowait
                show marnie with vpunchnowait
                play sound smack
                r "{size=+06}OW!{/size}"
                m "Stop messing around!"
                r "Sorry! I'm awake now!"
m "Anyways the captain wants everyone on the bridge."
m "Just freshen up and meet everyone there."
r "Yes Marnie!"
hide marnie with dissolve
dd "With this, Marnie leaves the room, and you begin to get out of the Cold Sleep pod, brushing down your jumpsuit."
r "My head IS a little foggy though... Maybe I should take look around a bit."

#LET PLAYER DO THINGS HERE
$roommanager.setuproom(0)
label showerchoice:
dd "A narrow sonic shower sits uncomfortably in the corner of this room."
menu(screen ='choice'):
    "take a shower":
        #play sound shower
        dd "You hop in and turn the dial. A wave of ultra sonic pulses hits you all over."
        r "Ahhh! I don't think I can ever get used to this!"
        $ shower = True
    "leave":
        dd "You head to the bridge."
#LET PLAYER DO THINGS HERE

scene bg_ship2 with fade
show marnie normal with dissolve:
    zoomnorm
    leftish
if shower == True:
    m "Jeez Rookie,{w=0.25} took you long enough."
else:
    m "Oof Rookie,{w=0.25} you still smell a bit funny."
show gelato normal with dissolve:
    zoomnorm
    rightish
    wiggle
if shower == True:
    g "Hey there human salvager!"
else:
    g "Smells like a perfectly normal human to me!"
if shower == True:
    r "Yup. That's me. The human salvager..."
else:
    r "Yup. That's me. The smelly human salvager..."
show gelato at wiggle
if shower == True:
    g "No you're {size=+06}THE HUMAN{/size} salvager!"
    show gelato at wiggle
    g "The one and only!"
    show gelato at wiggle
    g "Not since that last one!"
    g "{size=-06}That one didn't last long...{/size}"
else:
    g "No you're {size=+06}THE SMELLY HUMAN{/size} salvager!"
    m "Hey. No one's allowed to pick on the Rookie but me."
    show gelato at wiggle
    g "But I'm not picking on the Rookie..."
show otus normal with dissolve:
    zoomnorm
    xalign 1.35
show marnie:
    ease 0.4 xalign -0.1
show gelato:
    ease .2 center
pause 0.25
show gelato at wiggle
o "You Jabbersniffs sure took your sweet time!"
m "{size=-06}Wait.{w=0.25} But I was the first one here...{/size}"
show gelato at wiggle
g "Sometimes captain, you gotta go at a human's pace."
r "What does that even mean?"
o "Shut it kid! We got a new job to do."
m "Wait? What?{w=0.25} We're heading back from a job right now!"
m "That luxury comet skipper is filling up our entire cargo hold!"
show gelato at wiggle
g "Maybe it's something really{w=0.25} {size=-06}really small...{/size}"
m "We're on a tight schedule captain! We'll take a big penalty even if we're late by a single micro cycle!"
o "Hey!{w=0.25} Quit being such a Squeaklebeak! I’ve been scrapping ships longer than your people have been flying them!"
o "I know what I'm doing! And trust me, I think you’ll all want to be part of this."
show sprocko normal with dissolve:
    zoomnorm
    xalign -0.5
show marnie:
    ease 0.2 xalign 0.1
show gelato:
    ease 0.1 xalign 0.62
pause 0.25
show gelato at wiggle
s "Hey BOSS!"
s "We got visual!"
o "Finally! Put it on screen, Sprocko!"

#play sound engines
show cg01 with dissolve
g "Woah, what is that?"
o "Sprocko,{w=0.25} tell them."
s "Well let's see...{w=0.25} Judging from the data it LOOKS like a custom orbital station built almost FIFTY cycles ago."
m "Now why would we be interested in an old orbital station?"
s "Because WE are getting strong zetacite readings from that thing's reactor core."
m "OK..."
m "How strong?"
s "Nine hundred THOUSAND zetajoules... Enough to power an ENTIRE core world."
hide cg01 with dissolve

dd "The room is silent, as the magnitude of that statement hangs in the air."
show gelato at wiggle
g "T-That makes no sense!{w=0.25} How can a single station have enough power to do that?!"
o "Now you're getting it!"
o "This is an opportunity we can't miss. I'll jettison that entire smogdraffle comet skipper for this salvage if I have to!"
m "Are you sure those reading are correct?"
s "I quintuple checked it while YOU were all on ice."
s "My calculations are PERFECT!"
m "I don't like this... It's some sort of super secret, galactic government trick or something."
m "We step one foot on that thing, and {size=+06}BAM!{/size}{w=0.25} We’re sent to prison in a pocket dimension and never seen again!"
s "No way! I checked the flight charts and no one's been in this sector for AGES!"
o "There's nothing to worry about! We get our hands on whatever is powering that reactor and we can all retire on any core world we want!"

menu(screen ='choice'):
    "Marnie is right.":
        r "Maybe we should listen to Marnie."
        r "This sounds dangerous and I don't want to mess up my first salvage operation."
        m "See even the Rookie can tell that this is too good to be true."
        show gelato at wiggle
        g "It must be that human intuition!"
        s "Oh come on! We NEED, no we MUST get on that station!"
        s "Captain? What do you say?"
        o "How about we put it to a vote?"
        o "My vote counts as two and as captain I always win the tie breaker."
        o "If we tally up the votes...{w=0.25} It looks like... We're going!"
        show gelato at wiggle
        g "Yay democracy!"
        r "That's not how that works..."
    "The captain is right.":
        r "Captain Otus is right."
        r "If we miss this opportunity we'll be kicking ourselves for the rest of our lives."
        o "Yeah see! Good Rookie!"
        o "Who's a good Rookie! You are that's who!"
        r "Something feels off about that statement..."
        show gelato at wiggle
        g "{size=-06}Such a good human...{/size}"
        s "Oh! I can't WAIT to play with whatever is in there!"
        m "Are we actually doing this?"
        o "If anything looks off we'll high tail it out of there. I promise"

m "Ugh...{w=0.25} Fine. But you're covering for any late penalty we get."
o "Alright Sprocko. Guide her in."
show sprocko:
    ease 0.8 xalign 3.0
show marnie:
    ease 0.4 xalign -0.1
show gelato:
    ease .2 center
pause 0.25
show gelato at wiggle
s "{size=+06}Ghwahahahahahaha!{/size}"
show gelato at wiggle
g "Yippie!"
m "This is such a bad idea."
o "Alright Rookie, you're on point."
show bgblack2 with dissolve
#play sound landing









dd "END FOR NOW"


return




label enterroom:

    "[roommanager.currentroom.name]"

    $roommanager.changeinteractionlevel(0)

    call screen makeplayerUI(roommanager,roommanager.gotnav,roommanager.gotinv)



screen makeinteractables(targetinteractables, roommanagerref):

    default localrmanref = roommanagerref


    for ti in targetinteractables:
        if ti.intertype == 1:
            imagebutton:
                xpos ti.horposition
                ypos ti.verposition
                auto ti.imageref[ti.interprogress]
                action [SensitiveIf((ti.interprogress in ti.interrangequest)and(localrmanref.currinterlayer == 0)), Hide("makeinteractables"), Hide("makeplayerUI"), Function(localrmanref.intiateinteraction,ti.labelref)]


        elif ti.intertype == 2:
            frame:
                xpos ti.horposition
                ypos ti.verposition
                xpadding ti.xpad
                ypadding ti.ypad
                textbutton ti.textref  action NullAction()


screen interactableinteractionscreen(selectedinteractable):

    default localinterref = selectedinteractable
    image "[localinterref.menuimageref]" xalign 0.3 yalign 0.5



screen makeplayerUI(roommanagerref,navon,invon):

    default localrmanref = roommanagerref


    if (navon == 0):
        frame:
            xpadding 40
            ypadding 20
            xalign 0.9
            yalign 0.1
            textbutton "Navigation" action [SensitiveIf(localrmanref.currinterlayer == 0), Hide("makeplayerUI"), Show("navscreen",None,localrmanref)]

    if (invon == 0):
        frame:
            xpadding 40
            ypadding 20
            xalign 0.9
            yalign 0.2
            textbutton "Inventory" action NullAction()









screen navscreen(roommanagerref):

    modal True
    default localrmanref = roommanagerref
    default roomstogoto = []
    default count = 0

    for rtg in localrmanref.currentroom.adjacentrooms:
        $ roomstogoto.append(localrmanref.rooms[rtg])


    frame:
        xpadding 40
        ypadding 20
        xalign 0.9
        yalign 0.1
        textbutton "Back" action [Hide("navscreen"),Show("makeplayerUI",None,localrmanref)]


    for ri in roomstogoto:


        if (ri.locked == 0):

            imagebutton:
                xalign 0.5
                yalign (0.2 + (0.2*count))

                if (ri.discovered == 0):
                    auto ri.navicon
                else:
                    auto "iconunknown_%s.jpg"
                action [Hide(),Function(localrmanref.setuproom,ri.idnum)]
        else:

            imagebutton:

                xalign 0.5
                yalign (0.2 + (0.2*count))

                if (ri.discovered == 0):
                    auto ri.navicon
                else:
                    auto "iconunknown_%s.jpg"

                action [NullAction()]

            image "iconlocked.jpg" xalign 0.6 yalign (0.2 + (0.2*count))

        $ count += 1
