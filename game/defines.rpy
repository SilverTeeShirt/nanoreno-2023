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
## Characters

define r = Character("Rookie", color="#bababa")
define s = Character("Sprocko", color="#aa16c4")
define m = Character("Marnie", color="#6064d1")
define o = Character("Captain Otus", color="#f7a512")
define g = Character("Gelato", color="#208211")
define ai = Character("The Caretaker", color="#80fff9")
define qq = Character("???", color="#666666")
define dd = Character(None, what_italic=True, what_font="font/NunitoSemiboldItalic.ttf") #Description

## Interactables self,name,intertype(IMAGE BUTTON SET to 1),horposition,verposition,interprogress,interrangequest[],interrangelayer[]#set to 0,fltext,labelref,imageref,menuimageref

#rm_0 cold sleep locker
define rm0_shower= ImageInteractable("Shower",1,1775,180,0,[0],[0],"","showerchoice",["inter/inter150x650_%s.png"],"inter150x650_idle.png")
define rm0_gloves= ImageInteractable("Gloves",1,1490,350,0,[0],[0],"","gloveslook",["inter/inter150x150_%s.png"],"inter150x150_idle.png")
define rm0_mirror= ImageInteractable("",1,1619,290,0,[0],[0],"","mirrorlook",["inter/inter150x300_%s.png"],"inter150x300_idle.png")
define rm0_shoe= ImageInteractable("",1,1300,715,0,[0],[0],"","shoe1look",["inter/inter150x150_%s.png"],"inter150x150_idle.png")
define rm0_locker1= ImageInteractable("",1,1200,333,0,[0],[0],"","locker1look",["inter/inter150x150_%s.png"],"inter150x150_idle.png")
define rm0_locker2= ImageInteractable("",1,740,333,0,[0],[0],"","locker2look",["inter/inter150x150_%s.png"],"inter150x150_idle.png")
define rm0_gastanks= ImageInteractable("",1,70,40,0,[0],[0],"","gastanklook",["inter/inter300x150_%s.png"],"inter300x150_idle.png")
define rm0_wires= ImageInteractable("",1,380,20,0,[0],[0],"","rm0_wireslook",["inter/inter300x150_%s.png"],"inter300x150_idle.png")
define rm0_window= ImageInteractable("",1,970,250,0,[0],[0],"","rm0_windowlook",["inter/inter150x300_%s.png"],"inter150x300_idle.png")
define rm0_wbutton= ImageInteractable("",1,1002,583,0,[0],[0],"","rm0_wbuttonlook",["inter/inter_%s.png"],"inter_idle.png")
define rm0_note= ImageInteractable("",1,440,430,0,[0],[0],"","rm0_noteslook",["inter/inter_%s.png"],"inter_idle.png")
define rm0_terminal= ImageInteractable("",1,10,650,0,[0],[0],"","rm0_terminallook",["inter/inter300x300_%s.png"],"inter300x300_idle.png")
define rm0_coldsleeppod= ImageInteractable("Cold Sleep pod",1,130,390,0,[0],[0],"","sleeppodlook",["inter/inter300x300_%s.png"],"inter300x300_idle.png")
define rm0_scrathes= ImageInteractable("",1,460,560,0,[0],[0],"","scrathesslook",["inter/inter150x300_%s.png"],"inter150x300_idle.png")

define rm0_NAVTEMP= ImageInteractable("",1,1700,950,0,[0],[0],"","NAVTEMP",["gamesys/NAV_%s.png"],"NAV_idle.png") #remove rooms navtemp when removing


#rm_1 bridge
define rm1_mainwindow= ImageInteractable("",1,1100,235,0,[0],[0],"","mainwindowlook",["inter/inter800x250_%s.png"],"inter800x250_idle.png")
define rm1_radiatortop= ImageInteractable("",1,200,660,0,[0],[0],"","radtoplook",["inter/inter300x150_%s.png"],"inter300x150_idle.png")
define rm1_radiatorbot= ImageInteractable("",1,195,910,0,[0],[0],"","radbotlook",["inter/inter300x150_%s.png"],"inter300x150_idle.png")
define rm1_navseat= ImageInteractable("",1,1090,500,0,[0],[0],"","navseatlook",["inter/inter300x300_%s.png"],"inter300x300_idle.png")
define rm1_capchair= ImageInteractable("",1,1430,650,0,[0],[0],"","capchairlook",["inter/inter300x300_%s.png"],"inter300x300_idle.png")
define rm1_capscreen= ImageInteractable("",1,1570,520,0,[0],[0],"","capscreenlook",["inter/inter300x150_%s.png"],"inter300x150_idle.png")
define rm1_idol= ImageInteractable("",1,1450,450,0,[0],[0],"","idollook",["inter/inter_%s.png"],"inter_idle.png")
define rm1_readout= ImageInteractable("",1,1425,580,0,[0],[0],"","rm1_readoutlook",["inter/inter_%s.png"],"inter_idle.png")
define rm1_mainscreen= ImageInteractable("",1,1760,140,0,[0],[0],"","rm1_mainscreenlook",["inter/inter150x150_%s.png"],"inter150x150_idle.png")
define rm1_vents= ImageInteractable("",1,170,320,0,[0],[0],"","rm1_ventslook",["inter/inter300x300_%s.png"],"inter300x300_idle.png")
define rm1_vbutton= ImageInteractable("",1,103,526,0,[0],[0],"","rm1_vbuttonlook",["inter/inter_%s.png"],"inter_idle.png")
define rm1_wires= ImageInteractable("",1,490,0,0,[0],[0],"","rm1_wireslook",["inter/inter300x300_%s.png"],"inter300x300_idle.png")
define rm1_datafood= ImageInteractable("",1,600,340,0,[0],[0],"","rm1_datafoodlook",["inter/inter150x300_%s.png"],"inter150x300_idle.png")


############## Rooms ##############
define RM0_coldsleeproom = Room("Cold Sleep Room TEST",0,"bg_ship1",[rm0_NAVTEMP,rm0_shower,rm0_gloves,rm0_coldsleeppod,rm0_mirror,rm0_shoe,rm0_locker1,rm0_locker2,rm0_gastanks,rm0_wires,rm0_window,rm0_wbutton,rm0_note,rm0_terminal,rm0_scrathes],0,0,[1],"bg_ship1")

define RM1_bridge = Room("Bridge TEST",1,"bg_ship2",[rm1_mainwindow,rm1_radiatortop,rm1_radiatorbot,rm1_navseat,rm1_capchair,rm1_capscreen,rm1_idol,rm1_readout,rm1_mainscreen,rm1_vents,rm1_vbutton,rm1_wires,rm1_datafood],0,0,[0],"bg_ship2")




## Roommanager (and Inventory soon)
define roommanager = RoomManager("roommanager",[RM0_coldsleeproom,RM1_bridge],RM0_coldsleeproom,1,1,1)
