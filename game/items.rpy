###### Item Interactions

#bootkey
label itembootkeydesc:
    if bootkeyclean == False:
        dd "A stinky key found in a stinky boot."
    else:
        dd "A recently cleaned key found in a stinky boot."
    jump invscreensetup

label item_bootkeysolution:
    if bootkey1use == False:
        $bootkey1use = True
        dd "You open the locker and rummage through it."
        show item_datapad with dissolve:
            xalign 0.5
            yalign 0.5
        item "Received \"Universal Datapad\""
        hide item_datapad with dissolve
        $inventory.items.append(item_datapad)
        $renpy.block_rollback()
    else:
        dd "You've already rummaged through this locker."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_bootkeysolution2:
    dd "The key doesn't work on this set of lockers."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_bootkeysolution3:
    if bootkeyclean == False and power == False:
        $bootkeyclean = True
        play sound sonicshower
        dd "You blast the key with the sonic gun."
        dd "Not a single hint of boot stank is on it anymore."
    elif bootkeyclean == False and power == True:
        dd "Since the ship doesn't have any power you'll have to deal with this stinky key as is."
    else:
        dd "The key is already clean and shiny."
    $roommanager.returnfrominteraction(roommanager.currentroom)

label item_bootkeymar:
    if bootkeyclean == False and shower == False:
        m "What is that awful smell?"
        m "..."
        m "Is that you Rookie?"
        m "You really are just a stinky person aren't you?"
    elif bootkeyclean == False:
        m "Why are you showing me this stinky key?"
        m "Well it should open one of the lockers in the cold sleep room."
    else:
        m "That key should open one of the lockers in the cold sleep room."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_bootkeygel:
    if bootkeyclean == False:
        g "Hey one of the keys I was missing! I was wondering where that went."
        g "It smells a tad funky..."
    else:
        g "Hey one of the keys I was missing! I was wondering where that went."
    $roommanager.returnfrominteraction(roommanager.currentroom)





# OLD CODE USE FOR REFERENCE##################################
# label rm0_bootkeygel:
#     g "Hi, that's my key, I was wondering where it went."
#
#     $rm0_food.targetinter.append("Gelato")
#
#     $rm0_food.solutionlabs.append("rm0_foodsolution")
#
#     $rm0_bootkey.targetinter.append("locker1")
#
#     $rm0_bootkey.solutionlabs.append("rm0_lockersolution")
#
#     $roommanager.returnfrominteraction(roommanager.currentroom)

#     $inventory.removeitem(item_fittings)

# #food
# label rm0_foodsolution:
#     dd "With a single gulp, Gelato ingests the food bar. Wrapper and all."
#     g "That really hit the spot!"
#     $inventory.removeitem(rm0_food)
#     $renpy.block_rollback()
#     $roommanager.returnfrominteraction(roommanager.currentroom)
# label rm0_foodmsp:
#     s "I think I ate a few of those back in high school... I think it's Gelato's"
#
#     $rm0_food.targetinter.append("Gelato")
#
#     $rm0_food.solutionlabs.append("rm0_foodsolution")
#
#     $roommanager.returnfrominteraction(roommanager.currentroom)
# label rm0_foodmar:
#     m "Oh wow that... that looks bad. No thanks."
#     $roommanager.returnfrominteraction(roommanager.currentroom)
# label rm0_foodgel:
#     g "Oh hey, if it isn't my food bar, thanks buddy!"
#     jump rm0_foodsolution
# label rm0_foodmot:
#     o "A special nutrition bar. Not compatible with my species."
#     $roommanager.returnfrominteraction(roommanager.currentroom)


#Step 2 for item description: create label with the same name you put in the definition of the Item, put what you want to happen when you look at the description there.

# label itemkeysetdesc:
#     dd "A set of locker keys."

    #Step 3: we need to jump to somewhere else to avoid the game auto-closing.
    #If we are just supposed to return to the inventory screen, use the following line.

    # jump invscreensetup

    # if instead something happens that requires to do other stuff (change rooms, reset the room like after conversations, add stuff to lists, etc,
    # the same code you would in those cases applies. )




#keyset

label itemkeysetdesc:
    dd "A set of keys."
    jump invscreensetup

label item_keysetsolution1:
    dd "You'll need a different key to open the other locker."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_keysetsolution2:
    if keyset1use == False:
        $keyset1use = True
        dd "You open the locker and rummage through it."
        show item_fittings with dissolve:
            xalign 0.5
            yalign 0.5
        item "Received \"Extendable Power Fittings\""
        hide item_fittings with dissolve
        $subjectfittings = False
        $inventory.items.append(item_fittings)
        $renpy.block_rollback()
    else:
        dd "You've already rummaged through these lockers."
        $roommanager.returnfrominteraction(roommanager.currentroom)
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_keysetmar:
    m "That key set should open up the lockers in the cold sleep room."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_keysetgel:
    g "That's the key set I tend to carry around. Maybe you can handle that job from now on!"
    g "Just don't lose them..."
    $roommanager.returnfrominteraction(roommanager.currentroom)


#fittings
label itemfittingsdesc:
    dd "A large extendable power fitting. It can stretch great distances and carry a high density of energy."
    jump invscreensetup

