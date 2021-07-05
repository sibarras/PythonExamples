class ClaseMuestra:
    def __init__(self, val):
        self.val = val

ob1 = ClaseMuestra(0)
ob2 = ClaseMuestra(2)
ob3 = ob1
ob3.val += 1

print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1)
print(ob1.val, ob2.val, ob3.val)

str1 = "Mary tenía un "
str2 = "Mary tenía un corderito"
str1 += "corderito"

print(str1 == str2, str1 is str2)