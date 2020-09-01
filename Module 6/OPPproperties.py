class ExampleClass:
    __counter = 0

    def __init__(self, val=1):
        # this is an instance variable
        self.__first = val
        # this is an class variable. Underscores to make it private
        ExampleClass.__counter += 1

    def setSecond(self, val):
        # other instance variable
        self.__second = val


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.__third = 5

print(exampleObject1.__dict__, exampleObject1._ExampleClass__counter)
print(exampleObject2.__dict__, exampleObject2._ExampleClass__counter)
print(exampleObject3.__dict__, exampleObject3._ExampleClass__counter)
print(ExampleClass.__dict__)
