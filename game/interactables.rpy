###### Interactables

###### ###################### ######
###### rm_0 cold sleep locker ######
###### ###################### ######

label showerlook:
    dd "A narrow sonic shower sits uncomfortably in the corner the room."
    if shower == True:
        $roommanager.returnfrominteraction(roommanager.currentroom)
    if power == True:
        dd "No power means no shower. You'll have to stay a bit stinky."
        $roommanager.returnfrominteraction(roommanager.currentroom)
    else:
        menu(screen ='choice'):
            "Take a shower" if shower == False:
                dd "You hop in the shower and turn the dial."
                play sound sonicshower
                dd "A wave of ultra sonic pulses hits you all over."
                dd "Although clean you don't feel very refreshed."
                $ shower = True
                $roommanager.returnfrominteraction(roommanager.currentroom)
            "Back" if shower == False:
                $roommanager.returnfrominteraction(roommanager.currentroom)
label gloveslook:
    dd "Two pairs of work gloves dangle off the ship's internal super structure."
    dd "They are covered in a thick layer of dust and grime."
    dd "You are unsure who they belong to as no member of the crew would be able fit into the claw like design."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label mirrorlook:
    dd "This cleaning station contains a sonic pulse gun and other similar cleaning devices."
    dd "Useful for when you need to clean off gear or those more delicate parts of your body."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label shoe1look:
    dd "An oversized work boot sits awkwardly against the wall."
    if (rm0_shoe.interprogress == 0):
        dd "You peer inside the giant boot and notice something at the bottom."
        show item_key1 with dissolve:
            xalign 0.5
            yalign 0.5
        item "Received \"Boot Key\""
        hide item_key1 with dissolve
        $inventory.items.append(rm0_lockerkey)
        $renpy.block_rollback()
        $rm0_shoe.interprogress = 1
    else:
        dd "You wonder who it belongs to."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label locker1look:
    dd "These lockers are mainly used to store equipment and sometimes personal items."
    dd "This set of lockers have a dimond and circle symbol on them."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label locker2look:
    dd "These lockers are mainly used to store equipment and sometimes personal items."
    dd "This set of lockers have a square and triangle symbol on them."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label gastanklook:
    dd "The Cold Sleep pods use a mixture of volatiles and chemicals along with a weak pulse of electricity."
    dd "The tanks holding the chemicals have seen better cycles."
    dd "A white gooey chemical is slowly seeping out of one of the tanks."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_wireslook:
    dd "There are exposed wires hanging dangerously all over the room."
    dd "It's best not to touch them."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_windowlook:
    if coldwindow_on == False:
        dd "You stare deeply into the inky blackness of space."
        dd "A cold shiver runs down your spine as you contemplate the unimaginable vastness of the universe."
    else:
        dd "The window shade blocks the view into space."
        dd "Useful when trying to fall into the deep chill of Cold Sleep."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_wbuttonlook:
    dd "You press the window shade button."
    if power == False:
        play sound fastsys
        show bgwhite with vpunchnowait:
            alpha 0.0
        if coldwindow_on == False:
            $ coldwindow_on = True
            dd "The window shade shoots down in a flash."
        else:
            $ coldwindow_on = False
            dd "The window shade shoots up with a snap."
        $roommanager.returnfrominteraction(roommanager.currentroom)
    else:
        dd "Without the main power systems on, the button does nothing."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_noteslook:
    dd "The note says \"Do not use! Out of Order!\" written in Galactic Script."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_terminallook:
    if power == False:
        dd "The computer terminal flickers with a dull green light."
        # Add computer terminal stuff. Maybe cold sleep log, and info and lore about it.
        label rm0_terminallook1:
        menu(screen ='ctalk'):
            "Pod Status":
                menu(screen ='ctalk'):
                    "Pod 1":
                        c "Status: Release. Settings: Human. Power: Recharging 49\%"
                        c "Note: Emergency release activated."
                        jump rm0_terminallook1
                    "Pod 2":
                        c "Status: Release. Settings: Felle'tian. Power: Recharging 78\%"
                        jump rm0_terminallook1
                    "Pod 3":
                        c "Status: Ready. Settings: None. Power: Fully Charged"
                        jump rm0_terminallook1
                    "Pod 4":
                        c "Status: Critical Failure. Settings: Human. Power: Overloaded."
                        c "Note: Chemical mixture system offline. Pod lock disengaged. Maintenance cycle past due."
                        jump rm0_terminallook1
            "Data Log":
                c "If anyone is experiencing any symptoms of Starsickness please use an available Cold Sleep pod within the milli cycle. -M"
                c "Do not store Beverages in the Cold Sleep pods! Please use the Lockers for personal items! -M"
                c "Make sure to put the Rookie in pod 4. That one is already set for humans. They don't handle the Star Paths very well and can get some serious Starsickness. -CO"
                c "DO NOT PUT THE ROOKIE IN POD 4!!! -M"
                jump rm0_terminallook1
            "Back":
                $roommanager.returnfrominteraction(roommanager.currentroom)
    else:
        dd "There is no use in trying to activate this computer."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label sleeppodlook:
    dd "Cold Sleep pods are an older technology still in use today."
    dd "These pods in particular look very old."
    dd "You often get a bit nervous when climbing into one of these."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label scrathesslook:
    dd "This Cold Sleep pod is pretty banged up."
    dd "There are heavy scratches and marks all over the inside of this pod."
    $roommanager.returnfrominteraction(roommanager.currentroom)



