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

############################TEST BLOCK
############################TEST BLOCK

##rollback messes with item collecting
#$config.rollback_enabled = False

#$inventory.items.append(item_fittings)
#jump powerup_event

############################TEST BLOCK
############################TEST BLOCK

$roommanager.setuproominstant(0)
stop music fadeout 1.0
scene START

label introcold:
show bg_0cold_room
show bgblack
pause 1.5

qq "Hey..."
qq "Hey Rookie!"
play sound heartbeat volume 0.3
show bgblack with dissolveslow:
    alpha 0.5
dd "You awaken to the sound of your heart beginning to pump again, as you stir from the Cold Sleep."
play sound heartbeat volume 0.4
show bgblack with dissolve:
    alpha 0.85
show bgblack with dissolve:
    alpha 0.25
r "Ugh...."
show marnie normal behind bgblack with dissolve:
    zoomnorm
    center
dd "Standing above you, having pressed the emergency thaw button, is Marnie."
play sound heartbeat volume 0.5
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
        m "I can never tell how long you humans take in there!"
        show marnie normal
        m "How are you feeling?"
        r "A little woozy. It feels like my heart is pounding in the back of my skull..."
        m "That's to be expected. Emergency thaws are kind of rough..."
    "Where am I?":
        label start_whereami:
        hide bgblack with dissolve
        r "W-Where am I?"
        show marnie shocked at sulk
        m "Seriously? Don't tell me the Cold Sleep messed with your memory..."
        m "I thought they fixed that issue..."
        show marnie normal
        m "You're on the Rusty Clover. A salvager ship."
        r "Oh... I think already I knew that..."
        m "Well what else do you remember?"
        menu(screen ='choice'):
            "I'm a salvager":
                r "That I'm the Rookie space salvager?"
                m "Correct!{w=0.25} And...?"
                r "Um...{w=0.25} You're Marnie?"
                show marnie happy
                m "Yup!{w=0.25} All I needed to hear!"
                m "Your vitals are one hundred percent!"
                m "You should be fine!"
                r "R-Right..."
            "You're Marnie":
                r "Your name is Marnie. The ship's navigator?"
                show marnie happy
                m "Yup!{w=0.25} That's right!"
                m "I also do other important tasks like finance, scheduling, and sometimes waking up Rookies from their Cold Sleep."
                r "Yeah... I think I knew that too."
                m "You're perfectly fine!"
                r "I guess I am..."
            "Nothing!":
                r "Oh no!{w=0.25} {size=+06}I dont remember anything else!!!{/size}"
                show marnie shocked at hop
                r "{size=+06}Ahhhhhhh!{/size}"
                show marnie normal
                m "..."
                r "..."
                m "..."
                show marnie with vpunchnowait
                play sound smack volume 0.8
                r "{size=+06}OW!{/size}"
                show marnie shocked at hop
                m "Stop messing around!"
                r "S-Sorry!"
    "...":
        r "..."
        m "Hello? Can you hear me?"
        m "Maybe something went wrong with the Cold Sleep pod again..."
        show marnie shocked at hop
        m "{size=+06}Hey Rookie! Wake up!{/size}"
        menu:
            "I'm awake!":
                jump start_awake
            "Where am I?":
                jump start_whereami
            "...":
                r "..."
                show marnie normal at sulk
                m "Hmmmmm... All the vitals look good..."
                show marnie at sway
                m "Rookie? Are you..."
                r "..."
                m "..."
                r "..."
                m "..."
                hide bgblack with disfastnowait
                show marnie with vpunchnowait
                play sound smack volume 0.8
                r "{size=+06}OW!{/size}"
                show marnie shocked at hop
                m "Stop messing around!"
                r "Sorry! I'm awake now!"
                m "Don't scare me like that!"
                show marnie normal at sulk
                m "You should know better..."
show marnie normal
m "Anyways the Captain wants everyone on the bridge."
m "Just freshen up and meet everyone there."
r "Sure thing Marnie."
hide marnie with dissolve

play music ambience volume 0.15

##### this sets up the event when you enter room number, needs name of label as string
$roommanager.addeventstoroom(1,"introbridge")

dd "As you climb out of the Cold Sleep pod, you slowly glance around the room in an attempt to regain your bearings."

##### ROOM 0 COLD SLEEP #####
$roommanager.returnfrominteraction(roommanager.currentroom)
##### ROOM 0 COLD SLEEP #####

##### BRIDGE #####

label introbridge:
stop music fadeout 1.0
scene bg_1bridge_room with fade
show marnie normal with dissolve:
    zoomnorm
    leftish
