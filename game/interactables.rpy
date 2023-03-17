###### Interactables

###### rm_0 cold sleep locker ######
label showerchoice:
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
    dd "dirty shoe..."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label locker1look:
    dd "open locker for something."
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

label NAVTEMP: ##### TESTING
menu(screen ='choice'):
    "Go to bridge":
        jump introbridge
    "Stay":
        $roommanager.returnfrominteraction(roommanager.currentroom)

###### rm_1 bridge ######
label mainwindowlook:
    dd "look at space or planet."
    menu(screen ='choice'): #TESTING ONLY
        "go to hub this is for testing": #TESTING ONLY
            jump introhub
        "stay": #TESTING ONLY
            $roommanager.returnfrominteraction(roommanager.currentroom)

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













##### TESTING LOCATION OF INTERACTABLES ##### TESTING LOCATION OF INTERACTABLES
call screen TESTLOCATIONS
screen TESTLOCATIONS:

    imagebutton: #radiatortop
        xpos 200
        ypos 660
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #radiatorbot
        xpos 195
        ypos 910
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #captain chair
        xpos 1430
        ypos 650
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #navigator seat
        xpos 1090
        ypos 500
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #captain screen
        xpos 1570
        ypos 520
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #idol
        xpos 1450
        ypos 450
        auto "/inter/inter_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #readouts
        xpos 1425
        ypos 580
        auto "/inter/inter_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #main screen visualizer
        xpos 1760
        ypos 140
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #ship vents
        xpos 170
        ypos 320
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #vent buttons
        xpos 103
        ypos 526
        auto "/inter/inter_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #ship wires
        xpos 490
        ypos 0
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #ship data and food
        xpos 600
        ypos 340
        auto "/inter/inter150x300_%s.png"
        action Jump("TESTLOCATIONSEND")


label TESTLOCATIONSEND:


##### TESTING LOCATION OF INTERACTABLES ##### TESTING LOCATION OF INTERACTABLES
