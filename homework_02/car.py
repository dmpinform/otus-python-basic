"""
создайте класс `Car`, наследник `Vehicle`
"""
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from homework_02.base import Vehicle

class Car(Vehicle):
    def __init__(self, weight=0, fuel=10, fuel_consumption=1):
        self.engine=None
        super().__init__(weight,fuel,fuel_consumption)

    def set_engine(self,engine):
        self.engine=engine