play music floatingby volume 0.22
if shower == True:
    m "Jeez Rookie,{w=0.25} took you long enough."
else:
    m "Oof Rookie,{w=0.25} you still smell a bit funny."
show gelato normal behind marnie with dissolve:
    zoomnorm
    rightish
    wiggle
if shower == True:
    g "Hey there human salvager!"
else:
    g "Smells like a perfectly normal human salvager to me!"
r "Yup. That's me. The human salvager..."
show gelato happy at wiggle
if shower == True:
    g "Yeah! You're {size=+06}THE HUMAN{/size} salvager!"
    show gelato at wiggle
    g "The one and only!"
    show gelato at wiggle
    g "Not since that last one!"
    show gelato unhappy
    g "{size=-06}That one didn't last very long...{/size}"
else:
    g "No you're {size=+06}THE SMELLY HUMAN{/size} salvager!"
    m "Hey. No one's allowed to pick on the Rookie but me."
    show gelato unhappy at wiggle
    g "But I'm not picking on the Rookie..."
show otus unhappy with dissolve:
    zoomnorm
    xalign 1.375
show marnie:
    ease 0.4 xalign -0.1
show gelato normal:
    ease .2 center
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0
o "Gahhh! Where have you all been?!"
o "You jabbersniffs sure took your sweet time!"
show marnie at sway
if shower == True:
    m "{size=-06}But I was the first one here...{/size}"
else:
    m "Hey! I was here the whole time!"
    o "Bah! Whatever!"
show gelato at wiggle
g "Sometimes Captain, you gotta go at a human's pace!"
r "What does that even mean?"
show otus normal at wiggle
o "Shut it Rookie! We got a new job to do!"
show marnie unhappy at hop
m "Wait?! What?!{w=0.25} We're heading back from a job right now!"
m "That luxury comet skipper is filling up our entire cargo hold!"
show gelato at wiggle
g "Maybe it's something really{w=0.25} {size=-06}really small...{/size}"
m "We're on a tight schedule Captain! If we're late by a even a single micro cycle, we'll take a huge penalty!"
show otus unhappy at sway
o "Hey! Quit being such a squigglybeak!"
o "I’ve been scrapping ships longer than your people have been flying them!"
o "I know what I'm doing!"
show otus happy
o "And trust me! I think you’ll all want to be part of this!"
show sprocko happy with dissolve:
    zoomnorm
    xalign -0.575
show marnie normal:
    ease 0.2 xalign 0.1
show gelato:
    ease 0.1 xalign 0.62
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0
s "Hey BOSS!"
s "We got visual!"
o "Finally! Put it on screen, Sprocko!"
dd "With a simple click, the main screen turns on and a large orbital station comes into view."

show CG1 with dissolve
g "Woah, what is that?"
o "Sprocko,{w=0.25} tell them."
s "Well let's see...{w=0.25} Judging from the data it looks like an orbital station built over FIFTY cycles ago."
m "Now why would we be interested in an old orbital station?"
s "Because WE are getting strong zeta waves from that thing's reactor core."
m "OK..."
m "How strong?"
s "Nine hundred THOUSAND zetajoules... Enough to power an ENTIRE core world!"
show marnie shocked
show otus normal
show sprocko normal
show gelato shocked
hide CG1 with dissolve

dd "The room is silent, as the magnitude of that statement hangs in the air."
show gelato shocked at wiggle
g "T-That makes no sense!{w=0.25} How can a single space station have that much power?!"
show otus happy
o "Now you're getting it!"
o "This is an opportunity we can't miss."
o "I'll jettison that entire smogdoffle comet skipper for this salvage if I have to!"
m "Are you sure those readings are correct?"
show sprocko unhappy
s "I quintuple checked it while YOU were all on ice."
show sprocko happy at hop
s "My calculations are PERFECT!"
show marnie unhappy at sulk
m "I don't like this... It's some sort of super secret, galactic government trick or something."
m "We step one foot on that thing, and {size=+06}BAM!{/size}{w=0.25} We’re sent to prison in a pocket dimension and never seen again!"
show sprocko unhappy
s "I checked ALL the flight charts and no one's been in this sector for AGES!"
show sprocko shocked
s "It's a derelict and it's just been sitting there, SITTING!"
o "There's nothing to worry about!"
o "We've pinged it over and over with no response."
o "It's completely open for salvage!"
o "We get our hands on whatever is powering that reactor and we can all retire on any core world we want!"
show otus normal
o "What do you think Rookie?"

