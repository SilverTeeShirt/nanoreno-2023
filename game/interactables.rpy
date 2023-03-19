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






######################### #### ###############################
######################### TALK ###############################
######################### #### ###############################

label marnietalk:
    dd "talk marnie test."
    $roommanager.returnfrominteraction(roommanager.currentroom)

label sprockotalk:
    dd "test."
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

    imagebutton: #sky art
        xpos 510
        ypos 80
        auto "/inter/inter800x250_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #trash
        xpos 1350
        ypos 900
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #table
        xpos 1520
        ypos 720
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #charge station
        xpos 1740
        ypos 610
        auto "/inter/inter150x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #door 1
        xpos 1550
        ypos 360
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #door 2
        xpos 80
        ypos 360
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #logo
        xpos 885
        ypos 350
        auto "/inter/inter150x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #Elevator Door
        xpos 810
        ypos 670
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #Light 1
        xpos 710
        ypos 720
        auto "/inter/inter_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #Light 2
        xpos 1128
        ypos 720
        auto "/inter/inter_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #Heavy door
        xpos 0
        ypos 650
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #planet model
        xpos 1355
        ypos 160
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #power node mail
        xpos 350
        ypos 775
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #marnie1
        xpos 540
        ypos 690
        auto "/inter/talk/marnie1_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #otus1
        xpos 1100
        ypos 650
        auto "/inter/talk/otus1_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #gelato1
        xpos 1150
        ypos 450
        auto "/inter/talk/gelato1_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #sprocko1
        xpos 250
        ypos 740
        auto "/inter/talk/sprocko1_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #ai1
        xpos 1700
        ypos 680
        auto "/inter/talk/ai1_%s.png"
        action Jump("TESTLOCATIONSEND")
##### TESTING LOCATION OF INTERACTABLES ##### TESTING LOCATION OF INTERACTABLES
