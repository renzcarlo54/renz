from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (500, 600)     # for Window size
#    for ScreenManager
screen_helper = """ 
ScreenManager:
    
    MainScreen:
    SafetyScreen:
    FirstScreen:
    CRScreen:
    SBScreen:
    INScreen:
    BHScreen:
    BFScreen:
    DBScreen:
    CFScreen:
    AFAScreen:
    TCScreen:
    GDPScreen:
    FDPScreen:
    EarthScreen:
    FloodsScreen:
    TSLScreen:
    WindScreen:
    LandScreen:
    StructuralScreen:
    ForestScreen:
    FireScreen:
    FireRScreen:
    HotlineScreen:
    BatsScreen:
    NasScreen:
    TanScreen:
    LipScreen:
    SanScreen:
    TalScreen:
    CalScreen:
    San2Screen:
    RosScreen:
    BauScreen:
    PasScreen:
    MabScreen:
    LobScreen:
    LemScreen:
    TayScreen:
    IbaScreen:
    TinScreen:
    CaScreen:
    BalScreen:
    LiaScreen:
    MalScreen:
    
   #   for MainScreen/Window    
<MainScreen>:   
    name: 'main'
    MDCard:
        size_hint: None,None
        size: 500,430
        pos_hint:{'center_x':.5,'center_y':.6}
        elevation: 6
        md_bg_color: (236/255.0,98/255.0,81/255.0,1)
        padding: 20
        spacing: 30
        orientation: "vertical"
    Image:
        source: 'lsaver.jpg'
        pos_hint: {"center_x":.5,"center_y":.6}   
        size_hint: .9,.7
    MDFillRoundFlatIconButton:
        text: "First Aid Tips & Disaster Preparedness Plan"
        icon: 'pharmacy'
        theme_text_color: 'Custom'
        text_color: [1,1,1,1]
        md_bg_color: (255/255.0,28/255.0,0/255.0,1)
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'safety'
    MDFillRoundFlatIconButton:
        text: "Batangas Emergency Hotlines"
        icon: 'phone'
        theme_text_color: 'Custom'
        text_color: [1,1,1,1]
        md_bg_color: (255/255.0,28/255.0,0/255.0,1)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'hotline'
        
    #   for First Aid Tips & Disaster Preparedness Plan Screen/Window        
<SafetyScreen>:
    name: 'safety'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'First Aid Tips & Disaster Preparedness Plan'
                        left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 8
                    ScrollView:
                        MDGridLayout:
                            cols:2
                            padding: 5, 5
                            spacing: 5, 5
                            size_hint_y: None
                            height: self.minimum_height
                            row_default_height:120
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "firstaid.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False      
                                MDTextButton:
                                    text:     '                      First Aid'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'first'
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "disaster_preparedness.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False             
                                MDTextButton:
                                    text: '    General Disaster Preparedness'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'GDP' 
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "family2.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False           
                                MDTextButton:
                                    text: '     Family Disaster Preparedness'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'FDP'
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "Earth.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False            
                                MDTextButton:
                                    text: '                   Earthquakes'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'earth'  
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "Floods.webp"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False           
                                MDTextButton:
                                    text: '                        Floods'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'floods'   
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "storm.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False           
                                MDTextButton:
                                    text: '        Thunder Storm & Lightning'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'TSL'     
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "winds.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False           
                                MDTextButton:
                                    text: '                   Windstorm'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'WS' 
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "landslide.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False           
                                MDTextButton:
                                    text: '                     Landslide'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'ls'  
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "fire.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False          
                                MDTextButton:
                                    text: '                  Structural Fire'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'sf' 
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "forest.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False           
                                MDTextButton:
                                    text: '                     Forest Fire'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'ff'    
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "firesafety2.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False           
                                MDTextButton:
                                    text: '       Fire Safety & Protection Tips'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    font_style: 'H6'
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'fsp'  
                            MDCard:
                                size_hint: None,None
                                size: 240,150
                                pos_hint:{'center_x':.5,'center_y':.5}
                                elevation: 6
                                md_bg_color: [1,1,1,1]
                                orientation: "vertical"
                                Image:
                                    source: "rules1.png"
                                    size_hint_y: .8
                                    allow_stretch: False
                                    keep_ratio: False           
                                MDTextButton:
                                    text: '                Fire Safety Rules'
                                    theme_text_color: 'Custom'
                                    text_color: (236/255.0,98/255.0,81/255.0,1)
                                    size_hint_y: .2
                                    on_press: root.manager.current = 'fsr' 
        MDNavigationDrawer:  
            id: nav_drawer 
            BoxLayout:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "logo5.jpg"
                ScrollView:
                    MDList:
                        id: md_list
                        MDList:
                            OneLineIconListItem:
                                text: 'Hotline'     
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'        
                                on_press: root.manager.current = 'hotline'
                                IconLeftWidget:
                                    icon: "phone"
                            OneLineIconListItem:
                                text: 'Back'     
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'        
                                on_press: root.manager.current = 'main'
                                IconLeftWidget:
                                    icon: "arrow-left"
                                       
                
 #   for Fire Safety Rules Screen/Window
<FireRScreen>:
    name: 'fsr'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Fire Safety Rules"
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Checking the House'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "fs1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fs1.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fs2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fs2.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fs3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fs3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fs4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fs4.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                         
                MDCard:
                    size_hint: None,None
                    size: 490,500
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Checking and Safe Use of Household Items'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "fs5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fs5.jpg"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fs6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fs6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fs7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fs7.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fs8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fs8.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fs9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fs9.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fs10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fs10.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                                   
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'  
                  
 #    for Fire Safety & Protection Tips Screen/Window            
<FireScreen>:
    name: 'fsp'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Fire Safety & Protection Tips"
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Fire Alarms'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "fp1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp1.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp2.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp4.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp5.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                                      
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Fire Extinguishers'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "fp7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp7.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp8.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp9.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp10.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp11.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp12.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp13.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fp14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp14.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                                                       
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'   
                 
 #   for Forest Fire Screen/Window                      
<ForestScreen>:
    name: 'ff'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Forest Fire'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Encountering a Wild Fire'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "ff1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff1.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff2.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False        
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff4.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Fighting a Forest Fire as a Professional'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "ff5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff5.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff7.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff8.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff9.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff10.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                                
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Preventing Forest Fires'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "fp11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fp11.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff12.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff13.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff14.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ff15.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ff15.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                             
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'  
            
 #   for Structural Screen/Window                                                                
<StructuralScreen>:
    name: 'sf'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Structural Fire'
            elevation: 8 
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Keeping Safe in Your House During a Fire'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "sf1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf1.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf2.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf4.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf5.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf7.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                                                   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'What to Do Once You Exit Your Home'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "sf8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf8.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf9.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf10.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf11.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                          
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Preventing Future House Fires'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "sf12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf12.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf13.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sf14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sf14.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                    Image:
                        source: "white.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                               
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'  
  #   for Landslide Screen/Window                                                  
<LandScreen>:
    name: 'ls'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Landslide'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Staying Safe During a Landslide'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "ld1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld1.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld2.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld3.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld4.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld5.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld6.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld7.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld8.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False                                                       
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Staying Safe After a Landslide'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "ld9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld9.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld10.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld11.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld12.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld13.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld14.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ld15.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ld15.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                                             
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'        
 #  for Windstorm Screen/Window                                                             
<WindScreen>:
    name: 'WS'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Wind Storm'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Surviving in a Building'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "ws1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ws1.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ws2.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ws3.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ws4.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ws5.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False                                
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Surviving Out in the Open'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "ws6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ws6.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ws7.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ws8.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ws9.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ws10.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd11.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False                                            
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Preparing for a Tornado'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "ws12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd12.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd13.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd14.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws15.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd15.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws16.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd16.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ws17.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd17.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                                        
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'
 #   for Thunder Storm & Lightning Screen/Window                                                                
<TSLScreen>:
    name: 'TSL'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Thunder Storm & Lightning'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Preparing Beforehand'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "st1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st1.jpg"
                        size_hint_y: .1
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "st2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st2.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "st3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st3.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False      
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "st4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st4.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False      
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "st5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st5.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False      
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "st6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st6.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False      
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "st7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st7.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False                                                      
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Weathering the Storm'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "st8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st8.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "st9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st9.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "st10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st10.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "st11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "st11.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False    
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                    
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'     
#for Floods Screen/Window                                                                      
<FloodsScreen>:
    name: 'floods'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Floods'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Making a Flood Survival Plan'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "fl1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl1.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fl2.png"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl2.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,470
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fl3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                      
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Escaping Flood Waters'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "fl4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl4.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fl5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl5.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,470
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fl6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fl7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl7.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fl8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl8.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False                                   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Protecting Your Home'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "fl9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl9.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fl10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl10.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fl11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fl11.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                             
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'          
            
 #   for Earthquake Screen/Window                                                               
<EarthScreen>:
    name: 'earth'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Earthquake'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,550
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Taking Advantage of Warnings'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "er1.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "er1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er2.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er3.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er4.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er5.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False                  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Taking Cover Indoors'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1 
                    Image:
                        source: "er5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er6.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er7.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er8.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er9.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er10.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er11.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er12.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False                                                   
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Riding It out in a Vehicle'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1 
                    Image:
                        source: "er12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er13.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er14.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "er14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "er15.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                       
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'    
            
 #   for Family Disaster Preparedness Screen/Window                             
<FDPScreen>:
    name: 'FDP'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Family Disaster Preparedness'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'General Strategies for Making a Disaster Plan'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "fa1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa1.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa2.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False       
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa4.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa5.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa7.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa8.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa9.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa10.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False     
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa11.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "fa12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "fa12.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                                                        
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'  
               
  #   for General Disaster Preparedness Screen/Window                           
<GDPScreen>:
    name: 'GDP'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'General Disaster Preparedness'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Creating a Plan'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "gn1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn1.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn2.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn4.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn5.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn7.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                                              
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Packing an Emergency Kit'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "gn8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn8.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn9.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn10.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn11.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn12.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn13.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn14.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn15.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn15.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn16.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn16.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                                                                 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Monitoring Potential Disasters'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "gn17.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn17.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn18.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn18.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn19.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn19.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "gn20.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "gn20.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False    
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                          
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'              

 #   for First Aid Screen/Window  
<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'First Aid'
            elevation: 8
        ScrollView:
            MDList:
                OneLineListItem:
                    text: 'Cardiopulmonary Resuscitation'
                    theme_text_color: 'Custom'
                    text_color: (236/255.0,98/255.0,81/255.0,1)
                    font_style: 'H6'  
                    pos_hint: {'center_x':0.2,'center_y':0.8}
                    on_press: root.manager.current = 'cr'
                OneLineListItem:
                    text: 'Snake Bite First Aid'
                    theme_text_color: 'Custom'
                    text_color: (236/255.0,98/255.0,81/255.0,1)
                    font_style: 'H6'  
                    pos_hint: {'center_x':0.5,'center_y':0.8}
                    on_press: root.manager.current = 'sb' 
                OneLineListItem:
                    text: 'Injury/Wound First Aid'
                    theme_text_color: 'Custom'
                    text_color: (236/255.0,98/255.0,81/255.0,1)
                    font_style: 'H6'  
                    pos_hint: {'center_x':0.8,'center_y':0.8}
                    on_press: root.manager.current = 'in'
                OneLineListItem:
                    text: 'Broken Bone First Aid'
                    theme_text_color: 'Custom'
                    text_color: (236/255.0,98/255.0,81/255.0,1)
                    font_style: 'H6'  
                    pos_hint: {'center_x':0.2,'center_y':0.6}
                    on_press: root.manager.current = 'bh'  
                OneLineListItem:
                    text: 'Burns First Aid'
                    theme_text_color: 'Custom'
                    text_color: (236/255.0,98/255.0,81/255.0,1)
                    font_style: 'H6'  
                    pos_hint: {'center_x':0.5,'center_y':0.6}
                    on_press: root.manager.current = 'bf'  
                OneLineListItem:
                    text: 'Dog Bites First Aid'
                    theme_text_color: 'Custom'
                    text_color: (236/255.0,98/255.0,81/255.0,1)
                    font_style: 'H6'  
                    pos_hint: {'center_x':0.8,'center_y':0.6}
                    on_press: root.manager.current = 'db'        
                OneLineListItem:
                    text: 'Choking First Aid'
                    theme_text_color: 'Custom'
                    text_color: (236/255.0,98/255.0,81/255.0,1)
                    font_style: 'H6'  
                    pos_hint: {'center_x':0.2,'center_y':0.4}
                    on_press: root.manager.current = 'cf'  
                OneLineListItem:
                    text: 'Home First Aid Kit'
                    theme_text_color: 'Custom'
                    text_color: (236/255.0,98/255.0,81/255.0,1)
                    font_style: 'H6'  
                    pos_hint: {'center_x':0.5,'center_y':0.4}
                    on_press: root.manager.current = 'afa' 
                OneLineListItem:
                    text: 'Transportation of Casualties'
                    theme_text_color: 'Custom'
                    text_color: (236/255.0,98/255.0,81/255.0,1)
                    font_style: 'H6'  
                    pos_hint: {'center_x':0.8,'center_y':0.4}
                    on_press: root.manager.current = 'tc'                                     
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'safety'   

#for Cardiopulmonary Resuscitation Screen/Window                                 
<CRScreen>:
    name: 'cr'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Cardiopulmonary Resuscitation'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,380
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Taking Vitals'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "1.png"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False             
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "2.png"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "3.png"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False      
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "4.png"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Administering CPR'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "5.png"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False    
                        
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False
                    Image:
                        source: "6.png"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False      
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                        keep_ratio: False
                    Image:
                        source: "7.png"
                        size_hint_y: .1
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "8.png"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "9.png"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "10.png"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False
                         
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Continuing the Process Until Help Arrives'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "11.png"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "12.png"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "13.png"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Using an AED'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "14.png"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False   
                        
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "15.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "15.png"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False   
                        
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "16.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "16.png"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False                   
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "17.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "17.png"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False           
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "18.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "18.png"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "19.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "19.png"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,300
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Putting the Patient in Recovery Position'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "20.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "20.png"
                        size_hint_y: .1
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "21.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "21.png"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "22.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "22.png"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                                                                                                                                        
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'first'   
               
 #   for Snake Bite First Aid Screen/Window               
<SBScreen>:
    name: 'sb'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Snake Bite First Aid'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Treating a Venomous Snake Bite'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "sk1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk1.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk2.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk3.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False       
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk4.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk5.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk6.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk7.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk8.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk9.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk10.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk11.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Treating a Non-Venomous Snake Bite'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "sk12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk12.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk13.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk14.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk15.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk15.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk16.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk16.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk17.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk17.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Understanding Snakes and Their Bites'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "sk18.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk18.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk19.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk19.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk20.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk20.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk21.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk21.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk22.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk22.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sk23.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "sk23.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                                                                                                                                                          
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'first'      
            
#for Injury/Wood First Aid Screen/Window                      
<INScreen>:
    name: 'in'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Injury/Wood First Aid'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Treating Minor Wounds at Home'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "wd1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd1.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,430
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "wd2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd2.jpg"
                        size_hint_y: .7
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "wd3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "wd4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd4.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "wd5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd5.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                                       
                MDCard:
                    size_hint: None,None
                    size: 490,510
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Getting Medical Care'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "wd6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd6.jpg"
                        size_hint_y: .9
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "wd7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd7.jpg"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "wd8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd8.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "wd9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd9.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,420
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "wd10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "wd10.jpg"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False        
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                            
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'first'      

#for Broken Bone First Aid Screen/Window                              
<BHScreen>:
    name: 'bh'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Broken Bone First Aid'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,500
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Providing Initial Help'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "brb1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "brb1.jpg"
                        size_hint_y: .9
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,500
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "brb2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "brb2.jpg"
                        size_hint_y: .9
                        allow_stretch: False
                        keep_ratio: False     
                MDCard:
                    size_hint: None,None
                    size: 490,500
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "brb3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "brb3.jpg"
                        size_hint_y: .9
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,500
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "brb4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "brb4.jpg"
                        size_hint_y: .9
                        allow_stretch: False
                        keep_ratio: False                     
                MDCard:
                    size_hint: None,None
                    size: 490,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Addressing the Broken Bone'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "brb6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "brb6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,420
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "brb7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "brb7.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,420
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "brb8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "brb8.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                      
                        
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'first'    
            
#for Burns First Aid Screen/Window                        
<BFScreen>:
    name: 'bf'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Burns First Aid'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,380
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Categorizing the Severity of Your Burn'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "br1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br1.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,380
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "br2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br2.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,380
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "br3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br3.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,420
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "br4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br4.jpg"
                        size_hint_y: .7
                        allow_stretch: False
                        keep_ratio: False                   
                MDCard:
                    size_hint: None,None
                    size: 490,390
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Treating Minor (First- and Second-Degree) Burns at Home'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .2
                    Image:
                        source: "br5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br5.jpg"
                        size_hint_y: .3
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,390
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "br6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,390
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "br7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br7.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,390
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "br8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br8.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,390
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "br9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br9.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,390
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "br10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br10.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,390
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "br11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "br11.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,250
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "br12.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                                                  
        
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'first' 

#for Dog Bites First Aid Screen/Window                             
<DBScreen>:
    name: 'db'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Dog Bites First Aid'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Treating Minor Bites'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "db1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db1.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db2.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db3.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db4.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db5.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db6.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db7.jpg"
                        size_hint_y: .5
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db8.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db9.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db10.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False                                                                                                   
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Treating a Severe Dog Bite'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "db11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db11.jpg"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db12.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db13.jpg"
                        size_hint_y: .7
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db14.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,350
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "db15.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "db15.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False   
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                          
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'first'      
              
#for Choking First Aid Screen/Window             
<CFScreen>:
    name: 'cf'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Choking First Aid'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Helping Someone Else'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "ck1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck1.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck2.jpg"
                        size_hint_y: .7
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,440
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck4.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck5.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck6.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck7.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck8.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,500
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck9.jpg"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck10.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False                                                                      
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Helping Yourself'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "ck11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck11.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck12.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,400
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ck13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "ck13.jpg"
                        size_hint_y: .4
                        allow_stretch: False
                        keep_ratio: False  
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False     
                                                
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'first'   
            
#for Home First Aid Kit Screen/Window                   
<AFAScreen>:
    name: 'afa'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Home First Aid Kit'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,500
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Stocking Your Kit'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "hm1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm1.jpg"
                        size_hint_y: .9
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm2.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm4.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False    
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm5.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                      
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Choosing, Locating, and Maintaining Your Kit'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "hm6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm7.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm8.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm8.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm9.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm9.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False        
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm10.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm10.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False                 
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Making Mobile Kits'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "hm11.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm11.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm12.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm12.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm13.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm13.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm13.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False 
                MDCard:
                    size_hint: None,None
                    size: 490,510
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "hm14.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "hm14.jpg"
                        size_hint_y: .9
                        allow_stretch: False
                        keep_ratio: False     
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                        
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'first'      
#for Transportation of Casualties Screen/Window                  
<TCScreen>:
    name: 'tc'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Transportation of Casualties'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 5, 5
                spacing: 5, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Protecting the Spine'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "in1.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "in1.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False  
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "in2.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "in2.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "in3.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "in3.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False             
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    MDLabel:
                        text: 'Moving a Person Without a Spinal Injury'
                        theme_text_color: 'Custom'
                        text_color: (7/255.0,5/255.0,2/255.0,1)
                        font_style: 'H6'
                        size_hint_y: .1
                    Image:
                        source: "in4.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "in4.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                MDCard:
                    size_hint: None,None
                    size: 490,570
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "in5.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "in5.jpg"
                        size_hint_y: .9
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "in6.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "in6.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False
                MDCard:
                    size_hint: None,None
                    size: 490,450
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "in7.jfif"
                        size_hint_y: .8
                        allow_stretch: False
                        keep_ratio: False 
                    Image:
                        source: "in7.jpg"
                        size_hint_y: .6
                        allow_stretch: False
                        keep_ratio: False   
                    Image:
                        source: "white.jpg"
                        size_hint_y: .2
                        allow_stretch: False
                        keep_ratio: False                                 
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'first'       
                                                              
#for Hotline Screen/Window                                  
<HotlineScreen>:
    name: 'hotline'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Batangas Emergency Hotline'
                        left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 8
                    ScrollView:
                        MDList:
                            OneLineListItem:
                                text:'Balayan'      
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'         
                                on_press: root.manager.current = 'bal'
                            OneLineListItem:
                                text:'Batangas City'
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'
                                on_press: root.manager.current = 'bats'     
                            OneLineListItem:
                                text:'Bauan'       
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'         
                                on_press: root.manager.current = 'bau'
                            OneLineListItem:
                                text:'Calaca'
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'
                                on_press: root.manager.current = 'cal'
                            OneLineListItem:
                                text:'Calatagan'    
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'             
                                on_press: root.manager.current = 'ca'    
                            OneLineListItem:
                                text:'Ibaan'       
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'         
                                on_press: root.manager.current = 'iba'
                            OneLineListItem:
                                text:'Lemery'     
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'            
                                on_press: root.manager.current = 'lem'
                            OneLineListItem:
                                text: 'Lian'       
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'        
                                on_press: root.manager.current = 'lia'
                            OneLineListItem: 
                                text:'Lipa City'
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'
                                on_press: root.manager.current = 'lip' 
                            OneLineListItem:
                                text:'Lobo'          
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'       
                                on_press: root.manager.current = 'lob'
                            OneLineListItem:
                                text:'Mabini'        
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'         
                                on_press: root.manager.current = 'mab'
                            OneLineListItem:
                                text: 'Malvar'     
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'        
                                on_press: root.manager.current = 'mal'
                            OneLineListItem:
                                text:'Nasugbu'
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'
                                on_press: root.manager.current = 'nas'    
                            OneLineListItem:
                                text:'Rosario'    
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'             
                                on_press: root.manager.current = 'ros'
                            OneLineListItem:
                                text:'San Juan'   
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'         
                                on_press: root.manager.current = 'san2'
                            OneLineListItem:
                                text:'San Pascual' 
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'                
                                on_press: root.manager.current = 'pas'
                            OneLineListItem: 
                                text:'Santo Tomas'
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'
                                on_press: root.manager.current = 'san'                 
                            OneLineListItem:
                                text:'Talisay'
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'
                                on_press: root.manager.current = 'tal'        
                            OneLineListItem:
                                text:'Tanauan'
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'
                                on_press: root.manager.current = 'tan'  
                            OneLineListItem:
                                text:'Taysan'       
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'         
                                on_press: root.manager.current = 'tay'    
                            OneLineListItem:
                                text:'Tingloy'     
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'            
                                on_press: root.manager.current = 'tin'                                                                                                                                                                                                  
        MDNavigationDrawer:  
            id: nav_drawer 
            BoxLayout:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "bats.gif"
                ScrollView:
                    MDList:
                        id: md_list
                        MDList:
                            OneLineIconListItem:
                                text: "First Aid"
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'        
                                on_press: root.manager.current = 'safety'
                                IconLeftWidget:
                                    icon: "pharmacy"
                            OneLineIconListItem:
                                text: 'Back'     
                                theme_text_color: 'Custom'
                                text_color: (236/255.0,98/255.0,81/255.0,1)
                                font_style: 'H6'        
                                on_press: root.manager.current = 'main'
                                IconLeftWidget:
                                    icon: "arrow-left"  
                                                                                                                                      
#for Batangas City Screen/Window           
<BatsScreen>:
    name: 'bats'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Batangas City'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ht1.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False            
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'  
            
#for Nasugbu Screen/Window                            
<NasScreen>:
    name: 'nas'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Nasugbu'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "nasugbu.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False    
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'    
            
#for Tanauan Screen/Window                              
<TanScreen>:
    name: 'tan'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Tanauan'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "tanauan.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False   
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'    
            
#for Lipa City Screen/Window                               
<LipScreen>:
    name: 'lip'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Lipa City'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "lipa.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False     
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'           

#for Santo Tomas Screen/Window                      
<SanScreen>:
    name: 'san'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Santo Tomas'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "santo.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False   
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'   
            
#for Talisay Screen/Window                                
<TalScreen>:
    name: 'tal'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Talisay'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "talisay.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False  
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'       
               
#for Calaca Screen/Window                          
<CalScreen>:
    name: 'cal'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Calaca'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "calaca.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False      
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'   
            
#for San Juan Screen/Window                             
<San2Screen>:
    name: 'san2'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'San Juan'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sanjuan.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False  
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'  
            
#for Rosario Screen/Window                                 
<RosScreen>:
    name: 'ros'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Rosario'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "rosario.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False      
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'     
#for Bauan Screen/Window                           
<BauScreen>:
    name: 'bau'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Bauan'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "bauan.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False   
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'    
#for San Pascual Screen/Window                               
<PasScreen>:
    name: 'pas'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'San Pascual'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "sanpascual.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'   
             
#for Mabini Screen/Window                                 
<MabScreen>:
    name: 'mab'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Mabini'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "mabini.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False      
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'  
#for Lobo Screen/Window                              
<LobScreen>:
    name: 'lob'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Lobo'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "lobo.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False   
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'  
             
#for Lemery Screen/Window                                
<LemScreen>:
    name: 'lem'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Lemery'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "lemery.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False      
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'  
             
#for Taysan Screen/Window                             
<TayScreen>:
    name: 'tay'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Taysan'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "taysan.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False   
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'  
            
#for Ibaan Screen/Window                                 
<IbaScreen>:
    name: 'iba'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Ibaan'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "ibaan.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False  
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'   
            
#for Tingloy Screen/Window                                 
<TinScreen>:
    name: 'tin'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Tingloy'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "tingloy.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False  
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'       
            
#for Calatagan Screen/Window                             
<CaScreen>:
    name: 'ca'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Calatagan'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "calatagan.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False 
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'   
             
#for Balayan Screen/Window                          
<BalScreen>:
    name: 'bal'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Balayan'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "balayan.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False  
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'          
            
#for Lian Screen/Window                     
<LiaScreen>:
    name: 'lia'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Lian'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "lian.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False 
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline' 
            
#for Malvar Screen/Window                               
<MalScreen>:
    name: 'mal'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Malvar'
            elevation: 8
        ScrollView: 
            MDGridLayout:
                cols:1
                padding: 20, 5
                spacing: 20, 5
                size_hint_y: None
                height: self.minimum_height
                row_default_height:250
                MDCard:
                    size_hint: None,None
                    size: 460,490
                    pos_hint:{'center_x':.5,'center_y':.5}
                    elevation: 6
                    md_bg_color: [1,1,1,1]
                    orientation: "vertical"
                    Image:
                        source: "malvar.jpg"
                        size_hint_y: .10
                        allow_stretch: False
                        keep_ratio: False
    MDBottomAppBar:  
        MDToolbar:
            mode: 'end'
            type: 'bottom'
            icon: 'arrow-left'
            on_action_button: root.manager.current = 'hotline'    
                
        

"""


