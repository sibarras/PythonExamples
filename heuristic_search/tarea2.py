# Algoritmo Heuristico para Encontrar la ruta optima o de menor coste.
"""
Diagrama del Problema:


    ___  A  ___
  /      |      \\
 |       |       |
 B       C       D
 |       |       |
 E       F       G
 |       |       |
 H       I       J
 |       |    /  |
 K       L       M 
 |       |       |
 N       O       P

    ___ 0+2 ___
  /      |      \\
 |       |       |
1+1     1+1     1+3
 |       |       |
2+1     2+1     2+2
 |       |       |
3+1     3+1     3+2
 |       |    /  |
4+1   4+1->3+1  4+1
 |       |       |
5+0     4+0     5+0
"""

connections = [
]

abiertos = []
cerrados = []

end = False

class Node:
    def __init__(self, value:str, parent, child):
        self.name = value
        self.parent = parent
        self.child = child
        self.open = True
    
    def value(self):
        if '->' in self.name:
            self.name.split('')

# Root node
a_node = Node() 
while not end:
    