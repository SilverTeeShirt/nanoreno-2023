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
define rm0_shower= ImageInteractable("Shower",1,1775,180,0,[0],[0],"","showerlook",["inter/inter150x650_%s.png"],"inter150x650_idle.png")
define rm0_gloves= ImageInteractable("Gloves",1,1490,350,0,[0],[0],"","gloveslook",["inter/inter150x150_%s.png"],"inter150x150_idle.png")
define rm0_mirror= ImageInteractable("",1,1619,290,0,[0],[0],"","mirrorlook",["inter/inter150x300_%s.png"],"inter150x300_idle.png")
define rm0_shoe= ImageInteractable("",1,1300,715,0,[0],[0],"","shoe1look",["inter/inter150x150_%s.png","inter/inter150x150_%s.png"],"inter150x150_idle.png")
define rm0_locker1= ImageInteractable("Locker",1,1200,333,0,[0],[0],"","locker1look",["inter/inter150x150_%s.png"],"inter150x150_idle.png")
define rm0_locker2= ImageInteractable("",1,740,333,0,[0],[0],"","locker2look",["inter/inter150x150_%s.png"],"inter150x150_idle.png")
define rm0_gastanks= ImageInteractable("",1,70,40,0,[0],[0],"","gastanklook",["inter/inter300x150_%s.png"],"inter300x150_idle.png")
define rm0_wires= ImageInteractable("",1,380,20,0,[0],[0],"","rm0_wireslook",["inter/inter300x150_%s.png"],"inter300x150_idle.png")
define rm0_window= ImageInteractable("",1,970,250,0,[0],[0],"","rm0_windowlook",["inter/inter150x300_%s.png"],"inter150x300_idle.png")
define rm0_wbutton= ImageInteractable("",1,1002,583,0,[0],[0],"","rm0_wbuttonlook",["inter/inter_%s.png"],"inter_idle.png")
define rm0_note= ImageInteractable("",1,440,430,0,[0],[0],"","rm0_noteslook",["inter/inter_%s.png"],"inter_idle.png")
define rm0_terminal= ImageInteractable("",1,10,650,0,[0],[0],"","rm0_terminallook",["inter/inter300x300_%s.png"],"inter300x300_idle.png")
define rm0_coldsleeppod= ImageInteractable("Cold Sleep pod",1,130,390,0,[0],[0],"","sleeppodlook",["inter/inter300x300_%s.png"],"inter300x300_idle.png")
define rm0_scrathes= ImageInteractable("",1,460,560,0,[0],[0],"","scrathesslook",["inter/inter150x300_%s.png"],"inter150x300_idle.png")
#define rm0_NAVTEMP= ImageInteractable("",1,1700,950,0,[0],[0],"","NAVTEMP",["gamesys/NAV_%s.png"],"NAV_idle.png") #remove rooms navtemp when removing

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

#rm_2 hub
define skyart= ImageInteractable("",1,510,80,0,[0],[0],"","skyartlook",["inter/inter800x250_%s.png"],"inter800x250_idle.png")
define rm2_trash= ImageInteractable("",1,1350,900,0,[0],[0],"","rm2_trashlook",["inter/inter300x150_%s.png"],"inter300x150_idle.png")
define rm2_table= ImageInteractable("",1,1520,720,0,[0],[0],"","rm2_tablelook",["inter/inter150x150_%s.png"],"inter150x150_idle.png")
define charger= ImageInteractable("",1,1740,610,0,[0],[0],"","chargerlook",["inter/inter150x300_%s.png"],"inter150x300_idle.png")
define rm2_door1= ImageInteractable("",1,1550,360,0,[0],[0],"","rm2_doorlook",["inter/inter300x150_%s.png"],"inter300x150_idle.png")
define rm2_door2= ImageInteractable("",1,80,360,0,[0],[0],"","rm2_doorlook",["inter/inter300x150_%s.png"],"inter300x150_idle.png")
define logo= ImageInteractable("",1,885,350,0,[0],[0],"","logolook",["inter/inter150x300_%s.png"],"inter150x300_idle.png")
define rm2_elevator= ImageInteractable("",1,810,670,0,[0],[0],"","rm2_elevatorlook",["inter/inter300x300_%s.png"],"inter300x300_idle.png")
define rm2_light1= ImageInteractable("",1,710,720,0,[0],[0],"","rm2_lightlook",["inter/inter_%s.png"],"inter_idle.png")
define rm2_light2= ImageInteractable("",1,1128,720,0,[0],[0],"","rm2_lightlook",["inter/inter_%s.png"],"inter_idle.png")
define rm2_bigdoor= ImageInteractable("",1,0,650,0,[0],[0],"","rm2_bigdoorlook",["inter/inter300x300_%s.png"],"inter300x300_idle.png")
define planetmodel= ImageInteractable("",1,1355,160,0,[0],[0],"","planetmodellook",["inter/inter150x150_%s.png"],"inter150x150_idle.png")
define powermail= ImageInteractable("",1,350,775,0,[0],[0],"","powermaillook",["inter/inter150x150_%s.png"],"inter150x150_idle.png")

