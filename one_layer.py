import numpy as np 

def single_layer():

    inputs = [1,2,3,4]
    weights = [[1,2,3,4],
            [2,3,4,5],
            [3,4,1,2]]
    biases = [2,3,5]

    output = np.dot(weights, inputs) + biases
    print(biases)