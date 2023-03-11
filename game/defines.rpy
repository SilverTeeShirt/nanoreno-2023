#Python methods, move later

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
            renpy.show_screen("makeinteractables",cr.interactablelist,self)
            renpy.jump("enterroom")

        def changeinteractionlevel(self,newilv):
        
            self.currinterlayer = newilv

        
        def intiateinteraction(self,selinterjump):
            
            
            #renpy.show_screen("interactableinteractionscreen",selinter)

            renpy.jump(selinterjump)
    


           
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



## Defines
## Characters Chapter 0

define r = Character("Rookie", color="#bababa")

define s = Character("Sprocko", color="#aa16c4")
define m = Character("Marnie", color="#6064d1")
define o = Character("Captain Otus", color="#b0ad82")
define g = Character("Gelato", color="#208211")

define ai = Character("The Caretaker", color="#ffb73b")

define qq = Character("???", color="#666666")
define dd = Character(None, what_style="centered_text", what_italic=True)


## Interactables
define showerdoorintro = ImageInteractable("Cold sleep room",1,1836,524,0,[0],[0],"","showerchoice",["inter/testinteractable_%s.png"],"testinteractable_idle.png")

## Rooms

# Chapter 0
define coldsleeproom = Room("Cold sleep room",0,"bg_ship1",[showerdoorintro],0,0,[],"bg_ship1")



## Roommanager (and Inventory soon)
define roommanager = RoomManager("roommanager",[coldsleeproom],coldsleeproom,1,1,1)





