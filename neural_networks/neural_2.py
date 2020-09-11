import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataDict = {
    'Person': [1,2,3,4,5,6,7,8],
    'Loss of Smell': [1,1,0,0,1,0,0,0],
    'Weight Loss': [0,0,0,1,1,0,0,0],
    'Runny Nose': [0,0,1,0,0,1,0,1],
    'Body Pain': [1,0,1,0,0,1,1,0],
    'Result': [1,1,0,0,1,1,0,0]
}
# dataset = pd.DataFrame(data)
data_array = np.array(list(dataDict.values())).transpose()

# input data
input_data = data_array[:,1:5]
rows, cols = input_data.shape

# output data
target_output = data_array[:,5].reshape(rows,1)
print([rows, cols], data_array, input_data, target_output, sep='\n\n')

# pesos
weights = np.array([0.1, 0.2, 0.3, 0.4]).reshape(cols, 1)
print('\n', weights)

# peso del bias
bias = 0.3

# Taza de aprendizaje (learning rate)
lr = 0.05

# funcion sigmoidal
def sigmoid(x):
    return 1/(1+np.exp(-x))

# derivada de la sigmoidal
def dx_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))

# Main neural network
iterations = 10000
spectation = 0.001
errorTrack = []
for _ in range(iterations):
    # inputs
    inputs = input_data
    
    # feedfoward input
    pred_in = inputs@weights + bias
    
    # feedfoward output
    pred_out = sigmoid(pred_in)
    
    # backpropagation
    # error
    error = pred_out - target_output
    x = error.sum()
    errorTrack.append(x)
    print(f'error: {x}')
    
    if x < spectation:
        break

    # calculating derivative
    dcost_dpred = error
    dpred_dz = dx_sigmoid(pred_out)
    
    # multiply individual derivative
    z_delta = dcost_dpred * dpred_dz
    
    # multiply with the 3rd individual derivative
    weights -= lr * (input_data.T @ z_delta)

    # updating the bias weight value
    for val in z_delta:
        bias -= lr * val

print()
print(weights, bias, sep='\n')

# weights = np.array(
# [[10.1634992],
#  [ 0.45744949],
#  [ 2.97441782],
#  [ 2.9938138]]
# )
# bias = -6.07764153
# print(weights, bias, sep='\n')

test = sigmoid(np.array([1,0,0,1]) @ weights + bias)
test2 = sigmoid(np.array([0,0,1,0]) @ weights + bias)
test3 = sigmoid(np.array([1,0,1,0]) @ weights + bias)
print(test, test2, test3)
plt.plot(errorTrack)
plt.show()
