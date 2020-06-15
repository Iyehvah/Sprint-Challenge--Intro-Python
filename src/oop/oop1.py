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


#this is the base class
class Vehicle:

    pass
#This is the subclass of base class
class FlightVehicle(vehicle):

    pass
#this is also a subclass of base class
class GroundVehicle(vehicle):

    pass
#this is the subclass of flight vehicle
class Starship(FlightVehicle):

    pass
#this is another subclass of flight vehicle
class Airplane(FlightVehicle):

    pass
#this is a subclass of groundvehicle
class Car(GroundVehicle):

    pass
#this is a subclass of ground vehicle and also a sisterclass of car
class Motorcycle(GroundVehicle):

    pass