menu(screen ='choice'):
    "Marnie is right":
        r "Maybe we should listen to Marnie."
        show sprocko unhappy
        show gelato normal
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
        o "So if we tally it all up...{w=0.25} Tie breaker goes to the Captain..."
        show otus happy at hop
        o "Looks it's decided! We're going!"
        show marnie unhappy
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
        show marnie shocked at sulk
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
o "Alright Rookie! You're on point."
stop music fadeout 1.75
scene bgblack2 with dissolveslow
play sound hylong volume 0.7
pause 2.6
play sound2 metaldoorclunk volume 1
pause 1.25

$roommanager.addeventstoroom(2,"introhub")
$roommanager.setuproominstant(2)
$roommanager.checkroomevents(2)

##### HUB #####

label introhub:
scene bgblack
show bgblack2:
    alpha .7
show bg_2hub_room behind bgblack2 with dissolveslow
play sound3 airlock volume 0.6
dd "As the salvagers disembark onto the mysterious station, a wave of dusty stale air washes over them."
hide bgblack2 with dissolveslow
show marnie normal behind bgblack2 with dissolve:
    zoomnorm
    ease 0.4 xalign 0.2
stop sound fadeout 0.5
stop sound2 fadeout 0.5
m "Oof! It's so dark, dank, and dusty in here."
stop sound3 fadeout 0.5
m "Looks like it's been abandoned for a long time..."
show marnie unhappy at sulk
m "I don't like this..."
show gelato happy behind marnie with dissolve:
    zoomnorm
    center
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0
show marnie normal:
    ease 0.2 xalign -0.1
g "What are you talking about? This is great!"
g "All of this is so humany! Isn't that right Rookie?"
r "I guess..."
show gelato at wiggle
g "Look at the stairs and the carpet, and the pocket dimension delivery system!"
show gelato normal at wiggle
g "Perfect for the Rookie Earthling!"

menu(screen ='choice'):
    "I've never been to Earth":
        r "I've never actually been to Earth..."
        show gelato shocked at hop
        g "Whoa really!?"
        r "I was born on one of the colonies far from Earth."
        g "{size=-06} Does that mean you're not an actual Earthling?{/size}"
    "I like being in space":
        r "I actually really like being in space."
        r "Exploring and seeing the galaxy has always been a dream of mine."
        show gelato happy at wiggle
        g "Oh yeah?"
        g "So does that mean you'll be with the crew long term?"
        g "{size=-06} Maybe you can teach me human stick ball...{/size}"

show marnie shocked
m "C’mon, Gelato, take this seriously."
show sprocko happy with dissolve :
    zoomnorm
    xalign -0.55
show marnie normal:
    ease 0.2 xalign 0.1
show gelato normal:
    ease 0.1 xalign 0.55
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0
s "Gahahaha! Look at this place! It's just teeming with... {w=0.25}{size=+06}THINGS!{/size}"
show marnie unhappy
m "Not you too..."
s "Marnie! What do you think? How much of this stuff do you think we can shove into the cargo hold?"
m "Really? I thought we were only after the power source..."
show sprocko unhappy
s "But the Clover...{w=0.25} It needs upgrades..."
show otus normal with dissolve:
    zoomnorm
    xalign 1.4
show sprocko normal at hop
show marnie normal at hop
show gelato normal at hop
o "Focus, people! We have a tight timetable remember?"
o "First things first, we need to get the power restored and then figure a way to that reactor core."
o "Scrapping anything else can wait."
show sprocko happy
s "Yes! I'll take a look around, I already have...{w=0.25} IDEAS!"
hide sprocko with dissolve
show gelato normal at wiggle
g "How fun!{w=0.25} I guess we should spread out!"
hide gelato with dissolve
m "For the record I still think this is a bad idea..."
hide marnie with dissolve
show otus unhappy:
    ease 0.4 xalign 0.5
o "{size=+06}Rookie!{/size}"
r "Ahh! Yes Captain?"
o "Why are you just standing there?"
o "Go and help the others. See what they need."
show otus normal at hop
o "Now get to it!"
r "Ahh! Yes sir!"
hide otus with dissolve
play music ambience volume 0.15
##### ROOM 2 HUB #####
$roommanager.returnfrominteraction(roommanager.currentroom)
##### ROOM 2 HUB #####


##### Powerup Event #####
label powerup_event:
show sprocko happy:
    zoomnorm
    ease 0.5 xalign -0.55
