import os
import funUtils
from configparser import RawConfigParser
from kivy.uix.screenmanager import ScreenManager,Screen
from functools import partial
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

PG_SELECTED = ''

class LoginPage(Screen):
    def __init__(self,Name):
        super(LoginPage,self).__init__(name=Name)
        self.scrollView=ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.box=BoxLayout()
        self.scrollView.add_widget(self.box)
        self.add_widget(self.scrollView)
        self.box.orientation="vertical"
        self.box.size_hint_y=None
        self.box.bind(minimum_height=self.box.setter('height'))
        self.box.padding=[10,10]
        
        btn_creapg=Button(text="Crea pg")
        btn_creapg.pos_hint={"center_x":.5,"center_y":.5}
        btn_creapg.size_hint=(None,None)
        btn_creapg.width=50
        btn_creapg.height=20
        self.box.add_widget(btn_creapg)
        grid = GridLayout()
        grid.bind(minimum_height=grid.setter('height'))
        grid.size_hint_y=None
        grid.padding=[10,10]
        grid.spacing=[10,10]
        grid.cols=2
        
        btn_creapg.bind(on_press=partial(funUtils.setScreen,self,"nwpg"))
        file = os.listdir("pg")

        def sPg(obj):
            PG_SELECTED = obj.text
            self.manager.current="openPg"
        
        for i in range(len(file)):
            btn = Button(text=str(file[i][0:-4]),size_hint_y=None,height=40)
            btn.bind(on_press=sPg)
            grid.add_widget(btn)

        self.box.add_widget(grid)



class OpenPg(Screen):
    def __init__(self,Name):
        super(OpenPg,self).__init__(name=Name)
        self.scrollView=ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.box=BoxLayout()
        self.scrollView.add_widget(self.box)
        self.add_widget(self.scrollView)
        self.box.orientation="vertical"
        self.box.size_hint_y=None
        self.box.bind(minimum_height=self.box.setter('height'))
        self.box.padding=[10,10]

        l_name = MDLabel(text=PG_SELECTED)
        



class NewPgPage(Screen):
    def __init__(self,Name):
        super(NewPgPage,self).__init__(name=Name)
        self.scrollView=ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.box=BoxLayout()
        self.scrollView.add_widget(self.box)
        self.add_widget(self.scrollView)
        self.box.orientation="vertical"
        self.box.size_hint_y=None
        self.box.bind(minimum_height=self.box.setter('height'))
        self.box.padding=[10,10]

        Grid=GridLayout(cols=2)
        Grid.bind(minimum_height=Grid.setter('height'))
        Grid.padding=[10,10]
        Grid.spacing=[10,10]
        Grid.size_hint_y=None

        funUtils.CreateForm(Grid,"Nome Personaggio")
        funUtils.CreateForm(Grid,"Classe")
        funUtils.CreateForm(Grid,"Razza")
        funUtils.CreateForm(Grid,"Livello")
        funUtils.CreateForm(Grid,"Anni")
        funUtils.CreateForm(Grid,"Esperienza")

        Grid2=GridLayout(cols=2)
        Grid2.bind(minimum_height=Grid2.setter('height'))
        Grid2.spacing=[10,10]
        Grid2.padding=[10,10]
        Grid2.size_hint_y=None

        funUtils.CreateForm(Grid2,"Forza")
        funUtils.CreateForm(Grid2,"Costituzione")
        funUtils.CreateForm(Grid2,"Destrezza")
        funUtils.CreateForm(Grid2,"Intelligenza")
        funUtils.CreateForm(Grid2,"Saggezza")
        funUtils.CreateForm(Grid2,"Carisma")
        
        def createFileConfigPg(obj):
            info=[]
            i=0
            for widget in Grid.walk(True,True) :
                if i!=0:
                    info.append(widget.text)
                i=i+1
                
            config=RawConfigParser()
            config.add_section("BASE")
            config.set("BASE",info[2],info[3])
            config.set("BASE",info[4],info[5])
            config.set("BASE",info[6],info[7])
            config.set("BASE",info[8],info[9])
            config.set("BASE",info[10],info[11])

            i=0
            
            for widget in Grid2.walk(True,True) :
                if i!=0:
                    info.append(widget.text)
                i=i+1

            config.add_section("Caratteristiche")
            config.set("Caratteristiche",info[12],info[13])
            config.set("Caratteristiche",info[14],info[15])
            config.set("Caratteristiche",info[16],info[17])
            config.set("Caratteristiche",info[18],info[19])
            config.set("Caratteristiche",info[20],info[21])
            
            with open("pg/"+info[1]+".PG","w") as configFile:
                config.write(configFile)
            funUtils.setScreen(self,"login",None)
       
        self.box.add_widget(Grid)
        self.box.add_widget(Grid2)
        build=Button(text="Crea",size_hint_y=None,height=40,width=80)
        build.padding=[10,10]
        build.bind(on_press=createFileConfigPg)
        self.box.add_widget(build)
