# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass


class GroundVehicle(Vehicle):  # extends Vehicle
    pass


class FlightVehicle(Vehicle):  # extends Vehicle
    pass


class Car(GroundVehicle):  # extends GroundVehicle
    pass


class Motorcycle(GroundVehicle):  # extends GroundVehicle
    pass


class Starship(FlightVehicle):  # extends FlightVehicle
    pass


class Airplane(FlightVehicle):  # extends FlightVehicle
    pass