###### ########### ######
###### rm_1 bridge ######
###### ########### ######

label mainwindowlook:
    dd "You take a look out the main window."
    show CG1docked with dissolve
    dd "The ship is docked to the station and you have a nice view of the planet below."
    dd "The large green planet doesn't seem to hold any life. Just large swirls of noxious gas and planet wide storms."
    dd "Looking ahead you can see the edges of the Milkyway Galaxy. This sector also has a nice view of the Pepperoni Constellation."
    dd "Can you see it? It looks like a slice of pizza."
    hide CG1docked with dissolve
    $roommanager.returnfrominteraction(roommanager.currentroom)
label radtoplook:
    dd "This radiator helps circulate the air."

    $roommanager.returnfrominteraction(roommanager.currentroom)
label radbotlook:
    dd "Hot or cool air is pumped out of this unit."
    dd "It's a bit tricky to maintain a comfortable temperature for the diverse crew."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label navseatlook:
    dd "Navigator seat."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label capchairlook:
    dd "small chair for Captain Otus. It even has a small cup holder."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label capscreenlook:
    dd "captain's screen."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label idollook:
    dd "small idol, might be lucky travels through space or the world destroyer."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm1_readoutlook:
    dd "data on area."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm1_mainscreenlook:
    dd "main screen visualizer, displays images on the window."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm1_ventslook:
    dd "vents are dusty and crooked."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm1_vbuttonlook:
    dd "does stuff with vents maybe for puzzle."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm1_wireslook:
    dd "exposed wires being used to hold up more wires and tubes. Doesn't look safe."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm1_datafoodlook:
    dd "A display of the ship's status. It is blinking and looks worrying."
    dd "Also there's a nutrition dispenser here... Dunno why its connected to the data screen."
    $roommanager.returnfrominteraction(roommanager.currentroom)



###### ######## ######
###### rm_2 hub ######
###### ######## ######

label skyartlook:
    dd "art."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm2_trashlook:
    dd "trash messy."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm2_tablelook:
    dd "table dead plants long time."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label chargerlook:
    dd "some kind of charger."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm2_doorlook:
    dd "locked then not locked."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label logolook:
    dd "logo looks like hand catching something."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm2_elevatorlook:
    dd "lotsa text and stuff here about elevator."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm2_lightlook:
    dd "weird lights. feels like they are watching you when on."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm2_bigdoorlook:
    dd "big security storage area. need biometric data to open."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label planetmodellook:
    dd "looks familiar if sprocko in room."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm2_powermaillook:
    dd "DA MAIL power connect to this."
    $roommanager.returnfrominteraction(roommanager.currentroom)



###### ######## ######
###### rm_3 lab ######
###### ######## ######

