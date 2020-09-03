# Algoritmo Heuristico para Encontrar la ruta optima o de menor coste.
diagram = """
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
# Listas para mostrar los estados de cada nodo
opened = []
closed = []

class Node:
    def __init__(self, name:str, value:str, child):
        self.name = name
        self.char = value
        self.child = child
        
        if '->' in self.char:
            val1, val2 = self.char.split('->')
            val1, val2 = sum([int(num) for num in val1.split('+')]), sum([int(num) for num in val2.split('+')])
            self.value = (val1, val2)
        else:
            self.value = (sum([int(num) for num in self.char.split('+')]),)
        
        self.cost = self.value[0]
        self.valueCount = 0
    def __repr__(self):
        return f'({self.name}: {self.char})'


# Name = Node ( Value, Parent )
p = Node('P', '5+0', None)
o = Node('O', '4+0', None)
n = Node('N', '5+0', None)
m = Node('M', '4+1', p)
l = Node('L', '4+1->3+1', o)
k = Node('K', '4+1', n)
j = Node('J', '3+2', [l,m])
i = Node('I', '3+1', l)
h = Node('H', '3+1', k)
g = Node('G', '2+2', j)
f = Node('F', '2+1', i)
e = Node('E', '2+1', h)
d = Node('D', '1+3', g)
c = Node('C' ,'1+1', f)
b = Node('B' ,'1+1', e)

# Root node
a = Node('A', '0+2', [b,c,d])

opened.append(a) # Coloco el nodo raiz en abiertos
current = opened[0] # el primero es el que utilizamos

# imprimir diagrama
print(diagram+'\n\n')

# Iniciar el algoritmo
end = False
while not end and len(opened) > 0:
    # Mostrar los datos en el algoritmo
    print('Actual: '+str(current))
    print('Opened: '+str(opened))
    print('Closed: '+str(closed) + '\n\n')

    opened.pop() # Elimino el primer item
    closed.append(current) # anado el actual a cerrados
    
    # Genero una lista con los hijos o hijo
    if type(current.child) is Node:
        childs = [current.child]
    else:
        childs = current.child
    
    # Repetidos en la columna de cerrados o abiertos
    for child in childs:
        if child in opened or child in closed:
            child.valueCount += 1
            if child.value[child.valueCount] < child.cost:
                opened.remove(child)
                child.cost = child.value[child.valueCount]
                break
        if child in closed:
            child.valueCount += 1
            if child.value[child.valueCount] < child.cost:
                closed.remove(child)
                child.cost = child.value[child.valueCount]
                break
    
    # Insertamos los hijos en los abiertos
    opened = sorted(opened+childs, key=lambda node: node.cost, reverse=True)
    current = opened[-1]

    # Si llegamos al final salimos
    if current.child == None:
        print('Actual: '+str(current))
        print('Opened: '+str(opened))
        print('Closed: '+str(closed) + '\n\n')
        break

# Imprimir camino optimo
nodeList = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
path = []
cost = current.cost

while True:
    path.append(current)
    possibleNode = []
    for node in nodeList:
        if node.child == current:
            possibleNode.append(node)
        elif type(node.child) == list and current in node.child:
            possibleNode.append(node)

    current = possibleNode[current.valueCount]
    cost += current.cost

    if current == a:
        path.append(current)
        break
path.reverse()

print('PATH: '+ str(path))
print('Cost: '+str(cost))