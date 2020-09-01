class Stack:
    def __init__(self):
        self.__stackList = []
        
    def push(self,val):
        self.__stackList.append(val)
        
    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

# Esta clase esta heredando de la primera
# para heredar, tienes que colocar como argumento de la nueva clase, la clase padre,
# y colocar en el constructor, el metodo del contstructor de la clase padre, con el argumento self.
# luego de esto, puedes a\~nadir las propiedades extras.

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def getSum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stackObject = AddingStack()

for i in range(5):
    stackObject.push(i)
print(stackObject.getSum())

for i in range(5):
    print(stackObject.pop())