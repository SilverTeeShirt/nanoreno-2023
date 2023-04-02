############## ROOM MANAGER PYTON ##############
init offset = -2
init python:

    class Room():
        def __init__(self,name,idnum,bgref,interactablelist,discovered,locked,adjacentrooms,navicon,eventsready):
            self.name = name
            self.idnum = idnum
            self.bgref = bgref
            self.interactablelist = interactablelist
            self.discovered = discovered
            self.locked = locked
            self.adjacentrooms = adjacentrooms
            self.navicon = navicon
            self.eventsready = eventsready

        def bgref_change(self,idnum,bgref):

            self.room[idnum].bgref_change(bgref)

    class RoomManager():
        def __init__(self,name,rooms,currentroom,currinterlayer,gotnav,gotinv,navsys):
            self.name = name
            self.rooms = rooms
            self.currentroom = currentroom
            self.currinterlayer = currinterlayer
            self.gotnav = gotnav
            self.gotinv = gotinv
            self.navsys = navsys

        def addeventstoroom(self,roomid,labelref):

            self.rooms[roomid].eventsready.append(labelref)

        def checkroomevents(self, roomid):

            if (len(self.rooms[roomid].eventsready) > 0):

                roomtocheck = self.rooms[roomid]
                eventtocheck = roomtocheck.eventsready[0]

                roomtocheck.eventsready.remove(eventtocheck)

                #can call be used here?
                renpy.jump(eventtocheck)
                #renpy.call(eventtocheck)

            else:
                self.setuproom(roomid)



        def setuproom(self,idnum):
            self.currentroom = self.rooms[idnum]
            self.currinterlayer = 1
            cr = self.currentroom
            renpy.scene()
            renpy.show(cr.bgref)
            #renpy.with_statement(fadetransnowait)
            cr.discovered = 0
            self.setupinterforroom(cr)
            self.changeinteractionlevel(0)
            self.setupplayerUI()

        def setuproominstant(self,idnum):
            self.currentroom = self.rooms[idnum]


        def setupinterforroom(self,currroom):
            renpy.show_screen("makeinteractables",currroom.interactablelist,self)

        def setupplayerUI(self):
            renpy.jump("uisetup")

        def returnfrominteraction(self, currroom):
            self.setupinterforroom(currroom)
            self.changeinteractionlevel(0)
            self.setupplayerUI()
        
        


        def changeinteractionlevel(self,newilv):
            self.currinterlayer = newilv

        def intiateinteraction(self,selinterjump):
            #renpy.show_screen("interactableinteractionscreen",selinter)

            renpy.call(selinterjump)
            self.setupplayerUI()


        def intertoggle(self,tarinter):

            if tarinter.intertype == 1:

                    tarinter.intertype = 3

            elif tarinter.intertype == 3:

                    tarinter.intertype = 1

        def intertoggle_off(self,tarinter):
            tarinter.intertype = 3

        def intertoggle_on(self,tarinter):
            tarinter.intertype = 1

        def updatenavsys(self):

            self.navsys.clear()

            for rtg in self.currentroom.adjacentrooms:

                self.navsys.append(self.rooms[rtg])





    class Interactable():
        def __init__(self,name,intertype,horposition,verposition,interprogress,interrangequest,interrangelayer,fltext,labelref):
            self.name = name
            self.intertype = intertype #type of interactable
            self.horposition = horposition #change to specific position as opposed to alignment
            self.verposition = verposition
            self.interprogress = interprogress #how far into the chain of interactions the player is (ie: is a dorr you have to open closed or open)
            self.interrangequest = interrangequest #at what points in the chain of interactions (see above) is the button sensitive to player input?
            self.interrangelayer = interrangelayer #at what generic layer of interaction (no menu on screen/navigation/inventory/etc, see roommanager) is this button sensitive to player input?
            self.fltext = fltext #list of flavortexts in response to various situations
            self.labelref = labelref

    class ImageInteractable(Interactable):
        def __init__(self,name,intertype,horposition,verposition,interprogress,interrangequest,interrangelayer,fltext,labelref,imageref,menuimageref):
            super().__init__(name,intertype,horposition,verposition,interprogress,interrangelayer,interrangequest,fltext,labelref)
            self.imageref = imageref
            self.menuimageref = menuimageref



    class TextInteractable(Interactable):
        def __init__(self,name,intertype,horposition,verposition,interprogress,interrangequest,interrangelayer,fltext,textref,xpad,ypad):
            super().__init__(name,intertype,horposition,verposition,interprogress,interrangequest,interrangelayer,fltext,labelref)
            self.textref = textref
            self.xpad = xpad
            self.ypad = ypad

    class Inventory():
        def __init__(self,items,activeitem):
            self.items = items
            self.activeitem = activeitem


        def setactiveitem(self,nitem):
            self.activeitem = nitem

        def removeitem(self,itemr):

            if (itemr in self.items):
                self.items.remove(itemr)

            if (self.activeitem == itemr):
                self.activeitem = ""
        
        def returnfromdescription(self, roommanagerref):

            self.activeitem = ""
            invref = self
            renpy.show_screen("invscreen",None,invref,roommanagerref)






    class Item():
        def __init__(self,name,idnum,imageref,description,targetinter,solutionlabs,dragimg,comments):
            self.name = name
            self.idnum = idnum
            self.imageref = imageref
            self.description = description
            self.targetinter = targetinter
            self.solutionlabs = solutionlabs
            self.dragimg = dragimg
            self.comments = comments

        def interpretdrop(self,drpnm,rmmanagerref):

            commenters = ["Sprocko","Marnie","Gelato","Captain Otus","The Caretaker"]

            if drpnm in self.targetinter:

                solnum = self.targetinter.index(drpnm)

                renpy.jump(self.solutionlabs[solnum])

            elif drpnm in commenters:

                commnum = commenters.index(drpnm)

                renpy.jump(self.comments[commnum])

            else:
                renpy.jump("dragdroplab")







    def dropcheck(drags,drop):

        if not drop:
            return

        store.dragn = drags[0].drag_name
        store.dropn = drop.drag_name

        return True