class MainScreen(Screen):  # class for MainScreen/Window
    pass


class SafetyScreen(Screen):  # class for First Aid Tips & Disaster Preparedness Plan Screen/Window
    pass


class FDPScreen(Screen):  # class for Family Disaster Preparedness Plan Screen/Window
    pass


class FirstScreen(Screen):  # class for First Aid  Screen/Window
    pass


class CRScreen(Screen):  # class for Cardiopulmonary Resuscitation Screen/Window
    pass


class SBScreen(Screen):  # class for Snake Bites First Aid Screen/Window
    pass


class INScreen(Screen):  # class for Injury/Wound First Aid Screen/Window
    pass


class BHScreen(Screen):  # class for Broken Bone First Aid Screen/Window
    pass


class BFScreen(Screen):   # class for Burns First Aid Screen/Window
    pass


class DBScreen(Screen):  # class for Dog Bite First Aid Screen/Window
    pass


class CFScreen(Screen):  # class for Choking First Aid Screen/Window
    pass


class AFAScreen(Screen):  # class for Home First Aid Kit Screen/Window
    pass


class TCScreen(Screen):  # class for Transportation of Casualties Screen/Window
    pass


class GDPScreen(Screen):  # class for General Disaster Plan Screen/Window
    pass


class EarthScreen(Screen):  # class for Earthquake Screen/Window
    pass


