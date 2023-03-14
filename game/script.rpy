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

show bg_0coldsleep
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
        show marnie happy
        m "Alright good. I was worried when you didn't respond right away."
        m "I can never tell how long you humans take in there."
        m "How are you feeling?"
        r "A little woozy. It felt like my heart was pounding in the back of my skull."
        show marnie normal
        m "That's to be expected. Emergency thaws are kind of rough..."
    "Where am I?":
        label start_whereami:
        hide bgblack with dissolve
        r "W-Where am I?"
        show marnie unhappy at sulk
        m "Seriously? Don't tell me the Cold Sleep messed with your memory..."
        m "I thought they fixed that issue..."
        show marnie normal
        m "Well what do you remember?"
        menu(screen ='choice'):
            "I'm a salvager":
                r "That I'm a Rookie space salvager?"
                m "Correct!{w=0.25} And...?"
                r "Um...{w=0.25} You're Marnie?"
                show marnie happy
                m "Yup!{w=0.25} All I needed to hear!"
                m "You should be fine!"
                r "R-Right..."
            "I don't know":
                r "Oh no!{w=0.25} {size=+06}I don't know anything!!!{/size}"
                m "..."
                r "..."
                m "..."
                show marnie with vpunchnowait
                play sound smack
                r "{size=+06}OW!{/size}"
                show marnie unhappy
                m "Stop messing around!"
                r "S-Sorry!"
    "...":
        r "..."
        m "Hello? Can you hear me?"
        m "Maybe something went wrong with the Cold Sleep pod again..."
        m "{size=+06}Hey Rookie! Wake up!{/size}"
        menu:
            "I'm awake!":
                jump start_awake
            "Where am I?":
                jump start_whereami
            "...":
                m "Hmmmmm... All the vitals look good..."
                show marnie at sway
                m "Rookie? Are you..."
                r "..."
                m "..."
                r "..."
                m "..."
                hide bgblack with disfastnowait
                show marnie with vpunchnowait
                play sound smack
                r "{size=+06}OW!{/size}"
                show marnie unhappy
                m "Stop messing around!"
                r "Sorry! I'm awake now!"
                m "Don't scare me like that! You should know better..."
show marnie normal
m "Anyways the Captain wants everyone on the bridge."
m "Just freshen up and meet everyone there."
r "Yes Marnie."
hide marnie with dissolve
dd "With this, Marnie leaves the room, and you begin to get out of the Cold Sleep pod."
dd "As you brush down your jumpsuit, you slowly glace around the room and attempt to regain your bearings."

##### ROOM 0 COLD SLEEP #####
$roommanager.setuproom(0)
##### ROOM 0 COLD SLEEP #####


label introbridge:

scene bg_1bridge with fade
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
show gelato happy at wiggle
if shower == True:
    g "No you're {size=+06}THE HUMAN{/size} salvager!"
    show gelato at wiggle
    g "The one and only!"
    show gelato unhappy at wiggle
    g "Not since that last one!"
    show gelato unhappy
    g "{size=-06}That one didn't last long...{/size}"
else:
    g "No you're {size=+06}THE SMELLY HUMAN{/size} salvager!"
    m "Hey. No one's allowed to pick on the Rookie but me."
    show gelato unhappy at wiggle
    g "But I'm not picking on the Rookie..."
show otus normal with dissolve:
    zoomnorm
    xalign 1.375
show marnie:
    ease 0.4 xalign -0.1
show gelato normal:
    ease .2 center
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0
o "You jabbersniffs sure took your sweet time!"
show marnie at sway
m "{size=-06}But I was the first one here...{/size}"
show gelato at wiggle
g "Sometimes Captain, you gotta go at a human's pace!"
r "What does that even mean?"
o "Shut it kid! We got a new job to do."
show marnie unhappy at hop
m "Wait? What?{w=0.25} We're heading back from a job right now!"
m "That luxury comet skipper is filling up our entire cargo hold!"
show gelato at wiggle
g "Maybe it's something really{w=0.25} {size=-06}really small...{/size}"
m "We're on a tight schedule Captain! If we're late by a even a single micro cycle, we'll take a huge penalty!"
show otus unhappy at sway
o "Hey! Quit being such a pippyflop!"
o "I’ve been scrapping ships longer than your people have been flying them!"
show otus happy
o "I know what I'm doing! And trust me, I think you’ll all want to be part of this!"
show sprocko happy with dissolve:
    zoomnorm
    xalign -0.575