label dragdroplab:


    default dragn = None

    default dropn = None


    call screen dragdropscreen(inventory,roommanager,inventory.activeitem)

    $inventory.activeitem.interpretdrop(dropn,roommanager)


label invscreensetup:

    call screen invscreen(inventory,roommanager)



label uisetup:

    call screen makeplayerUI(roommanager)



screen makeinteractables(targetinteractables, roommanagerref):

    default localrmanref = roommanagerref


    for ti in targetinteractables:
        if ti.intertype == 1:
            imagebutton:
                xpos ti.horposition
                ypos ti.verposition
                auto ti.imageref
                action [SensitiveIf(localrmanref.currinterlayer == 0), Hide("makeinteractables"), Hide("makeplayerUI"), Function(localrmanref.intiateinteraction,ti.labelref)]


        elif ti.intertype == 2:
            frame:
                xpos ti.horposition
                ypos ti.verposition
                xpadding ti.xpad
                ypadding ti.ypad
                textbutton ti.textref  action [SensitiveIf(localrmanref.currinterlayer == 0), Hide("makeinteractables"), Hide("makeplayerUI"), Function(localrmanref.intiateinteraction,ti.labelref)]


screen interactableinteractionscreen(selectedinteractable):

    default localinterref = selectedinteractable




screen makeplayerUI(roommanagerref):

    default localrmanref = roommanagerref
    default localinvenref = inventory

    #$changevariables


    if (localrmanref.gotnav == 0):
        imagebutton:
            xpos 975
            ypos 950
            auto "gamesys/NAV_%s.png"
            action [SensitiveIf(localrmanref.currinterlayer == 0), Hide("makeplayerUI"), Function(localrmanref.updatenavsys), Show("navscreen",None,localrmanref)]

    if (localrmanref.gotinv == 0):
        imagebutton:
            xpos 775
            ypos 950
            auto "gamesys/INV_%s.png"
            action [SensitiveIf(localrmanref.currinterlayer == 0), Hide("makeplayerUI"),Function(localrmanref.changeinteractionlevel,1),Show("invscreen",None,localinvenref,localrmanref)]





