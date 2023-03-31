## Defines
## Characters

define r = Character("Rookie", color="#ffffff")
define s = Character("Sprocko", color="#9d50b4") #characode 1
define m = Character("Marnie", color="#5b66b7") #characode 2
define o = Character("Captain Otus", color="#ff8518") #characode 3
define g = Character("Gelato", color="#006e21") #characode 4
define ai = Character("The Caretaker", color="#00f0ff") #characode 5
define aie = Character("The Founder", color="#ff0000") #characode 5
define qq = Character("???", color="#8888887f")
define dd = Character(None, what_italic=True, what_font="font/NunitoSemiboldItalic.ttf") #Description
define item = Character(None, what_italic=True, what_style="centered_text", what_font="font/NunitoSemiboldItalic.ttf", what_size = 36) #Description

## Interactables self,name,intertype(IMAGE BUTTON SET to 1),horposition,verposition,interprogress,interrangequest[],interrangelayer[]#set to 0,fltext,labelref,imageref,menuimageref

###################rm_0 cold sleep locker
define rm0_shower= ImageInteractable("",1,1775,180,0,[0],[0],"","showerlook","inter/inter150x650_%s.png","inter/inter150x650_idle.png",0)
define rm0_gloves= ImageInteractable("",1,1490,350,0,[0],[0],"","gloveslook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define rm0_mirror= ImageInteractable("",1,1619,290,0,[0],[0],"","mirrorlook","inter/inter150x300_%s.png","inter/inter150x300_idle.png",0)
define rm0_shoe= ImageInteractable("",1,1300,715,0,[0],[0],"","shoe1look","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define rm0_locker1= ImageInteractable("locker1",1,1200,333,0,[0],[0],"","locker1look","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define rm0_locker2= ImageInteractable("",1,740,333,0,[0],[0],"","locker2look","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define rm0_gastanks= ImageInteractable("",1,70,40,0,[0],[0],"","gastanklook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm0_wires= ImageInteractable("",1,380,20,0,[0],[0],"","rm0_wireslook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm0_window= ImageInteractable("",1,970,250,0,[0],[0],"","rm0_windowlook","inter/inter150x300_%s.png","inter/inter150x300_idle.png",0)
define rm0_wbutton= ImageInteractable("",1,1002,583,0,[0],[0],"","rm0_wbuttonlook","inter/inter_%s.png","inter/inter_idle.png",0)
define rm0_note= ImageInteractable("",1,440,430,0,[0],[0],"","rm0_noteslook","inter/inter_%s.png","inter/inter_idle.png",0)
define rm0_terminal= ImageInteractable("",1,10,650,0,[0],[0],"","rm0_terminallook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm0_coldsleeppod= ImageInteractable("",1,130,390,0,[0],[0],"","sleeppodlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm0_scrathes= ImageInteractable("",1,460,560,0,[0],[0],"","scrathesslook","inter/inter150x300_%s.png","inter/inter150x300_idle.png",0)

###################rm_1 bridge
define rm1_mainwindow= ImageInteractable("",1,1100,235,0,[0],[0],"","mainwindowlook","inter/inter800x250_%s.png","inter/inter800x250_idle.png",0)
define rm1_radiatortop= ImageInteractable("",1,200,660,0,[0],[0],"","radtoplook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm1_radiatorbot= ImageInteractable("",1,195,910,0,[0],[0],"","radbotlook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm1_navseat= ImageInteractable("",1,1090,500,0,[0],[0],"","navseatlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm1_capchair= ImageInteractable("",1,1430,650,0,[0],[0],"","capchairlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm1_capscreen= ImageInteractable("",1,1570,520,0,[0],[0],"","capscreenlook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm1_idol= ImageInteractable("",1,1450,450,0,[0],[0],"","idollook","inter/inter_%s.png","inter/inter_idle.png",0)
define rm1_readout= ImageInteractable("",1,1425,580,0,[0],[0],"","rm1_readoutlook","inter/inter_%s.png","inter/inter_idle.png",0)
define rm1_mainscreen= ImageInteractable("",1,1760,140,0,[0],[0],"","rm1_mainscreenlook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define rm1_vents= ImageInteractable("",1,170,320,0,[0],[0],"","rm1_ventslook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm1_vbutton= ImageInteractable("",1,103,526,0,[0],[0],"","rm1_vbuttonlook","inter/inter_%s.png","inter/inter_idle.png",0)
define rm1_wires= ImageInteractable("",1,490,0,0,[0],[0],"","rm1_wireslook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm1_datafood= ImageInteractable("",1,600,340,0,[0],[0],"","rm1_datafoodlook","inter/inter150x300_%s.png","inter/inter150x300_idle.png",0)

###################rm_2 hub
define skyart= ImageInteractable("",1,510,80,0,[0],[0],"","skyartlook","inter/inter800x250_%s.png","inter/inter800x250_idle.png",0)
define rm2_trash= ImageInteractable("",1,1370,870,0,[0],[0],"","rm2_trashlook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm2_table= ImageInteractable("",1,1518,720,0,[0],[0],"","rm2_tablelook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define charger= ImageInteractable("",1,1745,610,0,[0],[0],"","chargerlook","inter/inter150x300_%s.png","inter/inter150x300_idle.png",0)
define rm2_door1= ImageInteractable("",1,1550,360,0,[0],[0],"","rm2_doorlook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm2_door2= ImageInteractable("",1,80,360,0,[0],[0],"","rm2_doorlook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define logo= ImageInteractable("",1,885,350,0,[0],[0],"","logolook","inter/inter150x300_%s.png","inter/inter150x300_idle.png",0)
define rm2_elevator= ImageInteractable("",1,810,670,0,[0],[0],"","rm2_elevatorlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm2_light1= ImageInteractable("",1,710,720,0,[0],[0],"","rm2_lightlook","inter/inter_%s.png","inter/inter_idle.png",0)
define rm2_light2= ImageInteractable("",3,1128,720,0,[0],[0],"","rm2_lightlook","inter/inter_%s.png","inter/inter_idle.png",0)
define rm2_bigdoor= ImageInteractable("",1,0,650,0,[0],[0],"","rm2_bigdoorlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define planetmodel= ImageInteractable("",1,1355,160,0,[0],[0],"","planetmodellook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define powermail= ImageInteractable("",1,350,775,0,[0],[0],"","powermaillook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)

define marnie_rm2= ImageInteractable("",1,545,680,0,[0],[0],"","marnietalk","inter/talk/marnie1_%s.png","inter/talk/marnie1_idle.png",2)
define sprocko_rm2= ImageInteractable("",1,230,735,0,[0],[0],"","sprockotalk","inter/talk/sprocko1_%s.png","inter/talk/sprocko1_idle.png",1)
define gelato_rm2= ImageInteractable("Gelato",1,1140,447,0,[0],[0],"","gelatotalk","inter/talk/gelato1_%s.png","inter/talk/gelato1_idle.png",4)
define otus_rm2= ImageInteractable("",1,1150,615,0,[0],[0],"","otustalk","inter/talk/otus1_%s.png","inter/talk/otus1_idle.png",3)
define ai_rm2= ImageInteractable("",3,1645,675,0,[0],[0],"","aitalk","inter/talk/ai1_%s.png","inter/talk/ai1_idle.png",5)

###################rm_3 lab
define rm3_ceiling= ImageInteractable("",1,650,25,0,[0],[0],"","rm3_ceilinglook","inter/inter800x250_%s.png","inter/inter800x250_idle.png",0)
define rm3_window= ImageInteractable("",1,840,350,0,[0],[0],"","rm3_windowlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define partshead= ImageInteractable("",1,380,680,0,[0],[0],"","partsheadlook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define partsarm= ImageInteractable("",1,80,790,0,[0],[0],"","partsarmlook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define raydish= ImageInteractable("",1,150,100,0,[0],[0],"","raydishlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define constructor= ImageInteractable("",1,90,490,0,[0],[0],"","constructorlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define fluidtanks= ImageInteractable("",1,613,420,0,[0],[0],"","fluidtankslook","inter/inter150x300_%s.png","inter/inter150x300_idle.png",0)
define biodevice= ImageInteractable("",1,745,550,0,[0],[0],"","biodevicelook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define rm3_datapad= ImageInteractable("",1,1028,650,0,[0],[0],"","rm3_datapadlook","inter/inter_%s.png","inter/inter_idle.png",0)
define rm3_safe= ImageInteractable("",1,745,765,0,[0],[0],"","rm3_safelook","inter/inter_%s.png","inter/inter_idle.png",0)
define rm3_computer= ImageInteractable("",1,1300,400,0,[0],[0],"","rm3_computerlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define chembank1= ImageInteractable("",1,1470,190,0,[0],[0],"","chembanklook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define chembank2= ImageInteractable("",1,1650,290,0,[0],[0],"","chembanklook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define chembank3= ImageInteractable("",1,1610,518,0,[0],[0],"","chembanklook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)

define sprocko_rm3= ImageInteractable("",3,1120,475,0,[0],[0],"","sprockotalk","inter/talk/sprocko2_%s.png","inter/talk/sprocko2_idle.png",1)


###################rm_4 conservatory
define hangingplants= ImageInteractable("",1,620,30,0,[0],[0],"","hangingplantslook","inter/inter800x250_%s.png","inter/inter800x250_idle.png",0)
define garden= ImageInteractable("",1,-100,550,0,[0],[0],"","gardenlook","inter/inter800x250_%s.png","inter/inter800x250_idle.png",0)
define scarecrow= ImageInteractable("",1,50,300,0,[0],[0],"","scarecrowlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define watertank= ImageInteractable("",1,390,90,0,[0],[0],"","watertanklook","inter/inter150x300_%s.png","inter/inter150x300_idle.png",0)
define rm4_stair= ImageInteractable("",1,1750,275,0,[0],[0],"","rm4_stairlook","inter/inter150x650_%s.png","inter/inter150x650_idle.png",0)
define rm4_panels= ImageInteractable("",1,930,265,0,[0],[0],"","rm4_panelslook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define pumpdoor= ImageInteractable("",1,930,535,0,[0],[0],"","pumpdoorlook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define pumps= ImageInteractable("",1,660,475,0,[0],[0],"","pumpslook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm4_light= ImageInteractable("",1,415,407,0,[0],[0],"","rm4_lightlook","inter/inter_%s.png","inter/inter_idle.png",0)
define forest= ImageInteractable("",1,1410,490,0,[0],[0],"","forestlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define colorfulflower= ImageInteractable("",1,1520,50,0,[0],[0],"","colorfulflowerlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define bird= ImageInteractable("",1,525,705,0,[0],[0],"","birdlook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)

define marnie_rm4= ImageInteractable("",3,1180,550,0,[0],[0],"","marnietalk","inter/talk/marnie2_%s.png","inter/talk/marnie2_idle.png",2)

###################rm_5 bar
define booth= ImageInteractable("",1,0,545,0,[0],[0],"","boothlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define plantmonster= ImageInteractable("",1,295,110,0,[0],[0],"","plantmonsterlook","inter/inter150x650_%s.png","inter/inter150x650_idle.png",0)
define paintings= ImageInteractable("",1,300,10,0,[0],[0],"","paintingslook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define eyetree= ImageInteractable("",1,5,20,0,[0],[0],"","eyetreelook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define moose= ImageInteractable("",1,690,130,0,[0],[0],"","mooselook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define harpoon= ImageInteractable("",1,710,0,0,[0],[0],"","harpoonlook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define bonemonster= ImageInteractable("",1,1100,30,0,[0],[0],"","bonemonsterlook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define bughead= ImageInteractable("",1,1525,210,0,[0],[0],"","bugheadlook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define rm5_tubes= ImageInteractable("",1,1580,30,0,[0],[0],"","rm5_tubeslook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define drinkmaker= ImageInteractable("",1,1240,400,0,[0],[0],"","drinkmakerlook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define drinks1= ImageInteractable("",1,1050,400,0,[0],[0],"","drinkslook","inter/inter150x150_%s.png","inter/inter150x150_idle.png",0)
define drinks2= ImageInteractable("",1,1450,435,0,[0],[0],"","drinkslook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm5_datapad= ImageInteractable("",1,1390,555,0,[0],[0],"","rm5_datapadlook","inter/inter_%s.png","inter/inter_idle.png",0)

define gelato_rm5= ImageInteractable("Gelato",3,440,140,0,[0],[0],"","gelatotalk","inter/talk/gelato2_%s.png","inter/talk/gelato2_idle.png",4)


###################rm_6 reactor core
define memento= ImageInteractable("",1,1685,540,0,[0],[0],"","mementolook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm6_door= ImageInteractable("",1,1525,30,0,[0],[0],"","rm6_doorlook","inter/inter150x650_%s.png","inter/inter150x650_idle.png",0)
define jarbot= ImageInteractable("",1,0,670,0,[0],[0],"","jarlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define jartop= ImageInteractable("",1,-35,100,0,[0],[0],"","jarlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define jarman= ImageInteractable("",1,-25,360,0,[0],[0],"","jarmanlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm6_computer= ImageInteractable("",1,300,450,0,[0],[0],"","rm6_computerlook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define deadguy= ImageInteractable("",1,900,750,0,[0],[0],"","deadguylook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm6_rcore= ImageInteractable("",1,810,200,0,[0],[0],"","rm6_rcorelook","inter/inter300x300_%s.png","inter/inter300x300_idle.png",0)
define rm6_points1= ImageInteractable("",1,300,90,0,[0],[0],"","rm6_pointslook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm6_points2= ImageInteractable("",1,1150,190,0,[0],[0],"","rm6_pointslook","inter/inter300x150_%s.png","inter/inter300x150_idle.png",0)
define rm6_datapad= ImageInteractable("",1,690,860,0,[0],[0],"","rm6_datapadlook","inter/inter_%s.png","inter/inter_idle.png",0)

define otus_rm6= ImageInteractable("",3,1142,295,0,[0],[0],"","otustalk","inter/talk/otus2_%s.png","inter/talk/otus2_idle.png",3)


############## Rooms ##############
############## Rooms ##############
define RM0_cold = Room("Cold TEST",0,"bg_0cold_room",[rm0_shower,rm0_gloves,rm0_mirror,rm0_shoe,rm0_locker1,rm0_locker2,rm0_gastanks,rm0_wires,rm0_window,rm0_wbutton,rm0_note,rm0_terminal,rm0_coldsleeppod,rm0_scrathes],0,0,[1],"bg_0cold_room",[])
define RM1_bridge = Room("Bridge TEST",1,"bg_1bridge_room",[rm1_mainwindow,rm1_radiatortop,rm1_radiatorbot,rm1_navseat,rm1_capchair,rm1_capscreen,rm1_idol,rm1_readout,rm1_mainscreen,rm1_vents,rm1_vbutton,rm1_wires,rm1_datafood],0,0,[0,2],"bg_1bridge_room",[])
define RM2_hub = Room("Hub TEST",2,"bg_2hub_room",[skyart,rm2_trash,rm2_table,charger,rm2_door1,rm2_door2,logo,rm2_elevator,rm2_light1,rm2_light2,rm2_bigdoor,planetmodel,powermail,marnie_rm2,sprocko_rm2,gelato_rm2,otus_rm2,ai_rm2],0,0,[1,3,4,5,6],"bg_2hub_room",[])
define RM3_lab = Room("Lab TEST",3,"bg_3lab_room",[rm3_ceiling,rm3_window,partshead,partsarm,raydish,constructor,fluidtanks,biodevice,rm3_datapad,rm3_safe,rm3_computer,chembank1,chembank2,chembank3,sprocko_rm3],0,0,[2,4,5],"bg_3lab_room",[])
define RM4_con = Room("Conservatory TEST",4,"bg_4con_room",[hangingplants,garden,scarecrow,watertank,rm4_stair,rm4_panels,pumpdoor,pumps,rm4_light,forest,colorfulflower,bird,marnie_rm4],0,0,[2,3,5],"bg_4con_room",[])
define RM5_bar = Room("Bar TEST",5,"bg_5bar_room",[booth,plantmonster,paintings,eyetree,moose,harpoon,bonemonster,bughead,rm5_tubes,drinkmaker,drinks1,drinks2,rm5_datapad,gelato_rm5],0,0,[2,3,4],"bg_5bar_room",[])
define RM6_core = Room("Core TEST",6,"bg_6core_room",[memento,rm6_door,jarbot,jartop,jarman,rm6_computer,deadguy,rm6_rcore,rm6_points1,rm6_points2,rm6_datapad,otus_rm6],0,0,[2],"bg_6core_room",[])

#####items######
define rm0_lockerkey = Item("Small Key",0,"item/item_key1_%s.png","A small key found in a sock. Too small to be a door's key.", "nonedonotusetest","rm0_lockersolution","item/item_key1_idle.png",["rm0_lockerkeycommsp","rm0_lockerkeycommmar","rm0_lockerkeycommot","rm0_lockerkeycomgel","rm0_lockerkeycomai"])

define rm0_food = Item("Food Bar",1,"item/item_food1_%s.png", "A nasty looking food bar. You could swear it is squirming in your hand.","nonedonotusetest", "rm0_foodsolution", "item/item_food1_idle.png",["rm0_foodcommsp","rm0_foodcommmar","rm0_foodcommot","rm0_foodcomgel","rm0_foodcomai"] )














## Roommanager (and Inventory soon)
define roommanager = RoomManager("roommanager",[RM0_cold,RM1_bridge,RM2_hub,RM3_lab,RM4_con,RM5_bar,RM6_core],RM0_cold,1,0,0)

define inventory = Inventory([],"")
