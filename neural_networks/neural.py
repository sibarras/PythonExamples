import numpy as np

# put data here
from data import features, targets, features_test, target_test
print(features)

def sig(x):
    return 1/(1+np.exp(-x))

# Hiperparameters
n_hidden =  2
epochs = 1000
alpha = 0.05

# dimensiones
m, k = features.shape

# pesos
entrada_escondida = np.random.normal(scale= 1/k**0.5,
                                     size = (k,n_hidden)
                                     )
escondida_salida = np.random.normal(scale= 1/k**0.5,
                                     size = (n_hidden)
                                     )
# Entrenamiento

for e in range(epochs):
    # Variables para el gradiente
    gradiente_entrada_escondida = np.zeros(entrada_escondida.shape)
    gradiente_escondida_salida = np.zeros(escondida_salida.shape)
    
    # Itera sobre el conjunto de entrenamiento
    for x, y in zip(features, targets):
        # pasada hacia adelante (foward pass)
        z = sig(np.matmul(x, entrada_escondida))
        y_ = sig(np.matmul(escondida_salida, z)) # prediccion
        
        # Pasada hacia atras
        salida_error = (y - y_) * y_ * (1 - y_)
        escondida_error = np.dot(salida_error, escondida_salida) * z * (1 - z)
        
        gradiente_entrada_escondida += escondida_error * x[:, None]
        gradiente_escondida_salida += salida_error * z
    
    # Actualizar los pesos
    entrada_escondida += alpha * gradiente_entrada_escondida / m
    escondida_salida += alpha * gradiente_escondida_salida / m
    
    if e % (epochs / 10) == 0:
        z = sig(np.dot(features.values, entrada_escondida))
        y_ = sig(np.dot(z, escondida_salida))
        
        # funcion de costo
        costo = np.mean((y_ - targets)**2)
        if ult_costo and ult_costo < costo:
            print("Costo de Entrenamiento: ", costo, " y SUBIENDO")
        else:
            print("Costo de Entrenamiento: ", costo)
        
        ult_costo = costo
    
    # Presicion en los datos de prueba
    z = sig(np.dot(features_test, entrada_escondida))
    y_ = sig(np.dot(z, escondida_salida))
    
    predicciones = y_ > 0.5
    presicion = np.mean(predicciones == target_test)
    print("Presicion: {:.3f}".format(presicion))