define marnie_rm2= ImageInteractable("",1,540,690,0,[0],[0],"","marnietalk",["inter/talk/marnie1_%s.png"],"marnie1_idle.png")
define sprocko_rm2= ImageInteractable("",1,250,740,0,[0],[0],"","sprockotalk",["inter/talk/sprocko1_%s.png"],"sprocko1_idle.png")
define gelato_rm2= ImageInteractable("",1,1150,450,0,[0],[0],"","gelatotalk",["inter/talk/gelato1_%s.png"],"gelato1_idle.png")
define otus_rm2= ImageInteractable("",1,1100,650,0,[0],[0],"","otustalk",["inter/talk/otus1_%s.png"],"otus1_idle.png")
define ai_rm2= ImageInteractable("",1,1700,685,0,[0],[0],"","aitalk",["inter/talk/ai1_%s.png"],"ai1_idle.png")

#rm_3 lab
# define skyart= ImageInteractable("",1,510,80,0,[0],[0],"","skyartlook",["inter/inter800x250_%s.png"],"inter800x250_idle.png")

#rm_4 con
define hangingplants= ImageInteractable("",1,620,30,0,[0],[0],"","hangingplantslook",["inter/inter800x250_%s.png"],"inter800x250_idle.png")

#rm_5 bar
# define skyart= ImageInteractable("",1,510,80,0,[0],[0],"","skyartlook",["inter/inter800x250_%s.png"],"inter800x250_idle.png")

#rm_6 core
# define skyart= ImageInteractable("",1,510,80,0,[0],[0],"","skyartlook",["inter/inter800x250_%s.png"],"inter800x250_idle.png")


############## Rooms ##############
define RM0_coldsleeproom = Room("Cold TEST",0,"bg_0cold_room",[rm0_shower,rm0_gloves,rm0_mirror,rm0_shoe,rm0_locker1,rm0_locker2,rm0_gastanks,rm0_wires,rm0_window,rm0_wbutton,rm0_note,rm0_terminal,rm0_coldsleeppod,rm0_scrathes],0,0,[1],"bg_0cold_room",[])

define RM1_bridge = Room("Bridge TEST",1,"bg_1bridge_room",[rm1_mainwindow,rm1_radiatortop,rm1_radiatorbot,rm1_navseat,rm1_capchair,rm1_capscreen,rm1_idol,rm1_readout,rm1_mainscreen,rm1_vents,rm1_vbutton,rm1_wires,rm1_datafood],0,0,[0,2],"bg_1bridge_room",[])

define RM2_hub = Room("Hub TEST",2,"bg_2hub_room",[skyart,rm2_trash,rm2_table,charger,rm2_door1,rm2_door2,logo,rm2_elevator,rm2_light1,rm2_light2,rm2_bigdoor,planetmodel,powermail,marnie_rm2,sprocko_rm2,gelato_rm2,otus_rm2,ai_rm2],0,0,[1,3,4,5,6],"bg_2hub_room",[])

define RM3_lab = Room("Lab TEST",3,"bg_3lab_room",[],0,0,[2,4,5],"bg_3lab_room",[])

define RM4_con = Room("Conservatory TEST",4,"bg_4con_room",[hangingplants],0,0,[2,3,5],"bg_4con_room",[])

define RM5_bar = Room("Bar TEST",5,"bg_5bar_room",[],0,0,[2,3,4],"bg_5bar_room",[])

define RM6_core = Room("Core TEST",6,"bg_6core_room",[],0,0,[2],"bg_6core_room",[])


#####items######
define lockerkey = Item("Small Key",0,"item/item_key1.png","A small key found in a sock. Too small to be a door's key, and besides, we use magnetic locks", "Locker")

## Roommanager (and Inventory soon)
define roommanager = RoomManager("roommanager",[RM0_coldsleeproom,RM1_bridge,RM2_hub,RM3_lab,RM4_con,RM5_bar,RM6_core],RM0_coldsleeproom,1,0,0)

define inventory = Inventory([])
