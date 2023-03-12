## Transform
## Use at: EXAMPLE show c_alien at wiggle

transform leftish:
    xalign 0.2 yalign 1.0
transform rightish:
    xalign 0.8 yalign 1.0
transform leftcenter:
    xalign 0.4 yalign 1.0
transform rightcenter:
    xalign 0.6 yalign 1.0

## Normal
transform zoomnorm:
    zoom .625 yalign 1.0

transform wiggle:
    ease 0.1 yoffset 20
    ease 0.1 yoffset 0
transform hop:
    ease 0.1 yoffset -30
    ease 0.1 yoffset 0
transform sway:
    ease 0.2 xoffset -10
    ease 0.2 xoffset 20
    ease 0.2 xoffset 0
transform flip:
    xzoom -1.0
transform flicker:
    alpha 1
    pause 0.1
    alpha 0
    pause 0.1
    alpha 1
    repeat

## Transitions ## Transitions
## Use with: EXAMPLE show c_alien with fadeslow

define fadeslow = Fade(1.5, 0.5, 1.5)
define dissolveslow = Dissolve(1.6)

define disfastnowait = { "master" : Dissolve(0.1) }

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define disnowait = { "master" : Dissolve(1.0) }
define disnowaitslow = { "master" : Dissolve(5.0) }
define fadenowait = { "master" : Fade(1.0, 0.0, 1.0) }
define vpunchnowait = { "master" : Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275) }

define disnowaitlabdoor = { "master" : Dissolve(2.5) }
