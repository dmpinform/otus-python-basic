from abc import ABC
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from homework_02.exceptions import LowFuelError,NotEnoughFuel,CargoOverload

class Vehicle(ABC):
    def __init__(self, weight=0, fuel=10, fuel_consumption=1):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started=False

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