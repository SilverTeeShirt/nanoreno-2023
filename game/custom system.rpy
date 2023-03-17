############## ROOM MANAGER PYTON ##############
init offset = -2
init python:

    class Room():
        def __init__(self,name,idnum,bgref,interactablelist,discovered,locked,adjacentrooms,navicon):
            self.name = name
            self.idnum = idnum
            self.bgref = bgref
            self.interactablelist = interactablelist
            self.discovered = discovered
            self.locked = locked
            self.adjacentrooms = adjacentrooms
            self.navicon = navicon



    class RoomManager():
        def __init__(self,name,rooms,currentroom,currinterlayer,gotnav,gotinv):
            self.name = name
            self.rooms = rooms
            self.currentroom = currentroom
            self.currinterlayer = currinterlayer
            self.gotnav = gotnav
            self.gotinv = gotinv


        def setuproom(self,idnum):
            self.currentroom = self.rooms[idnum]
            self.currinterlayer = 1
            cr = self.currentroom
            renpy.scene()
            renpy.show(cr.bgref)
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
            self.textref = textref;
            self.xpad = xpad;
            self.ypad = ypad;


############## ROOM MANAGER ##############
############## ROOM MANAGER ##############
############## ROOM MANAGER ##############


label uisetup:
    call screen makeplayerUI(roommanager)



screen makeinteractables(targetinteractables, roommanagerref):

    default localrmanref = roommanagerref


    for ti in targetinteractables:
        if ti.intertype == 1:
            imagebutton:
                xpos ti.horposition
                ypos ti.verposition
                auto ti.imageref[ti.interprogress]
                action [SensitiveIf((ti.interprogress in ti.interrangequest)and(localrmanref.currinterlayer == 0)), Hide("makeinteractables"), Hide("makeplayerUI"), Function(localrmanref.intiateinteraction,ti.labelref)]


        elif ti.intertype == 2:
            frame:
                xpos ti.horposition
                ypos ti.verposition
                xpadding ti.xpad
                ypadding ti.ypad
                textbutton ti.textref  action NullAction()


screen interactableinteractionscreen(selectedinteractable):

    default localinterref = selectedinteractable
    image "[localinterref.menuimageref]" xalign 0.3 yalign 0.5



screen makeplayerUI(roommanagerref):

    default localrmanref = roommanagerref


    if (localrmanref.gotnav == 0):
        frame:
            xpadding 40
            ypadding 20
            xalign 0.9
            yalign 0.1
            textbutton "Navigation" action [SensitiveIf(localrmanref.currinterlayer == 0), Hide("makeplayerUI"), Show("navscreen",None,localrmanref)]

    if (localrmanref.gotinv == 0):
        frame:
            xpadding 40
            ypadding 20
            xalign 0.9
            yalign 0.2
            textbutton "Inventory" action NullAction()



screen navscreen(roommanagerref):

    modal True
    default localrmanref = roommanagerref
    default roomstogoto = []
    default count = 0

    for rtg in localrmanref.currentroom.adjacentrooms:
        $ roomstogoto.append(localrmanref.rooms[rtg])


    frame:
        xpadding 40
        ypadding 20
        xalign 0.9
        yalign 0.1
        textbutton "Back" action [Hide("navscreen"),Show("makeplayerUI",None,localrmanref)]


    for ri in roomstogoto:


        if (ri.locked == 0):

            imagebutton:
                xalign 0.5
                yalign (0.2 + (0.2*count))

                if (ri.discovered == 0):
                    auto ri.navicon
                else:
                    auto "iconunknown_%s.jpg"
                action [Hide(),Function(localrmanref.setuproom,ri.idnum)]
        else:

            imagebutton:

                xalign 0.5
                yalign (0.2 + (0.2*count))

                if (ri.discovered == 0):
                    auto ri.navicon
                else:
                    auto "iconunknown_%s.jpg"

                action [NullAction()]

            image "iconlocked.jpg" xalign 0.6 yalign (0.2 + (0.2*count))

        $ count += 1
