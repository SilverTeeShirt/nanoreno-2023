######################### #### ###############################
######################### TALK ###############################
######################### #### ###############################

screen talk(items):
    style_prefix "choicetalk"
    frame:
        vbox:
            for i in items:
                textbutton i.caption action i.action
style choicetalk_frame is gui_frame
style choicetalk_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .75
    yalign .5
    spacing gui.choice_spacing
style choicetalk_button is default:
    properties gui.button_properties("choice_button")
style choicetalk_button_text is default:
    properties gui.button_text_properties("choice_button")



######################### ######### ####################
######################## Sprocko ########################
######################### ######### ####################
label sprockotalk:
    show sprocko normal with dissolve:
        zoomnorm
        left
    s "What's going on Rookie?"
    label sprockotalking:
    show sprocko normal
    menu(screen ='talk'):
        "Powering up the station" if crewstatus == 0:
            if stalk1 == False:
                $ stalk1 = True
                $ subjectfittings = True
                r "You said you had an idea about getting power to the station?"
                s "Well, it's OBVIOUS, isn't it?"
                menu(screen ='choice'):
                    "Yeah!":
                        r "Y-Yeah, of course it is!"
                        show sprocko happy at wiggle
                        s "GOOD! Glad that SOMEONE here is on the same wavelength as me!"
                        r "Totally."
                        s "..."
                        r "..."
                        show sprocko unhappy at sulk
                        s "So...?"
                        r "Oh, uh, I'll go and...?"
                        show sprocko shocked at hop
                        s "You don't know what you're doing, do you?!"
                        r "..."
                    "Not really":
                        r "Sorry I don't really follow."
                        show sprocko unhappy
                        s "I had high hopes for you Rookie."
                        s "But now you are..."
                        show sprocko shocked at hop
                        s "DISAPOINTING!"
                        r "S-Sorry..."
                show sprocko unhappy
                s "Listen ROOKIE! All we need to do is plug the Clover straight into this station's hub connector."
                r "How is our ship going to power this whole station?"
                show sprocko shocked at hop
                s "Do I have to explain EVERYTHING?!"
                show sprocko unhappy
                s "The station already has power. That much is obvious."
                s "But it's been thrown out of sync, hence all the... {size=-06}Spookiness.{/size}"
                show sprocko normal
                s "We connect the Clover. The power gets synchronized and {w=0.25}{nw}"
                show sprocko normal with vpunchnowait
                s "{cps=0}We connect the Clover. The power gets synchronized and {/cps}BOOM!"
                r "Ahh!"
                s "Well, not boom. That CLEARLY won't happen...{w=0.25} Probably..."
                show sprocko happy
                s "That should provide the station access to it's own power source again."
                r "Great! Let's start by doing that then!"
                s "Just find me the Expandable Power Fittings and we can!"
                r "Sure! Umm... Where are they again?"
                show sprocko unhappy
                s "What must it be like being trapped in a mind like that..."
                r "Hey!"
                show sprocko normal
                s "They'll be somewhere IN the Clover. Ask the others if you need help!"
                show sprocko happy
                s "Now let me get back to work! I have VERY important things to do!"
            elif stalk2 == True:
                jump powerup_event
            else:
                r "How do we power up the station again?"
                s "Just plug the ship STRIAGHT into this hub connector!"
                s "Find and connect the Expandable Power Fittings to both the ship and to the station!"
                r "Got it!"
            jump sprockotalking

        "Expandable Power Fittings" if crewstatus == 0 and subjectfittings == True:
            r "Where can I find the Expandable Power Fittings again?"
            show sprocko unhappy
            s "I told you to ASK around!"
            r "Sorry!"
            jump sprockotalking

        "The station" if crewstatus == 0:
            r "What do you think of this station?"
            show sprocko happy at wiggle
            s "This station is MARVELOUS!"
            show sprocko at wiggle
            s "This sector is MARVELOUS!"
            show sprocko normal
            s "I would like to study all of it."
            s "But as the Captain said, we should focus on getting to the reactor core."
            s "..."
            show sprocko happy at wiggle
            s "The reactor core must be MARVELOUS!"
            jump sprockotalking

        "Ideas" if crewstatus == 1 and stalk3 == False:
            $ stalk3 = True
            r "Have you actually tried to find anything to help us yet?"
            show s neutral
            s "What? Of course I have! I'm just... Cataloguing everything, first!"
            r "That sounds like you're touching everything to work out what it does."
            show s happy
            s "Yeah, but scientifically!"
            r "Hmm... How many have you done?"
            show s unhappy
            s "Well, five?"
            r "Five!? There's like hundreds in here!"
            show s shocked
            s "Well, it's a very involved process! First I have to find out what it does."
            s "Then I try to work out how it does it, and how I can do it better!"
            r "What!? We don't have time for all that, we're crashing!"
            show s shocked
            s "I'm fully aware we're crashing, which is why I have to be so careful!"
            s "If I can't save all of these, I need to make sure I take the most useful devices!"
            r "Grr, we won't have time for that! You should be helping the most out right now!"
            show s neutral
            s "Oh, and why's that?"
            menu(screen ='choice'):
                "Because this is your fault!":
                    r "Because if you hadn't connected our ship to the power source, we wouldn't be in this mess right now!"
                    show s shocked
                    s "Hey, that's not my fault! The odds of that happening were like, 30% tops!"
                    r "Wh- Wait, was there a way of doing it that was safer?"
                    show s neutral
                    s "Well, yeah, but it would have taken a lot longer!"
                    r "This is exactly what I mean! You put is in danger, and now you need to help us get out!"
                    r "Because let's be honest here, we can't do this without you. So please, focus and help us out!"
                    show s unhappy
                    s "..."
                "Because you're so smart!":
                    r "Because you're the smartest being I've ever met!"
                    show s shocked
                    r "Because I don't know how to use anything in here without breaking it!"
                    s "True, but..."
                    r "Because if anyone can help us escape a crashing space station, it's you!"
                    r "So please, please can you try to focus so we can all survive and get out of here!"
                    s "..."
            s "You're right. I need to focus on what can help us here and now."
            r "Thank you, Sprocko. I'm glad you finally-"
            s "After all, my arms can probably grab most of these tools if we need to run later..."
            r "Urgh... Just let me know if you need help with anything."
            jump sprockotalking

        "Escape pods" if escapepods == True:
            r "Hey Sprocko... About the escape pods..."
            show sprocko happy at wiggle
            s "Hehehehehe!"
            s "Escape pods? No no no! More like EXPLOSION PODS!"
            r "Explosion...{w=0.25} Pods?"
            s "I used them for an experiment and it was a great success!"
            show sprocko happy at wiggle
            s "You should have seen the COLORS!"
            show sprocko normal
            s "It was blue."
            r "..."
            jump sprockotalking

        "Coreworlds" if coreworlds == True:
            r "Hey Sprocko... coreworlds?"
            s "Don't know much."
            jump sprockotalking

        "Academy" if academy == True:
            r "Hey Sprocko, can you tell me about the Kobomba?"
            s "Sure!"
            jump sprockotalking

        "CHEAT AHEAD" if crewstatus == 0:
            r "How about some cheats?"
            $ stalk1 = True
            $ subjectfittings = True
            $ stalk2 = True
            jump powerup_event


        "Back":
            hide sprocko with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)



