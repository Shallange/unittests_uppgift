import unittest
from composition import Car
from composition import Motor

oneCar = Car("bmw", "black", "320")
oneCar.startMotor()

assert(type(oneCar) == Car)
assert(isinstance(oneCar, Car))
assert(oneCar.color == "black")
assert(oneCar.brand == "bmw")
assert(oneCar.model == "320")

