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

show bg_0cold_room
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
        m "I can never tell how long you humans take in there!"
        show marnie normal
        m "How are you feeling?"
        r "A little woozy. It felt like my heart was pounding in the back of my skull..."
        m "That's to be expected. Emergency thaws are kind of rough..."
    "Where am I?":
        label start_whereami:
        hide bgblack with dissolve
        r "W-Where am I?"
        show marnie shocked at sulk
        m "Seriously? Don't tell me the Cold Sleep messed with your memory..."
        m "I thought they fixed that issue..."
        show marnie normal
        m "Well what do you remember?"
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
            "I don't know":
                r "Oh no!{w=0.25} {size=+06}I don't know anything!!!{/size}"
                m "..."
                r "..."
                m "..."
                show marnie with vpunchnowait
                play sound smack volume 0.6
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
                play sound smack volume 0.6
                r "{size=+06}OW!{/size}"
                show marnie shocked at hop
                m "Stop messing around!"
                r "Sorry! I'm awake now!"
                m "Don't scare me like that!"
                show marnie normal
                m "You should know better..."
show marnie normal
m "Anyways the Captain wants everyone on the bridge."
m "Just freshen up and meet everyone there."
r "Yes Marnie."
hide marnie with dissolve

##### this sets up the event when you enter room number, needs name of label as string
$roommanager.addeventstoroom(1,"introbridge")
#####

dd "As you climb out of the Cold Sleep pod, you slowly glance around the room in an attempt to regain your bearings."


##### ROOM 0 COLD SLEEP #####
$roommanager.setuproom(0)
##### ROOM 0 COLD SLEEP #####

##### BRIDGE #####
label introbridge:
scene bg_1bridge_room with fade

show marnie normal with dissolve:
    zoomnorm
    leftish
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
    g "Smells like a perfectly normal human to me!"
if shower == True:
    r "Yup. That's me. The human salvager..."
else:
    r "Yup. That's me. The smelly human salvager..."
show gelato happy at wiggle
if shower == True:
    g "Yeah! You're {size=+06}THE HUMAN{/size} salvager!"
    show gelato at wiggle
    g "The one and only!"
    show gelato at wiggle
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
m "{size=-06}I was the first one here...{/size}"
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
#play sound blip and boops

dd "With a simple click, the main screen turns on and a large orbital station comes into view."

#play sound engines
show cg01 with dissolve
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
hide cg01 with dissolve

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
o "Rookie, you're on point."
show bgblack2 with dissolve
#play sound landing connecting

##### HUB #####

#play sound airlock opening door
scene bg_2hub_room with fadeslow
dd "As the salvagers disembark onto the mysterious station, a wave of dusty stale air washes over them."
show marnie normal with dissolve:
    zoomnorm
    ease 0.4 xalign 0.2
m "Oof! It's so dank, dark, and dusty in here."
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
g "Look the stairs and the carpet, and the pocket dimension delivery system!"
show gelato normal at wiggle
g "Perfect for the homesick Earthling!"

menu(screen ='choice'):
    "I've never been to earth":
        r "I've never actually been to Earth..."
        show gelato shocked at hop
        g "Whoa really!?"
        r "I was born pretty far from Earth on one of the colonies."
        g "{size=-06} Does that mean you're not an actual Earthling?{/size}"
    "I like being in space":
        r "I actually really like being in space."
        r "Exploring and seeing the galaxy has always been a dream of mine."
        show gelato happy at wiggle
        g "Oh yeah?"
        g "So does that mean you'll be with the crew long term?"
        g "{size=-06} Maybe you can teach me human stick hit ball...{/size}"

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
s "But the Clover... It needs upgrades."
show otus normal with dissolve:
    zoomnorm
    xalign 1.4
show sprocko normal at hop
show marnie normal at hop
show gelato normal at hop
o "Focus, people! We have a tight timetable remember?"
o "First things first, we need to get the power restored and then figure a way to that reactor core."
o "Scrapping anything else can wait."
o "Now get to it!"

# hide sprocko
# hide marnie
# hide gelato
# hide otus

