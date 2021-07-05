class NewClass:
    def __init__(self, x, y) -> None:
        self.name = x
        self.number = y

obj1 = NewClass('Sam', 20)
obj2 = NewClass('Sam', 20)

print(obj1==obj2)
print()

var1 = '5555555'
var2 = '554'
print(var2 > var1)
print()

for i in range(10):
    pass
print(i)
print()

L = [1.4, 'Python', False]
T = (1.3, 'Java', 'True')
try:
    for i in range(len(L)):
        if L[i]:
            L[i]=L[i]+T[i]
        else:
            T[i]=L[i]+T[i]
    print(L)
except Exception as e:
    print('Error:', e)
print()

class Pet:
    def call_me(self):
        print('Call Me!')

obj = Pet()
Pet.call_me('ok')
print()

print({i+1 for i in range(4)})