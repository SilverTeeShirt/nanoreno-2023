## Defines

label showerchoice:
    dd "A narrow sonic shower sits uncomfortably in the corner the room."
    menu(screen ='choice'):
        "Take a shower" if shower == False:
            #play sound shower
            dd "You hop in and turn the dial. A wave of ultra sonic pulses hits you all over."
            r "Ahhh! I don't think I can ever get used to this!"
            $ shower = True
            $roommanager.setuproom(0)
        "Leave" if shower == False:
            $roommanager.setuproom(0)
    $roommanager.setuproom(0)
label gloveslook:
    dd "Two pairs of work gloves dangle off the ship's internal super structure."
    dd "They are covered in a layer of dust and grime. Whoever these once belonged have long since gone."
    $roommanager.setuproom(0)
label mirrorlook:
    dd "cleaning station uses sonic pusle gun to reach the hard to clean areas."
    $roommanager.setuproom(0)
label shoe1look:
    dd "dirty shoe..."
    $roommanager.setuproom(0)
label locker1look:
    dd "open locker for something."
    $roommanager.setuproom(0)
label locker2look:
    dd "thats a locker 2."
    $roommanager.setuproom(0)
label gastanklook:
    dd "all sorts of chemicals for the cold sleep process."
    $roommanager.setuproom(0)
label rm0_wireslook:
    dd "dangerous wires."
    $roommanager.setuproom(0)
label rm0_windowlook:
    dd "look at space."
    $roommanager.setuproom(0)
label rm0_wbuttonlook:
    dd "push button, do later."
    $roommanager.setuproom(0)
label rm0_noteslook:
    dd "note do not use pod out of order."
    $roommanager.setuproom(0)
label rm0_terminallook:
    dd "COMPUTER."
    $roommanager.setuproom(0)
label sleeppodlook:
    dd "Large coldsleep pods."
    $roommanager.setuproom(0)
label scrathesslook:
    dd "Scratches from the inside."
    $roommanager.setuproom(0)








label NAVTEMP:
menu(screen ='choice'):
    "Stay":
        $roommanager.setuproom(0)
    "Go to bridge":
        jump introbridge


##### TESTING LOCATION OF INTERACTABLES ##### TESTING LOCATION OF INTERACTABLES
call screen TESTLOCATIONS
screen TESTLOCATIONS:
    imagebutton: #gloves
        xpos 1490
        ypos 350
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #mirror
        xpos 1619
        ypos 290
        auto "/inter/inter150x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #shoe
        xpos 1300
        ypos 720
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #locker 1
        xpos 1200
        ypos 333
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #locker 2
        xpos 740
        ypos 333
        auto "/inter/inter150x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #cold sleep gas tanks
        xpos 70
        ypos 40
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #wires
        xpos 380
        ypos 20
        auto "/inter/inter300x150_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #window
        xpos 970
        ypos 250
        auto "/inter/inter150x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #window button
        xpos 1002
        ypos 583
        auto "/inter/inter_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #note
        xpos 440
        ypos 430
        auto "/inter/inter_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #terminal
        xpos 10
        ypos 650
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #cold sleep pod
        xpos 130
        ypos 390
        auto "/inter/inter300x300_%s.png"
        action Jump("TESTLOCATIONSEND")
    imagebutton: #scrathes
        xpos 460
        ypos 560
        auto "/inter/inter150x300_%s.png"
        action Jump("TESTLOCATIONSEND")

label TESTLOCATIONSEND:


##### TESTING LOCATION OF INTERACTABLES ##### TESTING LOCATION OF INTERACTABLES
