import numpy as np 

X = [[1,2,3,4],
     [2,3,4,5],
     [6,7,8,9]]

class Layer_Dense:
    def __init__(self, inputs, neurons):
        self.weights = 0.10 * np.random.randn(inputs, neurons)
        self.biases = np.zeros((1,neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

layer1.forward(X)
layer2.forward(layer1.output)

print(layer1.output)
print(layer2.output)