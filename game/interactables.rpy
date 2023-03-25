###### Interactables

###### ###################### ######
###### rm_0 cold sleep locker ######
###### ###################### ######

label showerlook:
    dd "A narrow sonic shower sits uncomfortably in the corner the room."
    menu(screen ='choice'):
        "Take a shower" if shower == False:
            dd "You hop in the shower and turn the dial."
            play sound sonicshower volume 0.9
            dd "A wave of ultra sonic pulses hits you all over."
            r "Ahhh! How can anyone ever get used to this?!"
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
        show item_key1 with dissolve:
            xalign 0.5
            yalign 0.5
        item "Received \"Locker Key\""
        hide item_key1 with dissolve
        $inventory.items.append(lockerkey)
        $rm0_shoe.interprogress = 1
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
label forestlook:
    dd "dense forest."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label colorfulflowerlook:
    dd "colorful plant can use pollen."
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
    show gelato normal with dissolve:
        zoomnorm
        left
    s "What's going on human Rookie?"
    label gelatotalking:
    menu(screen ='talk'):
        "Need help?":
            r "Do you need help?"
            g "Nope it's all good."
            jump gelatotalking
        "Is this a test?":
            r "Test?"
            g "Yup."
            jump gelatotalking
        "Advice":
            r "Can I get advice?"
            g "Apple a day keeps the donkeys away... I think..."
            jump gelatotalking
        "Back":
            hide gelato with dissolve
            $roommanager.returnfrominteraction(roommanager.currentroom)

label otustalk:
    dd "test."
    $roommanager.returnfrominteraction(roommanager.currentroom)

label aitalk:
    dd "test."
    $roommanager.returnfrominteraction(roommanager.currentroom)





##### TESTING LOCATION OF INTERACTABLES ##### TESTING LOCATION OF INTERACTABLES
scene bg_6core_room
##### TESTING LOCATION OF INTERACTABLES ##### TESTING LOCATION OF INTERACTABLES
label TESTLOCATIONSEND:
call screen TESTLOCATIONS
screen TESTLOCATIONS:
    imagebutton: #booth
        xpos 0
        ypos 550
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #plantmonster
        xpos 295
        ypos 110
        auto "/inter/inter150x650_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #paintings
        xpos 300
        ypos 10
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #eyetree
        xpos 5
        ypos 20
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #moose
        xpos 690
        ypos 130
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #harpoon
        xpos 710
        ypos 0
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #bones
        xpos 1100
        ypos 30
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #bughead
        xpos 1525
        ypos 210
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #tubemachine
        xpos 1580
        ypos 30
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #drink maker
        xpos 1240
        ypos 400
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #drinks1
        xpos 1050
        ypos 400
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #drinks2
        xpos 1450
        ypos 435
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #datapad
        xpos 1390
        ypos 555
        auto "/inter/inter_%s.png"
        action Jump("TESTLOCATIONSEND")

    imagebutton: #gelato
        xpos 440
        ypos 140
        auto "/inter/talk/gelato2_%s.png"
        action Jump("TESTLOCATIONSEND")
##### TESTING LOCATION OF INTERACTABLES ##### TESTING LOCATION OF INTERACTABLES
