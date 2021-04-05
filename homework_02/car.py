"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):

    def __init__(self, weight=0, fuel=10, fuel_consumption=1):
        self.engine=None
        super().__init__(weight, fuel, fuel_consumption)

    def set_engine(self, engine):
        self.engine = engine