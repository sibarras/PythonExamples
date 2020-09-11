import numpy as np
featuresDict = {
    'Analisis de Aceite': [0,1,0,1,0,1,0,1,1,1],
    'Prueba de Factor de Potencia': [1,0,1,0,0,0,1,1,1,0],
    'Prueba de Resistencia de Devanados': [0,1,1,1,0,1,0,0,1,0],
    'Prueba de Relacion de Transformacion': [0,1,0,0,1,1,1,1,0,1],
    'Prueba de Disparos y alarmas': [1,0,1,1,0,0,1,0,0,0],
    'pruebas de Capacitancia en Bushings': [0,0,1,0,0,0,1,1,0,0]
}
features = np.array(list(featuresDict.values())).T
# print(features)
targets = np.array([0,1,1,0,0,1,1,1,0,0]).reshape(len(features),1)
# print(targets)
features_test = np.array([[0,1,0,1,1,1],[1,0,1,0,1,0]])
target_test = np.array([1,0]).reshape(len(features_test),1)