######################### ######### ####################
######################## Marnie ########################
######################### ######### ####################
label marnietalk:
    show marnie normal with dissolve:
        zoomnorm
        left
    m "Hey what's up?"
    label marnietalking:
    show marnie normal
    menu(screen ='talk'):
        "Powering up the station" if crewstatus == 0:
            r "Do you have any ideas on how to power up the station?"
            m "I overheard Sprocko talking about a power transfer."
            m "If that's the case then we might have to shut down some systems on the ship and reroute the power."
            m "Maybe just the ventilation system? That thing eats up a lot of energy..."
            jump marnietalking

        "Expandable Power Fittings" if crewstatus == 0 and subjectfittings == True:
            r "Hey Marnie do you know where can I find the Expandable Power Fittings?"
            m "Hmmmmm... I'm not sure. Gelato usually handles that kind of heavy equipment."
            m "I've seen him lug a whole rack of sprigle rods up a ladder before."
            m "It was impressive but..."
            show marnie unhappy at sulk
            m "Also pretty dangerous..."
            jump marnietalking

        "The station" if crewstatus == 0:
            r "What do you know about the station?"
            m "Looking through the registry it looks like it was created some fifty cycles ago."
            m "It's privately owned, so someone had credits to burn."
            m "And if what Sprocko is saying about the zeta waves..."
            show marnie happy at wiggle
            m "This really could turn our fortunes around!"
            show marnie normal
            m "But we shouldn't get our hopes up..."
            m "It could still just be a signal amplifier or some sort of trick like that."
            jump marnietalking

        "Purple idol" if idol == True:
            r "Hey what's up with that idol on the dashboard?"
            show marnie happy at sway
            m "Oh that? Hahaha!"
            m "Just a little something silly I picked up a while ago."
            m "It's supposed to represent an ancient space wurm that would guide travelers safely though space."
            m "They say it gives you good luck if you rub it's cute little head every once in a while!"
            jump marnietalking

        "Escape pods" if escapepods == True:
            r "Hey Marnie... What happened to the escape pods?"
            show marnie unhappy at sulk
            m "Unfortunately someone, {w=0.25}{size=-06}Sprocko.{/size} Doesn't think about the consequences of his actions."
            m "He decided it was a great place to test the explosives."
            m "I like him, honestly I do, but..."
            m "Working with Sprocko is...{w=0.25} Expensive..."
            r "That's not good..."
            jump marnietalking

        "Coreworlds" if coreworlds == True:
            r "Hey Marnie? What do you know about the coreworlds?"
            m "The coreworlds? The're the main worlds of the Galactic Government."
            m "Each of the planets that make up the core worlds are ."
            $galgov = True
            $mtalk1 = True
            jump marnietalking

        "Coreworlds" if crewstatus == 1 and if mtalk1 == True:
            r "Hey Marnie? coreworlds?"
            m "wish I could get my family to move there."
            $mtalk1 = True
            jump marnietalking

        "Back":
            hide marnie with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)



