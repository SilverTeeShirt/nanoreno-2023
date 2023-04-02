###### Item Interactions

######object description and result labels, move to own screen later?############
##rm0_lockerkey

label rm0_lockersolution:
    dd "Unlock the locker with the diamond symbol opened."
    dd "You place the key back to where you found it."
    show item_food1 with dissolve:
        xalign 0.5
        yalign 0.5
    item "Received \"Food Bar\""
    item "Lost \"Small Key\""
    hide item_food1 with dissolve
    $inventory.items.append(rm0_food)
    $inventory.removeitem(rm0_lockerkey)
    $renpy.block_rollback()
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_lockerkeycommsp:
    s "Hi, that's a key, a bit too analog for my taste."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_lockerkeycommmar:
    m "Hi, that's a key, I think it might open one of the lockers?"

    $rm0_lockerkey.targetinter.append("locker1") 

    $rm0_lockerkey.solutionlabs.append("rm0_lockersolution")

    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_lockerkeycommot:
    o "Hi, that's a key, I am not sure it's yours rookie."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_lockerkeycomgel:
    g "Hi, that's my key, I was wondering where it went."

    $rm0_food.targetinter.append("Gelato")

    $rm0_food.solutionlabs.append("rm0_foodsolution")

    $rm0_lockerkey.targetinter.append("locker1") 

    $rm0_lockerkey.solutionlabs.append("rm0_lockersolution")

    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_lockerkeycomai:
    ai "A key. Now go away."
    $roommanager.returnfrominteraction(roommanager.currentroom)



label rm0_foodsolution:
    dd "With a single gulp, Gelato ingests the food bar. Wrapper and all."
    g "That really hit the spot!"
    $inventory.removeitem(rm0_food)
    $renpy.block_rollback()
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_foodcommsp:
    s "I think I ate a few of those back in high school... I think it's Gelato's"

    $rm0_food.targetinter.append("Gelato")

    $rm0_food.solutionlabs.append("rm0_foodsolution")
    
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_foodcommmar:
    m "Oh wow that... that looks bad. No thanks."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_foodcommot:
    o "A special nutrition bar. Not compatible with my species."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label rm0_foodcomgel:
    g "Oh hey, if it isn't my food bar, thanks buddy!"
    jump rm0_foodsolution
label rm0_foodcomai:
    ai "Egads, what ghastly manner of food is that?"
    $roommanager.returnfrominteraction(roommanager.currentroom)



label item_fittingssolution:
    dd "You plug in the Extendable Power Fittings."
    $powerplug1 = True
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_fittingscommsp:
    s "Yes that is the Extendable Power Fittings! Good job!"
    s "Now plug it DIRECTLY into the ship and this hub connector!"
    s "Talk to me when you've figured it out."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_fittingscomgel:
    g "That's the Extendable Power Fittings alright. It's Super stretchy and should be able to reach however far you need."
    $roommanager.returnfrominteraction(roommanager.currentroom)


# Nothing to say about Item

label item_NAsp:
    s "What do you want me to do with that?"
    s "Sorry I'm too busy trying to do THINGS!"
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_NAmar:
    m "Sorry what is that?"
    m "I guess it's nice..."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_NAgel:
    g "Very cool, but I'm not sure what it is..."
    g "Is that from Earth or something?"
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_NAot:
    o "Rookie sometimes I don't know why I hired you."
    o "Get back to work and stop messing about."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_NAai:
    ai "That is certainly something."
    ai "I'm positive you can do something with it somewhere else."
    $roommanager.returnfrominteraction(roommanager.currentroom)