stop music fadeout 1.0
pause 1.0
play music floatingby volume 0.22
s "EVERYONE! Gather around please!"
show marnie normal behind sprocko with dissolve:
    zoomnorm
    xalign 0.1
show gelato normal behind marnie with dissolve:
    zoomnorm
    xalign 0.55
show otus normal with dissolve:
    zoomnorm
    xalign 1.4
m "Looks like you're running a cord from the station back to the ship."
show gelato at wiggle
g "Oh so that was the plan..."
s "Correct! Such a elegant solution is what you would call GENIUS!"
o "Good work Sprocko."
o "Once we get the station's power up we should have a much easier time getting to that core."
show sprocko normal at wiggle
s "OK! Let me adjust a few setting here..."
show sprocko happy at hop
stop music fadeout 1.5
s "POWER TRANSFER ACTIVATED!"
show bgblack2 with dissolve
play sound2 pop
$ power = True
pause 0.75
$roommanager.intertoggle(ai_rm2)
hide bgblack2 with dissolve
s "Gahahahahaha! I did it!"
show marnie happy at sway
m "I guess going here wasn't such a bad idea after all."
play sound shake volume 0.7
show gelato shocked
show marnie shocked
show sprocko shocked
show otus unhappy with vpunch
pause 1.5
play music spacedout volume 0.4
o "Whoa what was that?"
play sound shake volume 0.8
show sprocko unhappy with vpunch
pause 1.0
o "Sprocko?"
m "Please tell me the station didn't just shake."
show gelato at wiggle
g "It was probably just the wind."
r "I don't think there's wind up here..."
play sound2 outage volume 0.8
show bgblack with dissolve:
    alpha 0.4
show sprocko shocked at sulk
s "{size=-06}Uh oh...{/size}"
hide bgblack with disnowait
m "What was that?"
s "The Clover... It just lost power..."
show marnie unhappy at hop
m "The Clover lost power?! {size=+06}You have got to be kidding me!{/size}"
play sound shake volume 0.8
show otus with vpunch
pause 1.0
g "I think the station is starting to move on its own..."
qq "Actually the station only disabled its geostationary thrusters."
show gelato at wiggle
g "That's like the same thing isn't it?"
qq "Well no, it just means that the station's orbit is no longer stable. It is the gravity of the planet below that is making the station move."
o "Hold on! Who is speaking right now?"

show ai normal with dissolve:
    zoomnorm
    xalign 1.75
show otus:
    ease 0.2 xalign 1.15
show gelato shocked:
    ease 0.1 xalign 0.4
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0
show marnie shocked:
    ease 0.2 xalign -0.15
pause 0.05
show sprocko shocked:
    ease 0.2 xalign -1.1
    ease 0.1 yoffset 30
    ease 0.1 yoffset 0

ai "Hello. I am the Caretaker of this space station."
show sprocko unhappy:
    ease 0.9 xalign -0.75
show gelato at hop
g "Gah! Who is that?!"
show marnie at hop
m "Its some kind of creepy AI!"
ai "Once again, I am the Caretaker of this space station."
m "I thought this place was abandoned..."
ai "Abandoned? No it is clear that you ruffians have illegally boarded this station."
ai "Not only that but you have fooled around with the power systems and made a huge mess of things."
show ai unhappy
ai "It will take me half a cycle to clean all of this up!"
o "That's not what happened! We found the station like this... In fact we are well within our rights to salvage this whole place if we want to!"
show ai at wiggle
ai "B-Barbarians! The lot of you!"
show ai normal
ai "I am going to ask you all kindly, to leave."
show sprocko shocked at wiggle
s "But the Clover has been DRAINED of all it's power!"
s "We can't leave!"
ai "Is that so? Quite the predicament isn't it..."
play sound shake volume 0.8
show marnie unhappy with vpunch
pause 1.0
m "Umm, guys! There's that other problem with the station losing its orbit!"
m "You know what that means right?"
o "We're going to burn up and crash into the planet like a bunch of dumb pleffynoids?"
ai "Quite the predicament indeed..."
ai "Perhaps my master can help solve this problem..."
play sound2 beepon volume 0.8
show ai at shake
ai "..."
show ai at normalize
ai "Hmmmmm... He doesn't seem to be responding. How odd."
o "I doubt your master is still on this station..."
show ai happy
ai "Nonsense, he just put me into the charging station not even a milli cycle ago!"
show otus normal at wiggle
o "I think we're talking to an AI with a few screws loose here!"
show ai unhappy
ai "How rude."
show gelato normal at wiggle
g "Mr. Caretaker sir. Maybe you can help us get power back to our ship? We'll help you look for your master."
show ai normal
ai "I know where the master is. He is in the reactor core doing his research as always."
show otus happy
o "Fantastic all we have to do is hop on the elevator and go to the reactor. Why are we even wasting time on this stinking clankyfooter for?"
ai "I'm sorry but that area is off limits. Only the master is allowed there."
show otus unhappy
show gelato unhappy
show marnie shocked at sway
m "Can't you let us up?! It's an emergency!"
ai "Even if I could I would need the elevator codes..."
ai "And I can't seem to recall them... Maybe my memory circuit has been damaged..."
show sprocko unhappy
s "Talking to this THING,{w=0.25} is useless!"
play sound shake
show otus with vpunch
pause 1.0
ai "Well if you lot are all set, I need to do some tidying up before we all crash horribly and die."
hide ai with dissolve
pause 0.25
show sprocko:
    ease 0.5 xalign -0.55
