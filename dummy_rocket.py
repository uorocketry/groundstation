import random
import math

class DummyRocket:
    max_thrust = 2950
    max_mass_flow_rate = 0.0012 # kg/ms

    sensor_noise = 0.5

    def __init__(self):
        self.fuel_mass = 80.0
        self.thrust_level = 0.0

        self.acceleration = 0.0
        self.altitude = 0.0
        self.velocity = 0.0

        self.flight_time = 0
        self.burnout = False

    # called once per loop (once per ms)
    def update(self):
        self.flight_time += 1
        #thrust effect
        actual_acceleration = (self.get_thrust() * random.uniform(.9, 1.0))/ self.get_mass()

        # gravity
        actual_acceleration -= 9.81

        #drag effect you must model this yourself
        actual_acceleration -= 0.024524642*1.225*math.pow(self.velocity, 2)

        self.velocity += actual_acceleration*0.001
        self.altitude = self.altitude + self.velocity*0.001 + self.acceleration*0.001*0.001

        # bad noise
        self.acceleration = random.gauss(actual_acceleration, actual_acceleration*self.sensor_noise)

        self.fuel_mass -= self.thrust_level * self.max_mass_flow_rate
        if self.fuel_mass < 0:
            self.fuel_mass = 0.0

        if self.fuel_mass == 0 and not self.burnout:
            self.burnout = True
            print "Burnout @ ", self.flight_time/1000, " s"
            print "   velocity: ", self.velocity, " m/s"
            print "    altitude: ", self.altitude, " m \n"

    # returns true if rocket is flying, false is falling
    def flying(self):
        return self.velocity >= 0

    # flight time in milliseconds
    def get_flight_time(self):
        return self.flight_time

    # acceleration in meters per second squared
    def get_acceleration(self):
        return self.acceleration

    # mass in kilograms
    def get_mass(self):
        return 10 + self.fuel_mass

    # mass in kilograms
    def get_fuel_mass(self):
        return self.fuel_mass

    # thrust in Newtons
    def get_thrust(self):
        return self.max_thrust * self.thrust_level

    # thrust percentage level [0 to 1.0]
    def set_thrust(self, percentage):

        if percentage < 0.0:
            percentage = 0.0
        elif percentage > 1.0:
            percentage = 1.0;

        if self.fuel_mass > 0.0:
            self.thrust_level = percentage
        else:
            self.thrust_level = 0
