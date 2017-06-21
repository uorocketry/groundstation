import kivy
kivy.require("1.10.0")

import time

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from graph import Graph, MeshLinePlot
from dummy_rocket import DummyRocket
from kivy.uix.popup import Popup

#Set window not resizeable
#from kivy.config import Config
#Config.set('graphics','resizable',0)

#Set window size
#from kivy.core.window import Window
#Window.size = (1920, 1080)

class DashboardGridLayout(GridLayout):

    def update_clock(self, dt):
        self.display.text = time.asctime()

    #temporary to account for Clock sending dt arguments
    #In the future this function will process the data being sent by the rocket
    def update_rocket(self, dt):
        self.rocket.update()

    def connect(self):
        #self.ids.graph_alt.add_plot(self.plot)
        self.alt_set = []
        self.vel_set = []
        self.acc_set = []
        self.rocket = DummyRocket()
        self.rocket.set_thrust(1)
        self.open_popup()
        Clock.schedule_interval(self.update_rocket, 0.001)
        Clock.schedule_interval(self.read_data, 0.001)

    def read_data(self, dt):
        alt = self.rocket.altitude
        print(alt)
        self.alt_set.append(alt)

        vel = self.rocket.velocity
        print(vel)
        self.vel_set.append(vel)

        acc = self.rocket.acceleration
        print(acc)
        self.acc_set.append(acc)

    def open_popup(self):
        connection_popup = CustomPopup()
        connection_popup.open()


class CustomPopup(Popup):
    pass



class DashboardApp(App):
    def build(self):
        d = DashboardGridLayout()
        Clock.schedule_interval(d.update_clock, 1)
        return d

dbApp = DashboardApp()
dbApp.run()