class FloodsScreen(Screen):  # class for Floods Screen/Window
    pass


class TSLScreen(Screen):  # class for ThunderStorm Lightning Screen/Window
    pass


class WindScreen(Screen):  # class for Windstorm Screen/Window
    pass


class LandScreen(Screen):  # class for Landslides Screen/Window
    pass


class StructuralScreen(Screen):  # class for Structural Fire Screen/Window
    pass


class ForestScreen(Screen):  # class for Forest Fire Screen/Window
    pass


class FireScreen(Screen):  # class for Fire Safety & Protection tips Screen/Window
    pass


class FireRScreen(Screen):  # class for Fire Safety Rules Screen/Window
    pass


class HotlineScreen(Screen):  # class for Hotline Screen/Window
    pass


class BatsScreen(Screen):  # class for Batangas City Screen/Window
    pass


class NasScreen(Screen):  # class for Nasugbu Screen/Window
    pass


class TanScreen(Screen):  # class for Tanauan Screen/Window
    pass


class LipScreen(Screen):  # class for Lipa City Screen/Window
    pass


class SanScreen(Screen):  # class for Santo Tomas Screen/Window
    pass


class TalScreen(Screen):  # class for Talisay Screen/Window
    pass


class CalScreen(Screen):  # class for Calaca Screen/Window
    pass