show marnie unhappy:
    ease 1.0 xalign 0.1
show gelato:
    ease 0.75 xalign 0.55
show otus:
    ease 1.25 xalign 1.4
pause 0.25
m "This can't be happening..."
show gelato unhappy at sulk
g "I haven't even visited the Earth yet..."
show otus normal
o "We’ve been in sticky situations before, and we’ve always found a way out."
show marnie at hop
m "Only broken airlocks or collapsing structures, nothing as bad as this!"
o "Well, if you merge them all together, it’s kind of as big as this, right?"
show otus unhappy
show marnie shocked at wiggle
m "Captain we need a plan!"
g "We can only power the ship up with access to the reactor core."
m "And we need the AI to either recall the elevator codes or get them working on our own."
stop sound fadeout 0.5
menu(screen ='choice'):
    "We should repair the AI":
        r "We could search the rest of the station and maybe find parts to repair this Caretaker AI."
        r "Then we can convince it to let us up or something..."
        show otus normal at wiggle
    "We should find the codes":
        r "We could search the rest of the station for the elevator codes directly."
        r "Then we can hop on the elevator with or without that AI's permission."
        show otus normal at wiggle
o "That's not a terrible plan."
show sprocko normal
show gelato normal
show marnie normal at wiggle
m "We should have access to the rest of the station now that the power is back on."
show gelato at wiggle
g "The Rookie is right! We can't just sit here all day..."
o "It's decided."
o "We split up and search the station for whatever can help us."
o "The worse that can happen now is that we run out of time and..."
show sprocko unhappy at sulk
show marnie unhappy at sulk
show gelato unhappy at sulk
pause 0.75
show otus unhappy
o "Hey! Why are you all sulking?"
m "..."
s "..."
g "..."
m "Well I guess we have no other choice."
show marnie normal at sway
m "I don't want to say I told you so but..."
m "..."
hide marnie with dissolve
show sprocko unhappy at sulk
s "{size=-6}I am an embarrassment...{/size}"
s "How did I not know the Clover would be drained, leaving us all stranded?"
show sprocko shocked
s "I MUST redeem myself!"
hide sprocko with dissolve
show gelato normal at wiggle
g "Don't worry Captain we'll figure it out..."
show gelato unhappy
g "And if we don't..."
show gelato normal at hop
g "Then it has been an honor serving with you!"
hide gelato with dissolve
show otus unhappy:
    ease 0.4 xalign 0.5
o "{size=+06}Rookie!{/size}"
r "Ahh! Yes Captain?"
o "I know that things don't look too good..."
o "But..."
show otus happy at hop
stop music fadeout 1.0
o "This is what adventure is made of!"
o "I know we can make it out of here!"
o "Go and help the others! See what they need!"
show otus at hop
o "This is the perfect chance to prove yourself! Now get to it!"
r "Ahh! Yes sir!"
play music ambience volume 0.15
hide otus with dissolve
$crewstatus = 1
# $RM3_lab.locked = 0
# $RM4_con.locked = 0
# $RM5_bar.locked = 0
$roommanager.intertoggle_on(ai_rm2)
# $roommanager.intertoggle(sprocko_rm2)
# $roommanager.intertoggle(sprocko_rm3)
# $roommanager.intertoggle(marnie_rm2)
# $roommanager.intertoggle(marnie_rm4)
# $roommanager.intertoggle(gelato_rm2)
# $roommanager.intertoggle(gelato_rm5)
$roommanager.returnfrominteraction(roommanager.currentroom)


##### ROOM 3 LAB #####
label introlab_event:
##### ROOM 3 LAB #####




dd "END FOR NOW"

return