label rm3_ceilinglook:
    dd "tubes and stuff must connect to other rooms."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm3_windowlook:
    dd "window."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label partsheadlook:
    dd "head of servobot old."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label partsarmlook:
    dd "arm of servobot or something."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label raydishlook:
    dd "galvanizing ray. great but old technology."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label constructorlook:
    dd "very fancy constructor to create and repair machinery."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label fluidtankslook:
    dd "fluids are building up in tank, empty then fill later."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label biodevicelook:
    dd "simple bio encoder device. maybe useful for puzzle."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm3_datapadlook:
    dd "download data to read later. About Sebastain."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm3_safelook:
    dd "need code to open."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm3_computerlook:
    dd "computer with data you can read about station and the puzzle hints."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label chembanklook:
    dd "filled with chem or not. player must add chem ingredients."
    $roommanager.returnfrominteraction(roommanager.currentroom)



###### ################# ######
###### rm_4 conservatory ######
###### ################# ######

label hangingplantslook:
    dd "hanging plants."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label gardenlook:
    dd "garden."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label scarecrowlook:
    dd "scarecrow, looks like old servobot."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label watertanklook:
    dd "water is pumped and stored here."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm4_stairlook:
    dd "stair a bit rusty."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm4_panelslook:
    dd "big panels for helping plants grow."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label pumpdoorlook:
    dd "door is blocked by vines."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label pumpslook:
    dd "pumps water."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm4_lightlook:
    dd "Even with the power back on some things are just too damaged to reactivate."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label forestlook:
    dd "dense forest."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label colorfulflowerlook:
    dd "colorful plant can use pollen."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label birdlook:
    dd "thats a squiggleybeak. very dangerous defeat with chocolate."
    $roommanager.returnfrominteraction(roommanager.currentroom)


###### ######## ######
###### rm_5 bar ######
###### ######## ######

label boothlook:
    dd "nice looking booth soft velvety material."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label plantmonsterlook:
    dd "big taxidermy plant monster."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label paintingslook:
    dd "exprssionistic painting from a bygone era."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label eyetreelook:
    dd "creepy ocular tree."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label mooselook:
    dd "Moose, gelato says it must be a famout earth monster devours humans."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label harpoonlook:
    dd "deadly harpoon used in space hunts back in the day."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label bonemonsterlook:
    dd "big bone monster. This one is called a Gigamaw Wurm."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label bugheadlook:
    dd "Zirikkacamantis deadly and dangerous."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm5_tubeslook:
    dd "pumps and tube connected to the rest of the station. They power the beverage devices in the bar."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label drinkmakerlook:
    dd "make Bieere need pump activated for that."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label drinkslook:
    dd "Various glasses and containers for beverages. Get a beverage holder here to hold chemicals later."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm5_datapadlook:
    dd "download data to read later. About Sebastain and clues."
    $roommanager.returnfrominteraction(roommanager.currentroom)



###### ######## ######
###### rm_6 core ######
###### ######## ######

label mementolook:
    dd "Sebastian's sentimental things."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm6_doorlook:
    dd "Big honking door."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label jarlook:
    dd "odd device. seems to be for biological recovery. low power draining from it."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label jarmanlook:
    dd "Cloudy cant see inside yet, then opens to reveal the founder."
####TESTING
####TESTING
####TESTING
    menu(screen ='choice'):
        "ENDING?":
            show bgblack with fade
            scene bgblack2
            $ corejarman_on = True
            show spacemoving
            show bg_6coreback
            show bg_6core_roomforeground
            show bgblack
            ai "Well..."
            hide bgblack with dissolve
            show ai normale with dissolve:
                zoomnorm
            aie "I will kill you all!"
            show ai happye at wiggle
            aie "GHAHAHAHAHAHA!"
            aie "MURDERRRR!"
            aie "OPEN ZAAAA DOOORRRSS"
            play sound zetaheart
            show ai with vpunchnowait
            show ai unhappye
            hide bg_6coreback with dissolve
            aie "..."
            aie "im sad now..."
            hide ai with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)
        "Back":
            $roommanager.returnfrominteraction(roommanager.currentroom)
####TESTING
####TESTING
####TESTING
label rm6_computerlook:
    dd "Computer core room."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label deadguylook:
    dd "Not sure who this sad sack is."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm6_rcorelook:
    play sound zetaheart
    dd "impressive giant Zeta reactorcore."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm6_pointslook:
    dd "devices pointing to reactor core."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm6_datapadlook:
    dd "download data to read later. About Sebastain and clues."
    $roommanager.returnfrominteraction(roommanager.currentroom)

