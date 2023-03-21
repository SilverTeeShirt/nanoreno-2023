###### Interactables

###### ###################### ######
###### rm_0 cold sleep locker ######
###### ###################### ######

label showerlook:
    dd "A narrow sonic shower sits uncomfortably in the corner the room."
    menu(screen ='choice'):
        "Take a shower" if shower == False:
            #play sound shower
            dd "You hop in and turn the dial. A wave of ultra sonic pulses hits you all over."
            r "Ahhh! I don't think I can ever get used to this!"
            $ shower = True
            $roommanager.returnfrominteraction(roommanager.currentroom)
        "Leave" if shower == False:
            $roommanager.returnfrominteraction(roommanager.currentroom)
    $roommanager.returnfrominteraction(roommanager.currentroom)
label gloveslook:
    dd "Two pairs of work gloves dangle off the ship's internal super structure."
    dd "They are covered in a layer of dust and grime. Whoever these once belonged have long since gone."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label mirrorlook:
    dd "cleaning station uses sonic pulse gun to reach the hard to clean areas."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label shoe1look:
    if (rm0_shoe.interprogress == 0):
        dd "Dirty shoe...wait, there seems to be something inside."
        $inventory.items.append(lockerkey)
        $rm0_shoe.interprogress = 1
        dd "A small key... I wonder what can I open with it."
    else:
        dd "Nope, I got lucky once. That will have to do."

    $roommanager.returnfrominteraction(roommanager.currentroom)
label locker1look:
    dd "A locker. Always seems to be closed."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label locker2look:
    dd "thats a locker 2."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label gastanklook:
    dd "all sorts of chemicals for the cold sleep process."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_wireslook:
    dd "dangerous wires."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_windowlook:
    dd "look at space."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_wbuttonlook:
    dd "push button, do later."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_noteslook:
    dd "note says do not use pod out of order."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_terminallook:
    dd "COMPUTER have interactions maybe."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label sleeppodlook:
    dd "Large Cold Sleep pods."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label scrathesslook:
    dd "Scratches from the inside."
    $roommanager.returnfrominteraction(roommanager.currentroom)

# label NAVTEMP: ##### TESTING
# menu(screen ='choice'):
#     "Go to bridge":
#         jump introbridge
#     "Stay":
#         $roommanager.returnfrominteraction(roommanager.currentroom)


###### ########### ######
###### rm_1 bridge ######
###### ########### ######

label mainwindowlook:
    dd "look at space or planet."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label radtoplook:
    dd "radiator thing pump top."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label radbotlook:
    dd "radiator thing pump bottom."
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
label trashlook:
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
label rm2_lightslook:
    dd "weird lights. feels like they are watching you when on."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm2_bigdoorlook:
    dd "big ole door leading to ship."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label planetmodellook:
    dd "looks familiar if sprocko in room."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label powermaillook:
    dd "DA MAIL power connect to this."
    $roommanager.returnfrominteraction(roommanager.currentroom)


###### ######## ######
###### rm_3 lab ######
###### ######## ######

# label skyartlook:
#     dd "art."
#     $roommanager.returnfrominteraction(roommanager.currentroom)
# label trashlook:
#     dd "trash messy."
#     $roommanager.returnfrominteraction(roommanager.currentroom)


###### ######## ######
###### rm_4 conservatory ######
###### ######## ######

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
label forestlook:
    dd "dense forest."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label colorfulflowerlook:
    dd "colorful plant can use pollen."
    $roommanager.returnfrominteraction(roommanager.currentroom)


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


######################## Character ##############################

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
        "Is this a test?":
            r "Test?"
            m "Yup."
            jump marnietalking
        "Advice":
            r "Can I get advice?"
            m "Nah."
            jump marnietalking
        "Back":
            hide marnie with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)




label sprockotalk:
    show sprocko normal with dissolve:
        zoomnorm
        left
    s "What's going on Rookie?"
    label sprockotalking:
    menu(screen ='talk'):
        "Need help?":
            r "Do you need help?"
            s "No I'm all set."
            jump sprockotalking
        "Is this a test?":
            r "Test?"
            s "Yup."
            jump sprockotalking
        "Advice":
            r "Can I get advice?"
            s "Go away!"
            jump sprockotalking
        "Back":
            hide sprocko with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)

label gelatotalk:
    dd "test."
    $roommanager.returnfrominteraction(roommanager.currentroom)

label otustalk:
    dd "test."
    $roommanager.returnfrominteraction(roommanager.currentroom)

label aitalk:
    dd "test."
    $roommanager.returnfrominteraction(roommanager.currentroom)





##### TESTING LOCATION OF INTERACTABLES ##### TESTING LOCATION OF INTERACTABLES

label TESTLOCATIONSEND:
call screen TESTLOCATIONS
screen TESTLOCATIONS:
    imagebutton: #hanging plants
        xpos 620
        ypos 30
        auto "/inter/inter800x250_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #garden
        xpos -100
        ypos 550
        auto "/inter/inter800x250_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #scarecrow
        xpos 50
        ypos 300
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #watertank
        xpos 390
        ypos 90
        auto "/inter/inter150x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #stair
        xpos 1750
        ypos 275
        auto "/inter/inter150x650_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #panels
        xpos 930
        ypos 265
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #pump house front
        xpos 930
        ypos 535
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #pipes
        xpos 660
        ypos 475
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #forest
        xpos 1410
        ypos 490
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #colorful plant
        xpos 1520
        ypos 90
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")

    imagebutton: #colorful plant
        xpos 1520
        ypos 90
        auto "/inter/talk/marnie2_%s.png"
        action Jump("TESTLOCATIONSEND")
