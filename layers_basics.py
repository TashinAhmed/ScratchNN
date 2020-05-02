import numpy as np
inputs = [[1,2,3,4],
          [2,3,4,5],
          [6,7,8,9]]

weights1 = [[1,2,3,4],
           [2,3,4,5],
           [4,5,6,7]]


weights2 =[[1,2,4],
          [2,3,4],
          [6,8,9]]

biases1 = [2,3,4]
biases2 = [3,4,1]

layer1_out = np.dot(inputs, np.array(weights1).T) + biases1
layer2_out = np.dot(layer1_out, np.array(weights2).T) + biases2

print(layer1_out)
print(layer2_out)