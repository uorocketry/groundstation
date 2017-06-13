import kivy
kivy.require("1.10.0")

import datetime

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

#Set window not resizeable
#from kivy.config import Config
#Config.set('graphics','resizable',0)

#Set window size
from kivy.core.window import Window
Window.size = (1920, 1080)

class DashboardGridLayout(GridLayout):
    def update(self):
        return datetime.datetime.now()


class DashboardApp(App):

    def build(self):
        return DashboardGridLayout()

dbApp = DashboardApp()
dbApp.run()


