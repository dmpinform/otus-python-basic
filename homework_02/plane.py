"""
создайте класс `Plane`, наследник `Vehicle`
"""
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from homework_02.exceptions import LowFuelError,NotEnoughFuel,CargoOverload
from homework_02.base import Vehicle
   

class Plane(Vehicle):
    def __init__(self,weight=0, fuel=10, fuel_consumption=1,max_cargo=10):
        self.cargo = 0
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, cargo):
        
        cargo_sum = self.cargo + cargo
        if cargo_sum < self.max_cargo:
            self.cargo = cargo_sum
        else:
            raise CargoOverload(f'cargo = {cargo_sum}, max = {self.max_cargo}')

    def remove_all_cargo(self):
        cargo_old = self.cargo
        self.cargo = 0
        return cargo_old