label item_fittingssolution1:
    if powerplug1 == False:
        $powerplug1 = True
        $bridgecord_on = True
        play sound insert
        dd "You plug in the Extendable Power Fittings into the ventilation power port."
        if powerplug2 == True:
            dd "You've connected the Extendable Power Fittings to both the ship and the station."
            $ stalk2 = True
            $inventory.removeitem(item_fittings)
        else:
            dd "You'll need to connect the other end."
            $roommanager.returnfrominteraction(roommanager.currentroom)
        $roommanager.returnfrominteraction(roommanager.currentroom)
    else:
        dd "You should connect this somewhere else."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_fittingssolution2:
    if powerplug2 == False:
        $powerplug2 = True
        $hubcord_on = True
        play sound insert
        dd "You plug in the Extendable Power Fittings into the hub connector."
        if powerplug1 == True:
            dd "You've connected the Extendable Power Fittings to both the ship and the station."
            $ stalk2 = True
            $inventory.removeitem(item_fittings)
        else:
            dd "You'll need to connect the other end."
            $roommanager.returnfrominteraction(roommanager.currentroom)
        $roommanager.returnfrominteraction(roommanager.currentroom)
    else:
        dd "You should connect this somewhere else."
    $roommanager.returnfrominteraction(roommanager.currentroom)

label item_fittingssp:
    s "Yes! That is the Extendable Power Fittings!"
    s "Now plug it DIRECTLY into the Clover and this hub connector!"
    s "Talk to me when you've figured it out!"
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_fittingsgel:
    g "That's the Extendable Power Fittings alright. It's super stretchy and should be able to reach however far you'll need."
    $roommanager.returnfrominteraction(roommanager.currentroom)



#datapad
label itemdatapaddesc:
    dd "A Universal Datapad."
    jump invscreensetup

label item_datapadsolution1:
    dd "Data has been downloaded."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_datapadsolution2:
    dd "Data has been downloaded."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_datapadsolution3:
    dd "Data has been downloaded."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_datapadsp:
    s "Ahhhh! A Universal Datapad!"
    s "These things easily connect to one another and can hold vast quantities of data, UNIVERSALLY!"
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_datapadmar:
    m "Oh hey you found the Universal Datapad!"
    m "I meant to give you that earlier but I just couldn't find it..."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_datapadgel:
    g "Oh a Universal Datapad."
    g "Everyone should have one. You can message each other, store lots of data, and even play games on them!"
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_datapadot:
    o "Universal Datapads have been around for hundreds of cycles or so."
    o "They are very useful. You should hang on to that."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_datapadai:
    ai "Ahh yes a Universal Datapad."
    ai "Master has a whole closet full of them. They are so easily misplaced..."
    $roommanager.returnfrominteraction(roommanager.currentroom)

# Text Logs
# Cosmic Receipt
#
# 100 x Beryllium containment collectors - 5,999,999 credits
# 5 x Crates of thera-magnetic microfilament - 2,999 credits
# 666 x Metamorality dampeners - 4,444 credits
# 1 x Complete Collection of 'Childrens Library for Little Genuises' - 9,999 credits
#
# Please note - The following item was removed. The reason given was "Waste of Money"
#
# 1 x Teddy Bear - 5 credits
#
#
# To-Do List
# To-do list -
# 	Have The Caretaker perform a maintenance sweep of the ship.
# 	Install the latest trophy in the bar
# 	Have The Caretaker check the Zeta shielding to prevent detection.
# 	Check on the lab tests on the Bio Duplicator, should be working now
# 	Have The Caretaker read to Samantha, Newton's 'Philosophiae Naturalis Principia Mathematica'
# 	Walk in the garden for a while
# 	Perform maintenance on The Caretaker to make sure they don't gain too much sentience.
#
#
# Diary 1
#
# Hello Diary. Dad wants me to start writing in you, because uhh…
# Actually, I don't know why. He said something about personality assessment?
# But surely he was kidding, right? I mean, I'm still just a kid!
# CT said that it was probably alright, and I can trust them, at least.
# Urgh, this entry was a bit of a bust. Hopefully I can come up with something better tomorrow.
#
#
# Diary 2
#
# Hello Diary. Guess what? It's my birthday!
# It's been a great day, I only had to do half of my chores (CT took care of the rest of them!).
# I went for a walk in the garden and reread some classics.
# I also spent
# I've been alive for 15 years, all of them spent on the space station.
# Diary 4
#
# Hello Diary. Today sucks.
# Dad found out I had hacked a key for the bar and had been sneaking drinks.



# Nothing to say about Item
label item_NAsp:
    s "What do you want me to do with that?"
    s "Sorry I'm too busy trying to do important, THINGS!"
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_NAmar:
    m "You want me to take a look at this thing?"
    m "I'm not sure what it's for... Maybe the others can help you."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_NAgel:
    g "Very cool! But um... I'm not sure what that is."
    g "Maybe it's something from Earth? I should look into it more..."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_NAot:
    o "Rookie sometimes I don't know why I hired you."
    o "Get back to work and stop messing about."
    $roommanager.returnfrominteraction(roommanager.currentroom)
label item_NAai:
    ai "That is certainly something."
    ai "I'm positive you can do something with it somewhere far away from me."
    $roommanager.returnfrominteraction(roommanager.currentroom)
