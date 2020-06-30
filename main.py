from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition
import gui

class App(MDApp):
    def build(self):
        SM=ScreenManager(transition=SlideTransition())
        SM.add_widget(gui.LoginPage("login"))
        SM.add_widget(gui.NewPgPage("nwpg"))
        SM.add_widget(gui.OpenPg("openPg"))
        return SM

print(gui.PG_SELECTED)

if __name__=="__main__":
    App().run()