######################### ####### ###############################
######################### Computer ###############################
######################### ####### ###############################

screen ctalk(items):
    style_prefix "computertalk"
    frame:
        vbox:
            for i in items:
                textbutton i.caption action i.action
style computertalk_frame is gui_frame
style computertalk_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
    spacing gui.choice_spacing
style computertalk_button is default:
    properties gui.button_properties("choice_button")
style computertalk_button_text is default:
    properties gui.button_text_properties("choice_button")



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



######################### ######### ###############################
######################## Characters ##############################
######################### ######### ###############################

######################## Marnie ########################
label marnietalk:
    show marnie normal with dissolve:
        zoomnorm
        left
    m "Hey what's up?"
    label marnietalking:
    menu(screen ='talk'):
        "Need help?":
            r "Do you need help?"
            m "No I'm all set."
            jump marnietalking
        "BELOW IS TESTING":
            r "Test?"
            m "Yup."
            jump marnietalking
        "Advice":
            r "Can I get advice?"
            m "Nah."
            jump marnietalking
        "Explore":
            r "Can you explore the other room?"
            m "Sure thing."
            hide marnie with dissolve
            $roommanager.intertoggle(marnie_rm2)
            $roommanager.intertoggle(marnie_rm4)
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
        "Back":
            hide marnie with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)



######################## Sprocko ########################
label sprockotalk:
    show sprocko normal with dissolve:
        zoomnorm
        left
    s "What's going on Rookie?"
    label sprockotalking:
    menu(screen ='talk'):
        "Power up station" if sstatus == 0:
            if stalk1 == False:
                $ stalk1 = True
                r "You said you had an idea about getting power to the station?"
                s "Well, it's OBVIOUS, isn't it?"
                menu(screen ='choice'):
                    "Yeah!":
                        r "Y-Yeah, of course it is!"
                        show sprocko happy at wiggle
                        s "GOOD! Glad that SOMEONE here is on the same wavelength as me!"
                        r "T-Totally"
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
                s "So, the station already has power. That much is obvious."
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
                s "Just find me the expandable power fittings and we can!"
                r "Sure! Umm... Where are they again?"
                show sprocko unhappy
                s "What must it be like being trapped in a mind like that..."
                r "Hey!"
                show sprocko normal
                s "They'll be somewhere IN the Clover. Ask the others if you need help!"
                show sprocko happy
                s "Now leave me alone. I must adjust these...{w=0.25} CAPACITORS!"
                hide sprocko
                $ powertalk = True
                $roommanager.returnfrominteraction(roommanager.currentroom)
            else:
                r "How do we power up the station again?"
                s "Just plug the ship STRIAGHT into this hub connector!"
                s "Find and connect the power fittings to both the ship and the station!"
                r "Got it!"
            jump sprockotalking
        "BELOW IS TESTING":
            r "Can I get advice?"
            s "Go away!"
            jump sprockotalking
        "Explore":
            r "Can you explore the other room?"
            s "Sure thing."
            hide sprocko with dissolve
            $roommanager.intertoggle(sprocko_rm2)
            $roommanager.intertoggle(sprocko_rm3)
            $roommanager.returnfrominteraction(roommanager.currentroom)
        "Go away":
            r "I want you to vanish from everywhere."
            s "Sure thing."
            hide sprocko with dissolve
            $roommanager.intertoggle_off(sprocko_rm2)
            $roommanager.intertoggle_off(sprocko_rm3)
            $roommanager.returnfrominteraction(roommanager.currentroom)
        "Power up station TEST" if power == False:
            r "Can you turn up the power? "
            s "Sure thing but this will shut off the ship!"
            hide sprocko with dissolve
            $ power = True
            $roommanager.intertoggle(ai_rm2)
            $roommanager.setuproom(2)
        "Power down station TEST" if power == True:
            r "Can you cut off the power?"
            s "Um ok."
            hide sprocko with dissolve
            $ power = False
            $roommanager.intertoggle(ai_rm2)
            $roommanager.setuproom(2)
        "Toggle water":
            r "Can togglewater?"
            s "sure thing Rookie."
            hide sprocko with dissolve
            if water_on == False:
                $ water_on = True
            else:
                $ water_on = False
            $roommanager.returnfrominteraction(roommanager.currentroom)
        "Back":
            hide sprocko with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)