######################### ######### ####################
######################## Gelato ########################
######################### ######### ####################
label gelatotalk:
    show gelato normal with dissolve:
        zoomnorm
        left
    g "What's going on human Rookie?"
    label gelatotalking:
    show gelato normal
    menu(screen ='talk'):
        "Powering up the station" if crewstatus == 0:
            r "Any idea on how to power up the station?"
            g "I'm looking around and nothing comes to me."
            show gelato at wiggle
            g "If they only had a hand crank."
            r "Hand crank?"
            show gelato at wiggle
            g "Or one of those wheels you can walk forever in..."
            r "I'll just keep looking around."
            jump gelatotalking

        "Expandable Power Fittings" if crewstatus == 0 and subjectfittings == True:
            r "Do you know where I can find the Expandable Power Fittings?"
            if gtalk1 == False:
                $ gtalk1 = True
                show gelato unhappy
                g "Expandable Power Fittings... Expandable Power Fittings..."
                show gelato normal at wiggle
                g "Oh! They're in the lockers, with all the other equipment!"
                g "Here! Take these keys, it will help you open most of the lockers."
                show item_keyset with dissolve:
                    xalign 0.5
                    yalign 0.5
                item "Received \"Key Set\""
                hide item_keyset with dissolve
                $inventory.items.append(item_keyset)
                $renpy.block_rollback()
                r "What do you mean most of the lockers?"
                show gelato unhappy at sulk
                g "There may be a key missing..."
                show gelato normal at wiggle
                g "But I put it somewhere safe! Somewhere very safe and secure..."
                r "Did you lose it?"
                show gelato shocked at hop
                g "How did you guess?"
                r "Um..."
                show gelato happy at wiggle
                g "It must be somewhere safe..."
                g "Just keep looking around, I'm sure that you'll find it!"
            else:
                show gelato happy at wiggle
                g "That set of keys I gave should let you open the equipment lockers!"
                g "I last put the Expandable Power Fittings in there."
            jump gelatotalking

        "The station" if crewstatus == 0:
            r "What can you tell me about the station?"
            show gelato happy at wiggle
            g "Well It's a human station for sure!"
            g "If you look, everything is proportional to you guys. The stairs, the table, even the doors."
            show gelato at wiggle
            g "But mainly it's the air!"
            r "The air?"
            show gelato normal
            g "Yeah its the perfect mixture of seventy eight percent nitrogen, twenty one percent oxygen, and other trace gases."
            show gelato happy at wiggle
            g "A perfect replica of Earth air and ideal for humans!"
            r "Wow! How can you tell?"
            show gelato normal
            g "We Troaderlites are very sensitive to air quality since we can breath through our skin."
            show gelato happy at wiggle
            g "Knowing what the air is made of is second nature to us!"
            $troaderlite = True
            jump gelatotalking

        "Troaderlites" if crewstatus == 0 and troaderlite == True:
            r "What else can you tell me about Troaderlites?"
            show gelato happy at wiggle
            g "We're great swimmers and we're always breathing through our skin!"
            g "When at rest we don't even need to use our lungs!"
            show gelato unhappy at sulk
            g "But besides that..."
            g "Well... You know we aren't the most liked species in the galaxy..."
            show gelato at sulk
            g "Because of that war and everything..."
            g "It's tough sometimes but I try to manage."
            show gelato happy at wiggle
            g "I'm just so thankful Captain Otus took me onto his crew!"
            show gelato unhappy
            g "Sorry... I didn't really answer your question..."
            $ greatgalacticwar = True
            jump gelatotalking

        "Ideas" if crewstatus == 1 and gtalk3 == False:
            $gtalk3 = True
            r "So, what are you doing here?"
            show gelato shocked
            g "...Investigating?"
            show gelato happy
            r "You don't sound too sure about that."
            g "To be honest with you, Rookie, I'm spending a lot of energy on not freaking out right now!"
            show gelato unhappy
            g "Mostly just trying not to think about how I could die here so I can keep on helping!"
            r "Oh yeah, that makes sense..."
            g "What about you? Have you been in a life and death situation?"
            "Yes"
            r "Yeah, this isn't the first time my life has been on the line."
            r "I'd rather not talk about it though..."
            g "Oh, yeah, that's fair. Uh, sorry for bringing it up..."
            r "I get it, though. The fear... It's a lot, it can mess you up."
            r "But I was needed, and we need everyone right now."
            g "Hah, no one needs me. I'm just some goof who makes jokes..."
            r "We need that right now. We need someone to lift our spirits."
            g "..."
            "No"
            r "No, I can honestly say this is the first time I've ever been in a situation like this."
            show gelato shocked
            g "What? Then how are you so calm then?"
            menu(screen ='choice'):
                "Because I've got a job to do":
                    r "I've got a job to do, helping out the crew to make sure the ship doesn't crash!"
                    r "You've got that job as well, Gelato! We all need to work together right now!"
                "I guess it hasn't hit me yet":
                    r "To be honest, I guess it hasn't hit me yet."
                    r "I guess my brain is just sort of focusing on how to get us out of this situation."
                    r "Once all this is over, I'm probably going to collapse into a mess and have a panic attack or something."
                    r "But the point is, I'm going to make it to that point. We're going to make it to that point. Together."
                "I don't know":
                    r "I... I don't know. I just keep on pushing through, I guess?"
                    g "Huh. Maybe it's a human thing. My mum was the same way."
                    r "Maybe. What would she do right now?"
                    g "She... She would say that we can survive, but only if we all work together."
                    r "Maybe you should focus on listening to her?"
            show gelato happy
            g "Yeah... Yeah, you're right, Rookie! Thanks for the pep talk!"
            g "Right, I'm going to keep on investigating! You see what else you can find here!"
            g "Maybe you'll recognize one of these weird human things?"
            jump gelatotalking


        "The logo" if logo == True and crewstatus == 0:
            r "Gelato you ever seen a logo like that?"
            show gelato happy at wiggle
            g "Oh yeah!"
            show gelato at wiggle
            g "That's the Yummo Grabbo That Candy Corp logo!"
            show gelato normal at wiggle
            g "Although the orb looking part should be more candy like..."
            g "And the hand looking parts should be tentaclelier..."
            show gelato happy at wiggle
            g "It must be an older design!"
            jump gelatotalking

        "Back":
            hide gelato with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)