##### ROOM 2 HUB #####
$roommanager.setuproom(2)
##### ROOM 2 HUB #####

# dd "Next area is a test, look at window to continue"
# ##### ROOM 1 BRIDGE #####
# $roommanager.setuproom(1) #testing for now
# ##### ROOM 1 BRIDGE #####

dd "after they connect the Clover to the Station they power up the Station."

dd "DRAFT INCOMING."

# m "So we’re just going to… Slice this metal man open then?"
# s "That’s the plan! Just let me finish getting it working…"
# m "It just seems that, y’know, breaking into-"
# g "Woah, woah, who said anything about breaking into? We’re just cutting into, get me?"
# g "Hey Newbie, who are those guys your people have with the small knives who save lives?"
# r "...Surgeons?"
# g "Yeah, that’s the one! Would you say they ‘break into’ people bodies to fix them?"
# r "No, because that would be a really weird thing to-"
# g "Exactly, __Grouch, it would be weird to say."


m "Point is, a place all sealed up like this, with no clear cause why it’s empty…"
m "Just seems like a bad idea, is all."
o "__Grouch, usually I’d agree with you, but the potential…"
o "This is the sort of opportunity you only get once in a lifetime!"
m "Fine, but if this all goes horribly wrong and we all die, I get bragging rights."
g "Aw cool your jets, __Grouch! What could possibly go wrong?"
"And then everything went wrong."
s "I’ve managed to slice through the door!"
o "Okay! Everyone head in!"

# Change background to hub

r "Woah…"
g "Wow, this is some fancy, badass human stuff!"
o "Oh, we are absolutely taking everything that isn’t nailed down here."
m "Huh, maybe this isn’t such a bad ide-"

# strange notification sound

o "What was that sound?"
s "!"
o "__Tech? What is it?"

s "I just got a bill?"
qq "Yes. For the door."
s "What? Who said that?"
m "I knew this was going to go badly…"

show ai normal with dissolve:
    zoomnorm
    xalign 1.75
show otus:
    ease 0.2 xalign 1.15
show gelato:
    ease 0.1 xalign 0.4
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0
show marnie:
    ease 0.2 xalign -0.15
pause 0.05
show sprocko:
    ease 0.2 xalign -1.1
    ease 0.1 yoffset 30
    ease 0.1 yoffset 0

ai "Hello. This is my space station. Please leave."
show sprocko unhappy:
    ease 0.9 xalign -0.75
g "Gah! What the hell was that!"
ai "That doesn’t matter. Please leave."
o "Who the pleft do you think you are?"
ai "I am the owner of this space station. I have asked you once to leave. Please do so."
m "Or what, tin can?"
s "Oh, it is much more than that, __Grouch… It’s beautiful!"
g "__Tech! Don’t compliment things that threaten us!"
s "I wouldn’t say it’s threatening us-"
ai "If you do not leave, I will be forced to take drastic measures…"
r "Drastic measures?"
o "What kind of drastic measures?"
ai "Keeping you in the dark will help you make the right decision and leave."
s "It’s bluffing."
o "__Tech, you sure?"
s "No doubts. My scanner says no weapon signatures, no explosives and no personal on board."
s "At least, nothing automated."
o "Right, you heard __Tech, crew. The worst that can happen is that we can get annoyed to death."
ai "..."
r "Looks like you’re righ-"

show bgblack with dissolveslow:
    alpha 0.5
dd "Lights dim"

m "What the pleft was that?"
s "Uh oh…"
o "Tech, what’s going on?"
s "The Clover, it’s… It’s dead!"
o "What?"
s "I mean, the generator! It’s dead, it’s been drained of all power!"
g "I- That’s got to be a coincidence or something, right? I mean, what could drain the power that quickly?"
ai "No coincidence. Merely a show of power. Heh, power…"
m "What?!"
ai "Uh, just a pun. Power being a word that means both energy and strength. I found it funny."
s "You found it funny?"
g "Yeah, that was an awful joke."
g "That was like a, Great Grandad joke, eh Rookie?"
r "What?"
s "That’s not the point, __Goof. Hey, uh… Sorry, what do I call you?"
ai "..."
o "What are you angling at here, __Tech?"
s "Just… Let me try something. So, your name?"
ai "You may call me… Zates."
g "Zates? Why does that name sound familiar…"
s "__Goof, you’re missing the point! It has a name, a sense of humour."

