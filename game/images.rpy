## Images bgcolors

image bgblack = "#000000"
image bgblack2 = "#000000"
image bgwhite = "#FFFFFF"
image bgred = "#FF0000"
image bgblue = "#0064FF"

## Images Rooms

image bg_0cold_room:
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
    contains:
        "/bg/bg_0cold.png"

image bg_1bridge_room:
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
    contains:
        "/bg/bg_1bridge.png"

image bg_2hub_room:
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
    contains:
        "/bg/bg_2hub.png"

image bg_3lab_room:
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
    contains:
        "/bg/bg_3lab.png"

image bg_4con_room:
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
    contains:
        "/bg/bg_4con.png"

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
    (0, 0), "/char/ai/CaretakerHappy"
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