show marnie:
    ease 0.2 xalign 0.1
show gelato:
    ease 0.1 xalign 0.62
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0
s "Hey BOSS!"
s "We got visual!"
o "Finally! Put it on screen, Sprocko!"

#play sound engines
show cg01 with dissolve
g "Woah, what is that?"
o "Sprocko,{w=0.25} tell them."
s "Well let's see...{w=0.25} Judging from the data it LOOKS like an orbital station built almost FIFTY cycles ago."
m "Now why would we be interested in an old orbital station?"
s "Because WE are getting strong zeta waves from that thing's reactor core."
m "OK..."
m "How strong?"
s "Nine hundred THOUSAND zetajoules... Enough to power an ENTIRE core world!"
show marnie normal
show otus normal
show sprocko normal
show gelato #shocked
hide cg01 with dissolve

dd "The room is silent, as the magnitude of that statement hangs in the air."
#show gelato #shocked at wiggle
show gelato unhappy at wiggle
g "T-That makes no sense!{w=0.25} How can a single space station have that much power?!"
show otus happy
o "Now you're getting it!"
o "This is an opportunity we can't miss. I'll jettison that entire smogdoffle comet skipper for this salvage if I have to!"
m "Are you sure those readings are correct?"
show sprocko unhappy
s "I quintuple checked it while YOU were all on ice."
show sprocko happy at hop
s "My calculations are PERFECT!"
show marnie unhappy at sulk
m "I don't like this... It's some sort of super secret, galactic government trick or something."
m "We step one foot on that thing, and {size=+06}BAM!{/size}{w=0.25} We’re sent to prison in a pocket dimension and never seen again!"
show sprocko unhappy
s "No, I checked all the flight charts and no one's been in this sector for AGES!"
s "It's a derelict and it's just been sitting there, SITTING!"
o "There's nothing to worry about! We get our hands on whatever is powering that reactor and we can all retire on any core world we want!"
show otus normal
o "What do you think Rookie?"

menu(screen ='choice'):
    "Marnie is right":
        r "Maybe we should listen to Marnie."
        show marnie happy
        r "This sounds dangerous and I don't want to mess up my first salvage operation."
        m "See even the Rookie can tell that this is too good to be true."
        show gelato happy at wiggle
        g "It must be that human intuition!"
        show sprocko at hop
        s "Oh come on! We NEED, no we MUST get on that station!"
        s "Captain? What do you say?"
        o "How about we put it to a vote?"
        show otus at sway
        o "My vote obviously counts as two."
        show marnie unhappy
        o "So if we tally it all up...{w=0.25} Tie breaker goes to the Captain..."
        show otus happy at hop
        o "Looks it's decided! We're going!"
        show sprocko happy
        show gelato at wiggle
        g "Yay democracy!"
        r "That doesn't seem right..."
    "The Captain is right":
        r "Captain Otus is right."
        show otus happy
        show sprocko normal
        show gelato normal
        show marnie unhappy
        r "If we miss this opportunity we'll be kicking ourselves for the rest of our lives."
        r "I vote that we check it out at least."
        o "Yeah see! Good Rookie!"
        o "Who's a good Rookie! You are! That's who!"
        r "Something seems off about that statement..."
        show gelato happy at wiggle
        g "{size=-06}Such a good human...{/size}"
        s "Oh! I can not WAIT to play with whatever is in there!"
        show sprocko happy at shake
        s "{size=+06}Gehehehehe!{/size}"
        m "Are we actually doing this?"
        o "If anything looks off, we'll high tail it out of there. I promise."

m "Ugh...{w=0.25} Fine. But you're covering for any late penalty we get."
show sprocko at normalize
o "Alright Sprocko. Guide her in."
show sprocko happy:
    ease 0.8 xalign 3.0
show marnie normal:
    ease 0.4 xalign -0.1
show gelato normal:
    ease .2 center
pause 0.25
s "{cps=99}{size=+06}Ghwahahahahahaha!{/size}{/cps}"
show gelato happy at wiggle
g "Yippie!"
show marnie unhappy at sway
m "This is such a bad idea."
o "Alright Rookie, you're on point."
show bgblack2 with dissolve
#play sound landing