#ai looks nervous

s "I think we’re talking to a Sentient level AI here!"

#Everyone looks shocked

m "For real, __Tech?"
s "Yeah! And if th- person is meeting us at the door, then-"
o "What’s being kept inside must be worth all the gredits in the universe…"
ai "What?"
m "Cap, I know I had my doubts about this, but if that’s the case, we need to clear this place out!"
ai "Hold on, what?"
o "Agreed. I think this place is worth paying a fine for a late delivery!"
g "Hell, we should just trash the stuff in the hold and take as much from this place!"
ai "Take as much… Are you serious?"
r "Um, guys…"
m "I agree, the salvage from here is worth much more than our current contract…"
s "I really want to get my PTK on the data centre for this guy! Or the engine! Or pretty much anything in here!"
ai "If you dare lay a single metal finger -"
r "Guys?"
g "This place is giving massive human vibes, I wonder…"
o "Hey __Tech, can you power up the Rusty Clover with enough time?"
s "You kidding me? All I need to do is find the engine room and find a spare Zetacite cell."
ai "The engi- No. No more."
r "Guys!"

# Alarms start sounding

m "What the chirt was that?"
o "Everyone stay calm-"
ai "I gave you plenty of chances. You could have left at any point!"
s "Uh-oh…"

#screen shake

g "Woah, did you guys feel that?"
s "Yeah, that was the geostationary engines turning off."
o "Oh brip."
s "Yeah. The station is falling out of orbit and is going to…"
ai "Crash. Horribly. Killing all of you."
g "What the hell, you psychopath! You’re going to kill us all, including yourself!"
ai "Better that then allow you squiglybeaks to strip this station down!"
ai "Now, if you allow yourselves to die quietly to die with dignity, I must go."
r "Woah, where the hell are you going?"
ai "Shh! Like I said, please die quietly."

hide ai with dissolve

r "Oh my god, we’re going to die!"
m "I knew this was a stupid risk!"
g "We’re going to die, and I’ve never even been to Earth!"
s "I… I…"
o "Everyone, shut up!"
o "We’ve been in sticky situations before, and we’ve always found a way out."
m "Only broken airlocks or collapsing structures, nothing as bad as this!"
o "Well, if you merge them all together, it’s kind of as big as this, right?"
o "Anyway, not the point. That software-head expects us to sit back and die?"
o "__Tech,you mentioned a zetacite cell in the engine room?"
s "Oh! Uh, through those doors at the end of the room!"
o "Then we just need to bust open the doors and make our way to that engine room!"
m "Either we find a way to stop the ship from crashing or grab a cell, clever…"
s "Uh, one problem. Those doors are made up of Diamondic Titanium."
g "Wow, that’s like 10 magnitudes harder than diamond!"
o "Doesn’t matter. Everyone split up, and see if you can find a way through these doors."
r "How?"
o "Try anything. Hacking them, blowing them up, finding some fancy technology here, anything!"
s "Maybe I can find something in that lab…"

hide sprocko with dissolve

g "Hey, there’s a camera up there, right? I want to try something out!"

hide gelato with dissolve

m "Explosives, huh? That gives me an idea, let me see what I can find."

hide marnie with dissolve
show otus:
    ease 0.4 xalign 0.5

o "Rookie!"
r "Ah! Yeah?"
o "Figure out what the others need and help them."
o "I’m going to explore this area and see what I can find. I may have an idea..."

# START ROOM
############## FIRST DRAFT ##############

dd "Next area is a test, look at window to continue"
##### ROOM 1 BRIDGE #####
$roommanager.setuproom(1) #testing for now
##### ROOM 1 BRIDGE #####



dd "END FOR NOW"

return
