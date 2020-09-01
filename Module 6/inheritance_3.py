# inhiretance 3


# both classes have the same name for variable var and meethod fun
class Left:
    var = 'L'
    varLeft = 'LL'

    def fun(self):
        return 'Left'


class Right:
    var = 'R'
    varRight = 'RR'

    def fun(self):
        return 'Right'


# object inherits
class Sub(Left, Right):
    pass


obj = Sub()
# print first
print(obj.var, obj.varLeft, obj.varRight, obj.fun())


# Where this program will do the action?
# you will see that if we call a function that cames in
# the inheritance, and the function refers to a method declared in
# both classes, then the program will doit from the second. It means that
# you could change the action of a method in older classes in new classes.
class One:
    def doit(self):
        print("doit from One")

    def doanything(self):
        self.doit()


class Two(One):
    def doit(self):
        print("doit from Two")


one = One()
two = Two()

one.doanything()
two.doanything()