######################### ######### ####################
######################## Otus ########################
######################### ######### ####################
label otustalk:
    show otus normal with dissolve:
        zoomnorm
        left
    o "Huh? What is it?"
    label otustalking:
    show otus normal
    menu(screen ='talk'):
        "Powering up the station" if crewstatus == 0:
            r "Captain Otus, how do you think we should power up the station?"
            o "Hmmmmm... Sprocko usually has some pretty good ideas."
            o "Marnie is also pretty good at making sure Sprocko's Ideas don't kill us."
            o "See if one of them can come up with something."
            jump otustalking

        "Expandable Power Fittings" if crewstatus == 0 and subjectfittings == True:
            r "Do you know where I can find the Expandable Power Fittings?"
            o "I would ask Gelato, he's in charge of organizing the tools and heavy equipment."
            r "So you don't know where it is?"
            show otus unhappy
            o "Listen Rookie. It's Gelato's job to know and my job to know that he knows!"
            show otus happy
            o "That guy is a pro. And as a pro he knows where everything on that ship is."
            show otus normal at wiggle
            o "Well, nearly everything..."
            jump otustalking

        "The station" if crewstatus == 0:
            r "Hey Captain, what do you think about this station?"
            o "From the outside it looks like any typical high class private space station."
            o "But why is a fancy station like this out in the middle of nowhere?"
            o "This sector is mainly known for prospecting and not much else."
            o "And the fact that it is leaking an absurd of amount of zeta waves?"
            o "Strange right?"
            r "You seem to be having a good time."
            show otus happy at hop
            o "What can I say? I love me a good adventure!"
            jump otustalking

        "Plan" if crewstatus == 1:
            r "Hey Captain, what do you think of the plan?"
            o "So we either find spare parts to this AI Caretaker and fix it up."
            o "Or we find the elevator codes and get ourselves to the reactor core."
            o "After that, it should be easy to send power to ship and get out of here before this station crashes."
            o "Doesn't seem so hard right?"
            jump otustalking

        "The Caretaker" if crewstatus == 1:
            r "What's with the Caretaker anyways?"
            o "Well it's memory seems to be messed up."
            o "It also doesn't respond to question properly."
            o "Fixing it up could provide some actual answers."
            o "It's a sentient AI but there's something off about it..."
            show otus happy at hop
            o "Don't worry though I'll keep an eye on it!"
            jump otustalking

        "The logo" if logo == True:
            r "Hey Captain, have you seen that logo before?"
            o "That logo?"
            o "I think I have..."
            o "Some sort of Earth foundation I believe..."
            show otus unhappy
            o "Maybe its THAT foundation who runs this place."
            o "But..."
            show otus happy at wiggle
            o "Nah! It can't be!"
            jump otustalking

        "Back":
            hide otus with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)



