import kivy
kivy.require("1.10.0")

import time

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

#Set window not resizeable
#from kivy.config import Config
#Config.set('graphics','resizable',0)

#Set window size
from kivy.core.window import Window
Window.size = (1920, 1080)

class DashboardGridLayout(GridLayout):

    def update_clock(self, dt):

        self.display.text = time.asctime()


class DashboardApp(App):
    def build(self):
        d = DashboardGridLayout()
        Clock.schedule_interval(d.update_clock, 1)
        return d

dbApp = DashboardApp()
dbApp.run()


