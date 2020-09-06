# Algoritmo Heuristico para Encontrar la ruta optima o de menor coste.

class Node:
    def __init__(self, name: str, value: str, child):
        # propiedades de la clase Node
        self.name = name
        self.__char = value

        self.childs = []
        self.currentParentLink = 0

        # defino los hijos como una lista de nodos
        if type(child) is list:
            self.childs = child
        else:
            self.childs = [child]

        # tratar con el valor introducido, para ver si es de dos valores o uno solo
        if '->' in self.__char:
            vals = self.__char.split('->')
        else:
            vals = [self.__char]
        vals = [val[::2]  for val in vals]
        self.vals = [[int(g), int(h)] for g,h in vals]
        self.setNewLink()

    def __repr__(self):
        return f'({self.name}: {self.g}+{self.h})'

    def currentParentF(self):
        self.currentParentLink += 1
        return sum(self.vals[self.currentParentLink])

    def setNewLink(self):
        self.activeParentLink = self.currentParentLink
        self.g, self.h = self.vals[self.activeParentLink]
        self.f = sum(self.vals[self.activeParentLink])
        return 'Active Link: ' + str(self.activeParentLink)


class AStar:
    def __init__(self, root, goal):

        # convierto root y goal a listas
        if type(root) is list:
            self.roots = root
        else:
            self.roots = [root]
        if type(goal) is list:
            self.goals = goal
        else:
            self.goals = [goal]

        # Defino variables del Algoritmo
        self.opened = []
        self.closed = []

    def runAlgorithm(self):
        self.opened.append(self.roots[0])
        self.currentNode = self.opened[0]
        self.showStep()

        while self.currentNode not in self.goals:
            self.opened.remove(self.currentNode)
            self.closed.append(self.currentNode)

            childs = self.currentNode.childs
            self.manageChilds(childs)

            self.opened = sorted(self.opened+self.currentNode.childs, key=lambda node: node.h)
            self.opened = sorted(self.opened, key=lambda node: node.f)

            self.showStep()
            self.currentNode = self.opened[0]
        else:
            self.opened.remove(self.currentNode)
            self.closed.append(self.currentNode)
            self.showStep()

    def manageChilds(self, childs):
        for child in childs:
            if child in self.opened:
                if child.currentParentF() < child.f:
                    self.opened.remove(child)
                    child.setNewLink()
            if child in self.closed:
                if child.currentParentF() < child.f:
                    self.closed.remove(child)
                    child.setNewLink()

    def showPath(self):
        self.path = []
        self.totalCost = 0

        while self.currentNode not in self.roots:
            self.totalCost += self.currentNode.f
            self.path.append(self.currentNode)

            # nodos que podrian ser el padre
            possibleNode = []

            for node in self.closed:
                if self.currentNode in node.childs:
                    possibleNode.append(node)

            # de los posibles padres, elijo el que quedo como link activo en la busqueda
            self.currentNode = possibleNode[self.currentNode.activeParentLink]

        # una vez llegado al nodo raiz
        self.totalCost += self.currentNode.f
        self.path.append(self.currentNode)
        self.path.reverse()
        print('CAMINO: ' + str(self.path))
        print('COSTE TOTAL: ' + str(self.totalCost))

    def showStep(self):
        print('Actual: ' + str(self.currentNode))
        print('Abiertos: ' + str(self.opened))
        print('Cerrados: ' + str(self.closed) + '\n\n')


def main():
    diagram = """
    Diagrama del Problema:

       ___ 0+2 ___             ___  A  ___
     /      |      \\         /      |      \\
    |       |       |       |       |       |
   1+1     1+1     1+3      B       C       D
    |       |       |       |       |       |
   2+1     2+1   - 2+2      E       F     - G
    |       |   |   |       |       |    |  |
   3+1     3+1  |  3+2      H       I    |  J
    |       |   /   |       |       |   /   |
   4+1   4+1->3+1  4+1      K       L -     M 
    |       |       |       |       |       |
   5+0     4+0     5+0      N       O       P

    """
    print(diagram+'\n\n')
    # Name = Node ( Name, Value, Child )
    p = Node('P', '5+0', None)
    o = Node('O', '4+0', None)
    n = Node('N', '5+0', None)
    m = Node('M', '4+1', p)
    l = Node('L', '4+1->3+1', o)
    k = Node('K', '4+1', n)
    j = Node('J', '3+2', m)
    i = Node('I', '3+1', l)
    h = Node('H', '3+1', k)
    g = Node('G', '2+2', [j, l])
    f = Node('F', '2+1', i)
    e = Node('E', '2+1', h)
    d = Node('D', '1+3', g)
    c = Node('C', '1+1', f)
    b = Node('B', '1+1', e)
    a = Node('A', '0+2', [b, c, d])  # Root

    algorithm = AStar(a, [n, o, p])
    algorithm.runAlgorithm()
    algorithm.showPath()


if __name__ == '__main__':
    main()