class San2Screen(Screen):  # class for San Juan Screen/Window
    pass


class RosScreen(Screen):  # class for Rosario Screen/Window
    pass


class BauScreen(Screen):  # class for Bauan Screen/Window
    pass


class PasScreen(Screen):  # class for San Pascual Screen/Window
    pass


class MabScreen(Screen):  # class for Mabini Screen/Window
    pass


class LobScreen(Screen):  # class for Mabini Screen/Window
    pass


class LemScreen(Screen):  # class for Lemery Screen/Window
    pass


class TayScreen(Screen):  # class for Taysan Screen/Window
    pass


class IbaScreen(Screen):  # class for Ibaan Screen/Window
    pass


class TinScreen(Screen):  # class for Tingloy Screen/Window
    pass


class CaScreen(Screen):  # class for Calatagan Screen/Window
    pass


class BalScreen(Screen):  # class for Balayan Screen/Window
    pass


class LiaScreen(Screen):  # class for Lian Screen/Window
    pass


class MalScreen(Screen):  # class for Malvar Screen/Window
    pass


sm = ScreenManager()  # For ScreenManager
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SafetyScreen(name='safety'))
sm.add_widget(FirstScreen(name='first'))
sm.add_widget(CRScreen(name='cr'))
sm.add_widget(SBScreen(name='sb'))
sm.add_widget(INScreen(name='in'))
sm.add_widget(BHScreen(name='bh'))
sm.add_widget(BFScreen(name='bf'))
sm.add_widget(DBScreen(name='db'))
sm.add_widget(CFScreen(name='cf'))
sm.add_widget(AFAScreen(name='afa'))
sm.add_widget(TCScreen(name='tc'))
sm.add_widget(GDPScreen(name='GDP'))
sm.add_widget(FDPScreen(name='FDP'))
sm.add_widget(EarthScreen(name='earth'))
sm.add_widget(FloodsScreen(name='floods'))
sm.add_widget(TSLScreen(name='TSL'))
sm.add_widget(WindScreen(name='WS'))
sm.add_widget(LandScreen(name='ls'))
sm.add_widget(StructuralScreen(name='sf'))
sm.add_widget(ForestScreen(name='ff'))
sm.add_widget(FireScreen(name='fsp'))
sm.add_widget(FireRScreen(name='fsr'))
sm.add_widget(HotlineScreen(name='hotline'))
sm.add_widget(BatsScreen(name='bats'))


class LifeSaverApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        return screen


LifeSaverApp().run()
