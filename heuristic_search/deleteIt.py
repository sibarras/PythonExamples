listcomp = [[a,b,c] for a,b,c in ['1+2','2+3','3+1','1+4']]
res = [val[::2] for val in ['1+2','2+3','3+1','1+4']]
print(listcomp)
print([[int(g), int(h)] for g,h in res])

lst = [2,3,4,5]
print(lst)
while 1 not in lst:
    print(lst)
    lst.append(1)
print('ready')

class A:
    def a(self):
        print('a')

class B:
    def b(self):
        print('b')

class C(A, B):
    def c(self):
        self.a()

c = C()
c.c()