## Images bgcolors

image bgblack = "#000000"
image bgblack2 = "#000000"
image bgwhite = "#FFFFFF"
image bgred = "#FF0000"
image bgblue = "#0064FF"

image no_img:
    "#000000"
    alpha 0.0

## Space

image spacemoving:
    contains:
        "/bg/bg_Xstars0.png"
        xalign 0.0
        linear 240.0 xpos 1920
        repeat
    contains:
        "/bg/bg_Xstars0.png"
        xalign 1.0
        linear 240.0 xpos 1920
        repeat
    contains:
        "/bg/bg_Xstars1.png"
        xalign 0.0
        linear 190.0 xpos 1920
        repeat
    contains:
        "/bg/bg_Xstars1.png"
        xalign 1.0
        linear 190.0 xpos 1920
        repeat
    contains:
        "/bg/bg_Xstars2.png"
        xalign 0.0
        linear 160.0 xpos 1920
        repeat
    contains:
        "/bg/bg_Xstars2.png"
        xalign 1.0
        linear 160.0 xpos 1920
        repeat

## Menu

image main_menu:
    contains:
        "spacemoving"
    contains:
        "/gui/main_menubeam.png"
        alpha 0.7
        zoom 0.9
        xpos 150
        ypos -50
    contains:
        "/gui/main_menu.png"
        zoom 0.5
        xalign 1.0
        yalign 0.9

image titlecard:
    "/gui/main_menutitle.png"
    zoom 0.6
    xalign 0.05
    yalign 0.05

## CG

image CG1:
    contains:
        "/cg/cg01bg.png"
    contains:
        "CG1stars"
    contains:
        "/cg/cg01station.png"
    contains:
        "CG1ship"
        ease 2.5 ypos 20
        ease 2.5 ypos 0
        repeat

image CG1docked:
    contains:
        "/cg/cg01bg.png"
    contains:
        "CG1stars"

image CG1stars:
    "/cg/cg01star1.png" with dissolveslow
    pause 1.6
    "/cg/cg01star2.png" with dissolveslow
    pause 1.6
    repeat

image CG1ship:
    contains:
        "/cg/cg01ship.png"
    contains:
        "/cg/cg01shipengine.png"

## Images Rooms

image bg_0cold_roomP:
    contains:
        "spacemoving"
    contains:
        "coldwindow"
    contains:
        "/bg/bg_0cold.png"
    contains:
        "/bg/bg_0coldscreen.png"
        alpha .55
        pause .08
        "/bg/bg_0coldscreen.png"
        alpha .3
        pause .08
        repeat
image bg_0cold_roomP2:
    contains:
        "spacemoving"
    contains:
        "coldwindow2"
    contains:
        "/bg/bg_0cold2.png"
image coldwindow = ConditionSwitch(
    "coldwindow_on", "/bg/bg_0coldwindow.png",
    "True", "no_img")
image coldwindow2 = ConditionSwitch(
    "coldwindow_on", "/bg/bg_0coldwindow2.png",
    "True", "no_img")
image bg_0cold_room = ConditionSwitch(
    "power", "bg_0cold_roomP2",
    "True", "bg_0cold_roomP")



image bg_1bridge_roomP:
    contains:
        "spacemoving"
    contains:
        "/bg/bg_1bridge.png"
    contains:
        "/bg/bg_1bridgescreen.png"
        alpha .55
        pause .08
        "/bg/bg_1bridgescreen.png"
        alpha .3
        pause .08
        repeat
    contains:
        "bridgecord"
image bg_1bridge_roomP2:
    contains:
        "spacemoving"
    contains:
        "/bg/bg_1bridge2.png"
image bridgecord = ConditionSwitch(
    "bridgecord_on", "/bg/bg_1bridgecord.png",
    "True", "no_img")
image bg_1bridge_room = ConditionSwitch(
    "power", "bg_1bridge_roomP2",
    "True", "bg_1bridge_roomP")



image bg_2hub_roomP:
    contains:
        "spacemoving"
    contains:
        "/bg/bg_2hub.png"
    contains:
        "hubcord"
image bg_2hub_roomP2:
    contains:
        "spacemoving"
    contains:
        "/bg/bg_2hub2.png"
image hubcord = ConditionSwitch(
    "hubcord_on", "/bg/bg_2hubcord.png",
    "True", "no_img")
image bg_2hub_room = ConditionSwitch(
    "power", "bg_2hub_roomP2",
    "True", "bg_2hub_roomP")



image bg_3lab_room:
    contains:
        "spacemoving"
    contains:
        "/bg/bg_3lab.png"
    contains:
        "/bg/bg_3labscreen.png"
        alpha .55
        pause .08
        "/bg/bg_3labscreen.png"
        alpha .3
        pause .08
        repeat
    contains:
        "labpulse"
    contains:
        "labwaterfill"
image labwaterfill = ConditionSwitch(
    "water_on", "/bg/bg_3labfill.png",
    "True", "no_img")
image labpulse:
    "/bg/bg_3labpulse.png" with dissolveslow
    pause 2
    "/bg/bg_3labpulse2.png" with dissolveslow
    pause 2
    repeat



