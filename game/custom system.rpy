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



    class RoomManager():
        def __init__(self,name,rooms,currentroom,currinterlayer,gotnav,gotinv):
            self.name = name
            self.rooms = rooms
            self.currentroom = currentroom
            self.currinterlayer = currinterlayer
            self.gotnav = gotnav
            self.gotinv = gotinv

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
            #renpy.with_statement(fade)
            cr.discovered = 0
            self.setupinterforroom(cr)
            self.changeinteractionlevel(0)
            self.setupplayerUI()


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
        def __init__(self,name,intertype,horposition,verposition,interprogress,interrangequest,interrangelayer,fltext,labelref,imageref,menuimageref,characode):
            super().__init__(name,intertype,horposition,verposition,interprogress,interrangelayer,interrangequest,fltext,labelref)
            self.imageref = imageref
            self.menuimageref = menuimageref
            self.characode = characode


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


    class Item():
        def __init__(self,name,idnum,imageref,description,targetinter,solutionlab,dragimg,comments):
            self.name = name
            self.idnum = idnum
            self.imageref = imageref
            self.description = description
            self.targetinter = targetinter
            self.solutionlab = solutionlab
            self.dragimg = dragimg
            self.comments = comments

        def interpretoutcome(self,outcomeval,rmman):
            if outcomeval == 0:
                renpy.jump(self.solutionlab)
            
            if outcomeval == 6:
                rmman.returnfrominteraction(rmman.currentroom)

            if outcomeval == 1:
                renpy.jump(self.comments[0])
            
            if outcomeval ==2:
                renpy.jump(self.comments[1])

            if outcomeval ==3:
                renpy.jump(self.comments[2])
            
            if outcomeval ==4:
                renpy.jump(self.comments[3])
            
            if outcomeval ==5:
                renpy.jump(self.comments[4])


    def dropcheckcorr(drags,drop):

        store.dropoutcome = 0

        return True
    
    def dropcheckwrong(drags,drop):

        store.dropoutcome = 6

        return True
    
    def dropchecksp(drags,drop):

        store.dropoutcome = 1;

        return True

    def dropcheckmar(drags,drop):

        store.dropoutcome = 2;

        return True
    
    def dropcheckot(drags,drop):

        store.dropoutcome = 3;

        return True
    
    def dropcheckgel(drags,drop):

        store.dropoutcome = 4;

        return True

    def dropcheckai(drags,drop):

        store.dropoutcome = 5;

        return True





label dragdroplab:

    default dropoutcome = 99

    call screen dragdropscreen(inventory,roommanager,inventory.activeitem)

    $inventory.activeitem.interpretoutcome(dropoutcome,roommanager)






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
            action [SensitiveIf(localrmanref.currinterlayer == 0), Hide("makeplayerUI"), Show("navscreen",None,localrmanref)]

    if (localrmanref.gotinv == 0):
        imagebutton:
            xpos 775
            ypos 950
            auto "gamesys/INV_%s.png"
            action [SensitiveIf(localrmanref.currinterlayer == 0), Hide("makeplayerUI"),Function(localrmanref.changeinteractionlevel,1),Show("invscreen",None,localinvenref,localrmanref)]





screen navscreen(roommanagerref):

    modal True
    default localrmanref = roommanagerref
    default roomstogoto = []
    default count = 0

    for rtg in localrmanref.currentroom.adjacentrooms:
        $ roomstogoto.append(localrmanref.rooms[rtg])


    imagebutton:
            xpos 885
            ypos 950
            auto "gamesys/BCK_%s.png"
            action [Hide("navscreen"),Show("makeplayerUI",None,localrmanref)]


    for ri in roomstogoto:


        if (ri.locked == 0):

            imagebutton:
                xalign (0.2 + (0.15*count))
                yalign 0.5

                #if (ri.discovered == 0):
                    #auto ri.navicon
                #else:
                    #auto "iconunknown_%s.jpg"
                auto "navic/iconunknown_%s.jpg"
                #take it away later
                action [Hide("navscreen"),Hide("makeinteractables"),Function(localrmanref.checkroomevents,ri.idnum)]
        else:

            imagebutton:

                xalign 0.5
                yalign (0.2 + (0.2*count))

                #if (ri.discovered == 0):
                    #auto ri.navicon
                #else:
                    #auto "iconunknown_%s.jpg"
                auto "iconunknown_%s.jpg"
                #take it away later
                action [NullAction()]

            image "iconlocked.jpg" xalign 0.6 yalign (0.2 + (0.2*count))

        $ count += 1




