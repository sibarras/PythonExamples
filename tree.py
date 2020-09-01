treeDraw = """
          1
        /  \\
       2    3
      / \\  / \\
     4   56   7
    / \\
   8   9
"""
print(treeDraw)
tree = [
    (1, None),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2),
    (6, 3),
    (7, 3),
    (8, 4),
    (9, 4),
]


# de cualquier nodo a cualquier nodo mostrando el camino.
def treesteps(init, end=1):
    node_lst = []
    for ch, par in tree:
        if ch == init:
            if par is None:
                return ['root']
            node_lst.append(par)
            for node in treesteps(par):
                node_lst.append(node)
            return node_lst


# de cualquier nodo a cualquier nodo en cantidad
def treedistance(init, end=1):
    for ch, par in tree:
        if ch == init:
            if par is None:
                return 0
            return treedistance(par) + 1


# de cualquier nodo a cualquier nodo en cantidad
def nodeToNode(init, end=1, avoid=int):

    # estudio si el punto actual esta al lado de la respuesta
    if init == end:
        return 0
    for child, parent in tree:
        if parent == init and child == end:
            return 1
    for child, parent in tree:
        if child == init and parent == end:
            return 1
    # defino mis proximos puntos a analizar
    nextGoals = []
    fobridden = [avoid, None]
    for child, parent in tree:
        if parent == init and child not in fobridden:
            nextGoals.append(child)
        elif child == init and parent not in fobridden:
            nextGoals.append(parent)

    # analizo estos puntos
    for node in nextGoals:
        return nodeToNode(node, end, init) + 1


print(nodeToNode(9, 8))