screen navscreen(roommanagerref):

    modal True
    default localrmanref = roommanagerref
    default roomstogoto = roommanagerref.navsys



    imagebutton:
            xalign 0.5
            ypos 950
            auto "gamesys/BCK_%s.png"
            action [Hide("navscreen"),Show("makeplayerUI",None,localrmanref)]

    hbox:

        xalign 0.5
        yalign 0.5

        spacing 20

        for ri in roomstogoto:


            if (ri.locked == 0):

                imagebutton:
                    xalign 0.5
                    yalign 0.5

                    if (ri.discovered == 0):
                        auto ri.navicon
                    else:
                        auto "navic/navX_%s.png"
                    #take it away later
                    action [Hide("navscreen"),Hide("makeinteractables"),Function(localrmanref.checkroomevents,ri.idnum)]
            else:
                imagebutton:

                    xalign 0.5
                    yalign 0.5

                    if (ri.discovered == 0):
                        auto ri.navicon
                    else:
                        auto "navic/locksized_%s.png"
                    # auto "navic/navX_%s.png"
                    #take it away later
                    action [NullAction()]







screen invscreen(inventoryref,roommanagerref):


    modal False
    default localrmanref = roommanagerref
    default localinventoryref = inventoryref
    default itemstoshow = inventoryref.items




    imagebutton:
        xalign 0.5
        ypos 950
        auto "gamesys/BCK_%s.png"
        action [Hide("invscreen"),Function(localrmanref.changeinteractionlevel,0),Show("makeplayerUI",None,localrmanref)]

    #testing
    textbutton "No Item Selected":
        xalign 0.5
        ypos 900
        action NullAction()


    hbox:

        xalign 0.5
        ypos 800


        for gitem in itemstoshow:


            imagebutton:

                xalign 0.5
                yalign 0.5

                auto gitem.imageref

                #action [Hide("invscreen"),Function(localinventoryref.setactiveitem,gitem), Jump("dragdroplab")]

                action [Function(localinventoryref.setactiveitem,gitem),Show("invinterscreen",None,inventoryref,roommanagerref)]


                #alternate [Hide("invscreen"), Jump(gitem.description)]


screen invinterscreen(inventoryref,roommanagerref):

    default selitem = inventoryref.activeitem

    modal True

    imagebutton:
        xalign 0.5
        ypos 950
        auto "gamesys/BCK_%s.png"
        action [Hide("invinterscreen")]

    hbox:
        xalign 0.5
        yalign 0.7

        spacing 40

        frame:
            textbutton "Use" action [Hide("invinterscreen"), Hide("invscreen"),Jump("dragdroplab")]

        frame:
            textbutton "Examine" action [Hide("invinterscreen"),Jump(selitem.description)]


        

            


screen dragdropscreen(inventoryref,roommanagerref,itemtodrag):

    modal True


    default localinvenref = inventoryref
    default locitemtodrag =  itemtodrag
    default localrmanref = roommanagerref

    default interactablesonscreen = localrmanref.currentroom.interactablelist


    #transform other items into back button!!! (or use them to loop into this screen?) Account for count and relative position!


    imagebutton:
        xalign 0.5
        ypos 950
        auto "gamesys/BCK_%s.png"
        action [Hide("dragdropscreen"),Function(localrmanref.changeinteractionlevel,1),Show("invscreen",None,localinvenref,localrmanref)]

    #testing
    textbutton "Selected Item: use drag and drop":
        xalign 0.5
        ypos 900
        action NullAction()

    draggroup:

        drag:
            drag_name "[itemtodrag.name]"
            xalign 0.5
            ypos 800
            child itemtodrag.dragimg
            draggable True
            droppable False
            dragged dropcheck

        for intloc in interactablesonscreen:

            if (intloc.intertype != 3):

                drag:
                    drag_name intloc.name
                    xpos intloc.horposition
                    ypos intloc.verposition
                    child intloc.menuimageref
                    draggable False
                    droppable True











