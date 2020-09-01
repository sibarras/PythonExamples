import time


# Example of Inheritance. A Superclass controls
# the subclass of specific vehicles
class Vehicles:
    # This method is not used. But is here because it will be changed in
    # the subclasses
    def changedirection(left, on):
        pass

    # This function will take the future methods to use it in this method
    def turn(left):
        changedirection(left, True)
        time.sleep(0.25)
        changedirection(left, False)


class TrackedVehicle(Vehicles):
    # The real process that the class will use then the turn method is called
    def controltrack(left, stop):
        pass

    # The way that this class takes the empty method and assign it to a new
    # method in the subclass that will rule the new use of turn method in the
    # superclass
    def changedirection(left, on):
        controltrack(left, on)


class WheeledVehicle(Vehicles):
    # The real process that the class will use then the turn method is called
    def turnfrontwheels(left, on):
        pass

    # The way that this class takes the empty method and assign it to a new
    # method in the subclass that will rule the new use of turn method in the
    # superclass
    def changedirection(left, on):
        turnfrontwheels(left, on)


# ============================================================================

# Example of Composition. The process of creating
# an object using other objects.
class Tracks:
    # The way that tracks changes his direction
    def changedirection(self, left, on):
        print("Tracks: ", left, on)


class Wheels:
    # The way that wheels changes his direction
    def changedirection(self, left, on):
        print("Wheels: ", left, on)


class Vehicle:
    # We init a controller that take the previous class ways of control
    def __init__(self, controller):
        self.controller = controller

    # Then, we control the vehicle with this method, that takes te control
    # and use it
    def turn(self, left):
        self.controller.changedirection(left, True)
        time.sleep(0.25)
        self.controller.changedirection(left, False)


# We instance the vechicle class with diferents control inputs and make
# two objects using a single class.
wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())
# Test
wheeled.turn(True)
tracked.turn(False)
