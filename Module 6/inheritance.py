# example of __str__ method to print a class ouput
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy


sun = Star('Sun', 'Milky Way')
print(sun)


# Inheritance example of three classes and comprobation
# of the classes and subclasses
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


myVehicle = Vehicle()
myLandVehicle = LandVehicle()
myTrackedVehicle = TrackedVehicle()

for obj in [myVehicle, myLandVehicle, myTrackedVehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()


# The use of 'is' operator.
class SampleClass:
    def __init__(self, val):
        self.val = val


ob1 = SampleClass(0)
ob2 = SampleClass(2)
ob3 = ob1
ob3.val += 1

print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1)
print(ob1.val, ob2.val, ob3.val)

str1 = "Mary had a little "
str2 = "Mary had a little lamb"
str1 += "lamb"

print(str1 == str2, str1 is str2)


# To see how a class inherits properties and methods
# from his father
class Super:
    c_supVar = 1

    def __init__(self, name):
        self.name = name
        self.i_supVar = 11

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    c_subVar = 2

    def __init__(self, name):
        # Super.__init__(self, name)
        super().__init__(name)
        self.i_subVar = 12


# The class instance
obj = Sub("Andy")
# The subclass oupput
print(obj)
# Output for class variables
print(obj.c_subVar)
print(obj.c_supVar)
# output for instance variables
print(obj.i_subVar)
print(obj.i_supVar)