######################## Gelato ########################
label gelatotalk:
    show gelato normal with dissolve:
        zoomnorm
        left
    g "What's going on human Rookie?"
    label gelatotalking:
    menu(screen ='talk'):
        "Power up station" if gstatus == 0:
            if stalk1 == False:
                r "What to do about power."
                g "No idea!! talk to Sprocko!"
                jump gelatotalking
            elif gtalk1 == False:
                g "Take hit set of keys!"
                show item_keyset with dissolve:
                    xalign 0.5
                    yalign 0.5
                item "Received \"Key Set\""
                hide item_keyset with dissolve
                $inventory.items.append(item_keyset)
                $renpy.block_rollback()
                $ gtalk1 = True
                jump gelatotalking
            g "use that to get item power extender!"
            jump gelatotalking
        "Need help?":
            r "Do you need help?"
            g "Nope it's all good."
            jump gelatotalking
        "BELOW IS TESTING":
            r "Test?"
            g "Yup."
            jump gelatotalking
        "Advice":
            r "Can I get advice?"
            g "Apple a day keeps the donkeys away... I think..."
            jump gelatotalking
        "Explore":
            r "Can you explore the other room?"
            g "Sure thing."
            hide gelato with dissolve
            $roommanager.intertoggle(gelato_rm2)
            $roommanager.intertoggle(gelato_rm5)
            $roommanager.returnfrominteraction(roommanager.currentroom)
        "Back":
            hide gelato with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)

# "The station":
#     r "What can you tell me about the station?"
#     g "Well It's a human station for sure."
#     g "If you look, everything is proportional to you guys. The stairs, the table, even the doors."
#     g "But mainly it's the air!"
#     r "The air?"
#     g "Yeah its the perfect mixture of oxygen, nitrogen, elements. A Perfect replicata of Earth air and ideal for humans."
#     g "You see we Troaderlites are very sensitive to air qaulitiy since we often times breath through our skin."
#     g "When at rest we don't even need to use our lungs!"
#
# "Troaderlites":
#     r "What can you tell me about Troaderlites in general?"
#     g "Well... You know we aren't the most liked species in the galaxy..."
#     g "Because of that war and everything..."
#     g "It's tough sometimes but I try to manage."
#     g "I'm thankful Captain Otus took me onto his crew. It's just so much fun!"
#     g "Sorry... I didn't really answer your question..."



######################## Otus ########################
label otustalk:
    show otus normal with dissolve:
        zoomnorm
        left
    o "Huh? What is it?"
    label otustalking:
    menu(screen ='talk'):
        "Need help?":
            r "Do you need help?"
            o "Not from you."
            jump otustalking
        "BELOW IS TESTING":
            r "Test?"
            o "Yup."
            jump otustalking
        "Advice":
            r "Can I get advice?"
            o "Be useful Rookie."
            jump otustalking
        "Explore":
            r "Can you explore the other room?"
            o "Sure thing."
            hide otus with dissolve
            $roommanager.intertoggle(otus_rm2)
            $roommanager.intertoggle(otus_rm6)
            $roommanager.returnfrominteraction(roommanager.currentroom)
        "Back":
            hide ai with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)



######################## Caretaker AI ########################
label aitalk:
    show ai normal with dissolve:
        zoomnorm
        left
    ai "You are unwelcome."
    label aitalking:
    menu(screen ='talk'):
        "BELOW IS TESTING":
            r "Test?"
            ai "Yup."
            jump aitalking
        "Need help?":
            r "Do you need help?"
            ai "Do not disturb my master."
            jump aitalking
        "Be evil or weird":
            r "you werid now?"
            ai "Please leave this station."
            show ai happye with hop
            ai "OR DONT!"
            show ai normal with wiggle
            ai "Sorry I don't know whats going on."
            show ai unhappye with hop
            ai "GAHHHHHH!"
            show ai unhappy with wiggle
            ai "Sometimes I get like this..."
            jump aitalking
        "Back":
            hide ai with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)
