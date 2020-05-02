import numpy as np
inputs = [[1,2,3,4],
          [2,3,4,5],
          [6,7,8,9]]

weights = [[1,2,3,4],
           [2,3,4,5],
           [4,5,6,7]]

biases = [2,3,4]

output = np.dot(inputs, np.array(weights).T) + biases

print(output)