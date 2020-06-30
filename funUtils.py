from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel

def CreateForm(obj,testo):
    label=MDLabel(text=testo)
    textinput=TextInput(text="",multiline=False,halign="center")
    textinput.size_hint_y=None
    textinput.height=30
    obj.add_widget(label)
    obj.add_widget(textinput)

def setScreen(screen,sc,obj):
    screen.manager.current=sc
