import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import random

class NeuralNetwork:
    def __init__(self):
        # Error Register
        self.errorTrack = []
        
        # Trained network
        self.trained = False
    
    def __repr__(self):
        if self.trained == False:
            return 'No trained network'
        return 'Neural Network:\n(Weights: {},\nBias: {},\nTrain: {})\n'\
                .format(list(self.weights.reshape(len(self.weights))), float(self.bias), self.trained)

    @staticmethod
    def __sigmoid(x):
        return 1/(1+np.exp(-x))
    
    def __sigmoid_dx(self, x):
        return self.__sigmoid(x) * (1-self.__sigmoid(x))

    def train(self, inputs:list, targets:list, iterations=10000, learning_rate=0.05, errorRange=0.001):
        # Data for training
        self.inputs = np.array(list(inputs))
        self.samples, self.dendrites = self.inputs.shape
        self.targets = np.array(list(targets)).reshape(self.samples, 1)
        
        # dimension verification
        assert self.targets.shape[0] == self.inputs.shape[0]
        i = 0
        # for first train
        if not self.trained:
            # Weights
            self.weights = np.array([random() for _ in range(self.dendrites)])
            self.weights = self.weights.reshape(self.dendrites, 1)
            
            # bias
            self.bias = random()
            self.totError = 0
            
        while i in range(iterations) or self.totError < errorRange:
            # prediction
            prediction_in = self.inputs @ self.weights + self.bias
            prediction_out = self.__sigmoid(prediction_in)
            
            # Error
            error = prediction_out - self.targets
            self.totError = error.sum()
            self.errorTrack.append(self.totError)
            
            # Calculate derivatives
            dprediction_dz = self.__sigmoid_dx(prediction_out)
            z_delta = error * dprediction_dz
            
            # Calculate 3rd derivative for weights
            self.weights -= learning_rate * (self.inputs.T @ z_delta)
            
            # weight for bias
            for delta in z_delta:
                self.bias -= learning_rate * delta
            
            # Counter
            i += 1

        self.trained = True
        self.showProgress()

    def showProgress(self):
        if len(self.errorTrack) > 0:
            plt.plot(self.errorTrack)
            plt.title('Error in iterations')
            plt.xlabel('Iterations')
            plt.ylabel('Error')
            plt.show()

    def saveTrain(self):
        if self.trained == True:
            file = open('neural_networks/NeuralNetworkData.txt', mode='wt')
            file.write(f'weights: {list(self.weights)}\n')
            file.write(f'bias: {float(self.bias)}')
            file.close()
            plt.plot(self.errorTrack)
            plt.title('Error in iterations')
            plt.xlabel('Iterations')
            plt.ylabel('Error')
            plt.savefig('neural_networks/error.png')

    def predict(self, inputs:list):
        assert self.trained and len(inputs) == self.dendrites
        inputs = np.array(inputs)
        prediction_in = inputs @ self.weights + self.bias
        return 'Is True in {}%'.format(round(float(self.__sigmoid(prediction_in))*100, 2))

dataDict = {
    'Sample': [1,2,3,4,5,6,7,8],
    'Loss of Smell': [1,1,0,0,1,0,0,0],
    'Weight Loss': [0,0,0,1,1,0,0,0],
    'Runny Nose': [0,0,1,0,0,1,0,1],
    'Body Pain': [1,0,1,0,0,1,1,0],
    'Result': [1,1,0,0,1,1,0,0]
}

df = pd.DataFrame(dataDict)
print(df)
inputs = np.array(list(dataDict.values())[1:-1]).T
targets = list(dataDict.values()).pop()

# Neural Network Train
nn1 = NeuralNetwork()
nn1.train(inputs, targets)
nn1.saveTrain()

# Network Prediction
print(nn1)
print(nn1.predict([1,0,0,1]))
print(nn1.predict([0,0,1,0]))
print(nn1.predict([1,0,1,0]))