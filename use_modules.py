# Esto es necesario para que en el presente programa
# sea reconocido el programa que se encuentra en otra
# direccion.
from sys import path
module_path = './Module 6'
# Es mejor usar rutas absolutas para poder hacer esto.
path.append(module_path)

import inheritance

# Aunque el editor diga que no esta bien si funciona

print('Termine de importar el archivo inheritance')

print(ord('a'))
print(ord(' '))

