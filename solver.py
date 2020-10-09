import numpy as np

class Ecuation:
    def __init__(self, xList:list, constant=0, etype='main'):
        """Define una ecuacion como una matriz de numpy, recibiendo las variables en una lista.

        Args:
            xList (list): Se introducen los valores que multiplican a cada variable en la ecuacion
            constant (float): Valor constante de la ecuacion. Defaults to 0.
            etype (str, optional): Se define si la ecuacion es la principal('main')
                o de restriccion('slack'). Defaults to 'main'.
        """
        self.dimensions = len(xList)
        self.variables = np.array(xList)
        self.constant = constant
        self.type = etype
    
    def __repr__(self):
        return 'Ecuation(y = {} + {})'.format(self.variables, self.constant)

def solve(main:Ecuation, slacks:list):
    # Verifico que todos los valores introducidos son ecuaciones
    for slack in slacks:
        if type(slack) is not Ecuation:
            print('[ERROR]: No se utilizaron ecuaciones para ser operadas en el solver')
            return None

    def basicSolution(main=main, slacks=slacks):
        # Solucion de x1, x2, x3, ..., xn son todas ceros
        solution = np.zeros(main.dimensions)
        # Las restricciones las colocamos en cero y evaluaremos el maximo de cada una
        yres = np.array([slack.constant for slack in slacks])

        limits = []  # Limites de cada variable
        for variable in range(main.dimensions):
            # para cada variable en la ecuacion principal
            conditions = []
            for slack in slacks: # Para cada ecuacion en las restricciones
                if slack.variables[variable] > 0:
                    conditions.append(('greater', max([0,-slack.constant/slack.variables[variable]])))
                elif slack.variables[variable] < 0:
                    conditions.append(('less', -slack.constant/slack.variables[variable]))
                print('variable={}, restriccion={}'.format(variable, conditions[-1]))
            
            limits.append([0,np.Infinity])

            for res, val in conditions:
                if res == 'greater' and val > limits[-1][0]:
                    limits[-1][0] = val
                elif res == 'less' and val < limits[-1][1]:
                    limits[-1][1] = val 
            del conditions   
        return limits
    
    return basicSolution()


y = Ecuation([1,0,1], constant=3)
r1 = Ecuation([1, -1, 1], constant=2, etype='slack')
r2 = Ecuation([-1, 0, -1], constant=3, etype='slack')
r3 = Ecuation([-2, 1, 0], constant=4, etype='slack')

print(solve(y, [r1, r2, r3]))