dd "Next area is a test, look at window to continue"

##### ROOM 1 BRIDGE #####
$roommanager.setuproom(1) #testing for now
##### ROOM 1 BRIDGE #####



label introhub:
scene bg_2hub with fade

show marnie normal with dissolve:
    zoomnorm
    ease 0.4 xalign -0.1
show gelato normal with dissolve:
    zoomnorm
    ease .2 center
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0
show otus normal with dissolve:
    zoomnorm
    xalign 1.35
show sprocko normal with dissolve:
    zoomnorm
    xalign -0.5
show marnie:
    ease 0.2 xalign 0.1
show gelato:
    ease 0.1 xalign 0.62
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0

o "TEST."

# o “For once, I agree with _Goof.”
# Goof “Ha, thanks!”
# Goof “Wait, what do you mean for once-”
#
# Landing
#
# “The ship lands in a spacious docking area, and we quickly deploy ourselves onto the ships.”
# Goof “Ooh, this looks very humany, don’t you think, Newbie?”
# You “I guess…”
# Tech “Huh, you think so, __Goof?”
# Goof “Yeah! Look, the size of the doors, the layout of the room it screams Earth Architecture!”
# Goof “And smell that air! The perfect mixture of Oxygen, Nitrogen and a few other gases.”
# Goof “Perfect for the homesick earthling!”
# Leader “Smell that air- __Goof, what have I told you about wearing a helmet?”
# Goof “Aw man, I hate having to wear that helmet. It makes me feel all stuffy.”
# Leader “Please, __Goof. If I can put up with being inside this tin can, you can wear a helmet for a bit.”
# Grouch “C’mon, __Goof, take this seriously. I want us in and out as quickly as we can!”
# Tech “No way, Grouch, look at this place! Even this docking area is years ahead of anything on our ship…”
# Grouch “__Tech, one of my kids transport pods is years ahead of the Junk.”
# Tech “Hey! She tries her best, darn it.”
# Leader “Focus, people. We need to get past this door. Newbie, grab a Fission Slicer from our tools and use it on the door.”
# Leader “Everyone else, take some time to try and take things seriously for a little while…”
#
# EnteringHub
#
# “__Tech begins to slice the slice through the doors.”
# Grouch “So we’re just going to… Slice this metal man open then?”
# Tech “That’s the plan! Just let me finish getting it working…”
# Grouch “It just seems that, y’know, breaking into-”
# Goof “Woah, woah, who said anything about breaking into? We’re just cutting into, get me?”
# Goof “Hey Newbie, who are those guys your people have with the small knives who save lives?”
# You “...Surgeons?”
# Goof “Yeah, that’s the one! Would you say they ‘break into’ people bodies to fix them?”
# You “No, because that would be a really weird thing to-”
# Goof “Exactly, __Grouch, it would be weird to say.”
# Grouch “Point is, a place all sealed up like this, with no clear cause why it’s empty…”
# Grouch “Just seems like a bad idea, is all.”
# Leader “__Grouch, usually I’d agree with you, but the potential…”
# Leader “This is the sort of opportunity you only get once in a lifetime!”
# Grouch “Fine, but if this all goes horribly wrong and we all die, I get bragging rights.”
# Goof “Aw cool your jets, __Grouch! What could possibly go wrong?”
# “And then everything went wrong.”
# Tech “I’ve managed to slice through the door!”
# Leader “Okay! Everyone head in!”
#
# #Change background to hub
#
# You “Woah…”
# Goof “Wow, this is some fancy, badass human stuff!”
# Leader “Oh, we are absolutely taking everything that isn’t nailed down here.”
# Grouch “Huh, maybe this isn’t such a bad ide-”
#
# # strange notification sound
#
# Leader “What was that sound?”
# Tech “!”
# Leader “__Tech? What is it?”
# Tech “I just got a bill?”
# AI “Yes. For the door.”
# Tech “What? Who said that?”
# Grouch “I knew this was going to go badly…”
# AI “Hello. This is my space station. Please leave.”
# Goof “Gah! What the hell was that!”






dd "END FOR NOW"

return

############## ROOM MANAGER ##############

label enterroom:

    # "[roommanager.currentroom.name]"

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
