from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=0, fuel=10, fuel_consumption=1):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError(f'fuel = 0')

    def move(self, dist):
        fuel_dist = dist*self.fuel_consumption
        if self.fuel > fuel_dist:
            self.fuel -= fuel_dist
        else:
            raise NotEnoughFuel(f'fuel_dist = {fuel_dist}, fuel = {self.fuel}')