screen invscreen(inventoryref,roommanagerref):


    modal False
    default localrmanref = roommanagerref
    default localinventoryref = inventoryref
    default itemstoshow = []
    #default interactablesonscreen = localrmanref.currentroom.interactablelist
    default count = 0


    imagebutton:
        xpos 885
        ypos 950
        auto "gamesys/BCK_%s.png"
        action [Hide("invscreen"),Function(localrmanref.changeinteractionlevel,0),Show("makeplayerUI",None,localrmanref)]


    for it in inventoryref.items:

        $itemstoshow.append(it)



    for gitem in itemstoshow:


        imagebutton:

            xpos (400 + (250*count))
            ypos 950

            auto gitem.imageref

            action [Hide("invscreen"),Function(localinventoryref.setactiveitem,gitem), Jump("dragdroplab")]

            alternate [Hide("invscreen"), Show("itemdescscreen",None,gitem.description,localinventoryref,localrmanref)]

        $ count += 1


screen dragdropscreen(inventoryref,roommanagerref,itemtodrag):

    modal True

    default localinvenref = inventoryref
    default locitemtodrag =  itemtodrag
    default localrmanref = roommanagerref

    default interactablesonscreen = localrmanref.currentroom.interactablelist


    #transform other items into back button!!! (or use them to loop into this screen?) Account for count and relative position!


    imagebutton:
        xpos 885
        ypos 950
        auto "gamesys/BCK_%s.png"
        action [Hide("dragdropscreen"),Function(localrmanref.changeinteractionlevel,1),Show("invscreen",None,localinvenref,localrmanref)]

    draggroup:

        drag:
            drag_name "[itemtodrag.name]"
            xpos 400
            ypos 950
            child itemtodrag.dragimg
            draggable True
            droppable False

        for intloc in interactablesonscreen:

            if (intloc.intertype != 3):

                if (intloc.name == locitemtodrag.targetinter):

                    drag:
                        drag_name "[intloc.name]"
                        xpos intloc.horposition
                        ypos intloc.verposition
                        child intloc.menuimageref
                        draggable False
                        droppable True
                        dropped dropcheckcorr
                else:
                    if (intloc.characode == 0):
                        drag:
                            drag_name "[intloc.name]"
                            xpos intloc.horposition
                            ypos intloc.verposition
                            child intloc.menuimageref
                            draggable False
                            droppable True
                            dropped dropcheckwrong

                    if (intloc.characode == 1):
                        drag:
                            drag_name "[intloc.name]"
                            xpos intloc.horposition
                            ypos intloc.verposition
                            child intloc.menuimageref
                            draggable False
                            droppable True
                            dropped dropchecksp
                
                    if (intloc.characode == 2):
                        drag:
                            drag_name "[intloc.name]"
                            xpos intloc.horposition
                            ypos intloc.verposition
                            child intloc.menuimageref
                            draggable False
                            droppable True
                            dropped dropcheckmar

                    if (intloc.characode == 3):
                        drag:
                            drag_name "[intloc.name]"
                            xpos intloc.horposition
                            ypos intloc.verposition
                            child intloc.menuimageref
                            draggable False
                            droppable True
                            dropped dropcheckot

                    if (intloc.characode == 4):
                        drag:
                            drag_name "[intloc.name]"
                            xpos intloc.horposition
                            ypos intloc.verposition
                            child intloc.menuimageref
                            draggable False
                            droppable True
                            dropped dropcheckgel
                
                    if (intloc.characode == 5):
                        drag:
                            drag_name "[intloc.name]"
                            xpos intloc.horposition
                            ypos intloc.verposition
                            child intloc.menuimageref
                            draggable False
                            droppable True
                            dropped dropcheckai






screen itemdescscreen(itemdesc, inventoryref, roommanagerref):

    modal True

    default localrmanref = roommanagerref
    default inventoryreference = inventoryref

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 30
        textbutton "[itemdesc]" action [Hide("itemdescscreen"), Show("invscreen",None, inventoryreference, localrmanref)]
