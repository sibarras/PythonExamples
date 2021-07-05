class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

# Si utilizo la funcion super, no es necesario usar self
# ni saber el nombre de la superclase que utilizo.
class Sub(Super):
    def __init__(self, nombre):
        super().__init__(nombre)

# Si utilizo el nombre literal de la superclase, tengo que
# Pasarle el self de forma obligatoria siempre.
class Sub2(Super):
    def __init__(self, nombre):
        Super.__init__(self, nombre)

obj = Sub("Andy")

print(obj)