image bg_4con_room:
    contains:
        "spacemoving"
    contains:
        "/bg/bg_4con.png"
    contains:
        "conbird"
    contains:
        "convine"
image convine = ConditionSwitch(
    "convine_off", "no_img",
    "True", "/bg/bg_4convine.png")
image conbirdactive:
    "/bg/bg_4conbeak.png"
    ease 0.1 ypos -15
    ease 0.1 ypos 0
    pause 1
    ease 1.0 xpos 15
    pause 3
    ease 0.1 ypos -15
    ease 0.1 ypos 0
    ease 0.1 ypos -15
    ease 0.1 ypos 0
    ease 1.0 xpos -15
    pause 1
    ease 0.1 ypos -15
    ease 0.1 ypos 0
    pause 4
    ease 1.0 xpos 15
    pause 1.5
    ease 1.0 xpos 0
    pause 2
    ease 0.1 xpos 5
    ease 0.1 xpos -5
    ease 0.1 xpos 5
    ease 0.1 xpos -5
    ease 0.1 xpos 5
    ease 0.1 xpos -5
    ease 0.1 xpos 5
    ease 0.1 xpos -5
    ease 0.1 xpos 5
    ease 0.1 xpos -5
    pause 1
    ease 0.1 ypos -15
    ease 0.1 ypos 0
    repeat
image conbird = ConditionSwitch(
    "conbird_off", "no_img",
    "True", "conbirdactive")

image bg_5bar_room:
    contains:
        "spacemoving"
    contains:
        "/bg/bg_5bar.png"
    contains:
        "barwaterfill"
image barwaterfill = ConditionSwitch(
    "water_on", "/bg/bg_5barfill.png",
    "True", "no_img")


image bg_6core_room:
    contains:
        "spacemoving"
    contains:
        "/bg/bg_6coreback.png"
    contains:
        "coreglow"
    contains:
        "/bg/bg_6core.png"
    contains:
        "/bg/bg_6corescreen.png"
        alpha .55
        pause .08
        "/bg/bg_6corescreen.png"
        alpha .3
        pause .08
        repeat
    contains:
        "jarman_image"

image bg_6core_roomforeground:
    contains:
        "coreglow"
    contains:
        "/bg/bg_6core.png"
    contains:
        "/bg/bg_6corescreen.png"
        alpha .55
        pause .08
        "/bg/bg_6corescreen.png"
        alpha .3
        pause .08
        repeat
    contains:
        "jarman_image"

image coreglow:
    "/bg/bg_6coreglow.png" with dissolveslow
    pause 2
    "/bg/bg_6coreglow2.png" with dissolveslow
    pause 2
    repeat
image jarmanactive:
    contains:
        "/bg/bg_6core_jar.png"
    contains:
        "/bg/bg_6core_jarman2.png"
        ease 6.7 ypos 11
        ease 5.9 ypos -5
        repeat
    contains:
        "/bg/bg_6core_jarman1.png"
        ease 5.6 ypos 11
        ease 5.3 ypos 0
        repeat
    contains:
        "/bg/bg_6core_jarman3.png"
        ease 3.7 ypos -5
        ease 4.3 ypos 0
        repeat
image jarman_image = ConditionSwitch(
    "corejarman_on", "jarmanactive",
    "True", "no_img")

## Images Characters

## AI

image ai normal = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/ai/CaretakerNeutral.png"
    )

image ai unhappy = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/ai/CaretakerUnhappy.png"
    )

image ai happy = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/ai/CaretakerHappy.png"
    )

image ai normale = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/ai/CaretakerNeutralEvil.png"
    )

image ai unhappye = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/ai/CaretakerUnhappyEvil.png"
    )

image ai happye = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/ai/CaretakerHappyEvil.png"
    )

## Marnie

image marnie normal = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/mar/MarnieNeutral.png",
    )

image marnie unhappy = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/mar/MarnieUnhappy.png",
    )

image marnie happy = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/mar/MarnieHappy.png",
    )

image marnie shocked = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/mar/MarnieShocked.png",
    )

## Otus

image otus normal = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/otus/OtusNeutral.png",
    )

image otus unhappy = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/otus/OtusUnhappy.png",
    )

image otus happy = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/otus/OtusHappy.png",
    )

## Gelato

image gelato normal = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/gel/GelatoNeutral.png",
    )

image gelato unhappy = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/gel/GelatoUnhappy.png",
    )

image gelato happy = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/gel/GelatoHappy.png",
    )

image gelato shocked = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/gel/GelatoShocked.png",
    )

## Sprocko

image sprocko normal = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/spro/SprockoNeutral.png",
    )

image sprocko unhappy = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/spro/SprockoUnhappy.png",
    )

image sprocko happy = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/spro/SprockoHappy.png",
    )

image sprocko shocked = LiveComposite(
    (1920, 1750),
    (0, 0), "/char/spro/SprockoShocked.png",
    )





## ITEMS

image small_item_key1:
    "item/item_key1.png"
    zoom .25
