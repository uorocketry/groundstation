#


import kivy
kivy.require("1.10.0")

import time
import xlwt

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
        self.end = False
        self.plot()

        #runs the sim before graph starts to prevent performance issues
        while not (self.rocket.burnout):
            if(self.rocket.flight_time %100 == 0):

                self.alt = self.rocket.altitude
                self.alt_set.append(self.alt)

                self.vel = self.rocket.velocity
                self.vel_set.append(self.vel)

                self.acc = self.rocket.acceleration
                self.acc_set.append(self.acc)

                self.tim = self.rocket.flight_time
                self.tim_set.append(self.tim / 1000)

            self.rocket.update()

        #Create the excel sheet to which all data will be saved
        self.book = xlwt.Workbook(encoding="utf-8")
        self.sheet1 = self.book.add_sheet("Flight Data")
        self.sheet1.write(0, 0, "Flight Time")
        self.sheet1.write(1, 0, "Altitude")
        self.sheet1.write(2, 0, "Velocity")
        self.sheet1.write(3, 0, "Acceleration")

        #Start reading data
        Clock.schedule_interval(self.update, 0.1)

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

        #while (not self.end):
        #Check to make sure all data is received; if not set as 0
        try:
            self.tim = self.tim_set[self.ele]/1000
        except IndexError:
            self.tim = self.tim + 0.1

        try:
            self.alt = self.alt_set[self.ele]

        except IndexError:
            self.alt = 0

        try:
            self.vel = self.vel_set[self.ele]

        except IndexError:
            self.vel = 0

        try:
            self.acc = self.acc_set[self.ele]

        except IndexError:
            self.acc = 0


        #Add all the values to their respective arrays
        self.tim_set.append(self.tim)
        self.alt_set.append(self.alt)
        self.vel_set.append(self.vel)
        self.acc_set.append(self.acc)

        self.alt_display.text = str(round(self.alt_set[self.ele], 2))
        self.vel_display.text = str(round(self.vel_set[self.ele], 2))
        self.acc_display.text = str(round(self.tim_set[self.ele], 2))

        if (self.ele <= 200):
            self.plot_alt.points = ((self.tim_set[x], self.alt_set[x]) for x in range(self.ele))
            self.plot_vel.points = ((self.tim_set[x], self.vel_set[x]) for x in range(self.ele))
            self.plot_acc.points = ((self.tim_set[x], self.acc_set[x]) for x in range(self.ele))

        else:
            self.graph_alt.xmax = self.ele/10 + 10
            self.graph_alt.xmin = self.ele/10 - 20

            self.graph_vel.xmax = self.ele/10 + 10
            self.graph_vel.xmin = self.ele/10 - 20

            self.graph_acc.xmax = self.ele/10 + 10
            self.graph_acc.xmin = self.ele/10 - 20

            self.plot_alt.points = ((self.tim_set[x], self.alt_set[x]) for x in range(self.ele-200, self.ele))
            self.plot_vel.points = ((self.tim_set[x], self.vel_set[x]) for x in range(self.ele-200, self.ele))
            self.plot_acc.points = ((self.tim_set[x], self.acc_set[x]) for x in range(self.ele-200, self.ele))

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