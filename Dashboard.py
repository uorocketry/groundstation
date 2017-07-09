import kivy
kivy.require("1.10.0")

import time

from math import sin
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
        self.clck.text = time.asctime()

    #temporary to account for Clock sending dt arguments
    #In the future this function will process the data being sent by the rocket
    def update_rocket(self, dt):
        self.rocket.update()

    def connect(self):
        self.ele = 0
        self.alt_set = []
        self.vel_set = []
        self.acc_set = []
        self.tim_set = []
        self.rocket = DummyRocket()
        self.rocket.set_thrust(1)
        self.open_popup()
        self.plot()

        Clock.schedule_interval(self.update_rocket, 0.001)
        Clock.schedule_interval(self.update, 1)

    def open_popup(self):
        connection_popup = CustomPopup()
        connection_popup.open()

    def plot(self):
        self.plot_alt = MeshLinePlot(color=[1, 0, 0, 1])
        self.plot_alt.points = [(0,0)]
        self.graph_alt.add_plot(self.plot_alt)

        self.plot_vel = MeshLinePlot(color=[1,0,0,1])
        self.plot_vel.points = [(0,0)]
        self.graph_vel.add_plot(self.plot_vel)

        self.plot_acc = MeshLinePlot(color=[1,0,0, 1])
        self.plot_acc.points = [(0,0)]
        self.graph_acc.add_plot(self.plot_acc)


    def update(self, dt):
        self.alt = self.rocket.altitude
        #self.alt_set.append(self.alt)

        self.vel = self.rocket.velocity
        #self.vel_set.append(self.vel)

        self.acc = self.rocket.acceleration
        #self.acc_set.append(self.acc)

        self.tim = self.rocket.flight_time
        #self.tim_set.append(self.tim)

        self.alt_display.text = str(round(self.alt, 2))
        self.vel_display.text = str(round(self.vel, 2))
        self.acc_display.text = str(round(self.acc, 2))

        self.plot_alt.points.append((self.tim/1000, self.alt))
        #= [(x / 1000, self.alt_set[x]) for x in range(self.ele)]
        self.plot_vel.points.append((self.tim/1000, self.vel))
        #= [(x / 1000, self.vel_set[x]) for x in range(self.ele)]
        self.plot_acc.points.append((self.tim/1000, self.acc))
        #= [(x / 1000, self.acc_set[x]) for x in range(self.ele)]

        self.ele += 1


class CustomPopup(Popup):
    pass

class CustGraph(Graph):
    pass



class DashboardApp(App):
    def build(self):
        d = DashboardGridLayout()
        Clock.schedule_interval(d.update_clock, 1)
        return d

dbApp = DashboardApp()
dbApp.run()



