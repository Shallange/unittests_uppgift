import unittest
from composition import Car
from composition import Motor

oneCar = Car("bmw", "black", "320")
oneCar.startMotor()

assert(type(oneCar) == Car)
assert(isinstance(oneCar, Car))
assert(str(oneCar.color) == "black")
assert(str(oneCar.brand) == "bmw")
assert(str(oneCar.model) == "320")

assert(callable(Motor.ignite))
assert(callable(oneCar.startMotor))