######################### ######### ####################
######################## AI ########################
######################### ######### ####################
label aitalk:
    show ai normal with dissolve:
        zoomnorm
        left
    ai "Hello, what is it that you want?"
    label aitalking:
    show ai normal
    menu(screen ='talk'):
        # "The station" if crewstatus == 1:
        #     r "Hey Caretaker, what can you tell me about this station."
        #     jump aitalking

        "End of the game!" if crewstatus == 1:
            ai "Sorry but this is the end of the game!"
            ai "We will work hard to finish it up but one month just wasn't enough."
            ai "I apologize and hope you look forward to it!"
            ai "Feel free to explore a bit and let us know what you think."
            ai "Thank you for playing!"
            jump aitalking

        "The logo" if logo == True:
            r "Do you have any idea what that logo is?"
            ai "Well it is quite obviously the Z{nw}"
            show ai at shake
            ai "{cps=0}Well it is quite obviously the Z{/cps}---zttztzt...."
            ai "The Z-zztzttztttzt...."
            play sound beepon
            show ai unhappy at normalize
            ai "How odd. I can't seem to say that word..."
            show ai normal
            ai "It is a famous foundation. Surely you are just being forgetful."
            jump aitalking
        "Back":
            hide ai with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)









######################### ######### ####################
######################## TEST MENU ########################
######################### ######### ####################
label sprockotalkTESTINGONLY:
    show sprocko normal with dissolve:
        zoomnorm
        left
    s "What's going on Rookie?"
    label sprockotalkingTEST:
        menu(screen ='talk'):
            "BELOW IS TESTING":
                r "Can I get advice?"
                s "Go away!"
                $roommanager.returnfrominteraction(roommanager.currentroom)
            "Toggle water":
                r "Can togglewater?"
                s "sure thing Rookie."
                hide sprocko with dissolve
                if water_on == False:
                    $ water_on = True
                else:
                    $ water_on = False
                $roommanager.returnfrominteraction(roommanager.currentroom)
            "Toggle bird":
                r "Can  u toggle?"
                m "Sure..."
                hide marnie with dissolve
                if conbird_off == False:
                    $ conbird_off = True
                else:
                    $ conbird_off = False
                $roommanager.returnfrominteraction(roommanager.currentroom)
            "Toggle vines":
                r "Can u vines??"
                m "Sure..."
                hide marnie with dissolve
                if convine_off == False:
                    $ convine_off = True
                else:
                    $ convine_off = False
                $roommanager.returnfrominteraction(roommanager.currentroom)
            "Be evil or weird":
                r "Can you be weird now?"
                ai "Sorry but you must leave."
                show ai happye at hop
                aie "OR DONT!"
                show ai normal at wiggle
                ai "Sorry I don't know whats going on."
                show ai unhappye at hop
                aie "GAHHHHHH!"
                show ai unhappy at wiggle
                ai "Sometimes I get like this..."
                jump aitalking
            "Back":
                hide sprocko with dissolve
                $roommanager.returnfrominteraction(roommanager.currentroom)
######################### ######### ####################
######################## TEST MENU ########################
######################### ######### ####################
