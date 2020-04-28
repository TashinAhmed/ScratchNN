import numpy as np 

def single_neuron():
    '''
    a neuron have some incoming edges which are it's inputs having corresponding weights and each nodes/neurons has it's own bias which gives the result of the particular neuron = i1*w1+i2*w2+i3*w3+bias [i=input,w=weight]
    '''

    inputs = [1.2,5.1,2.1]
    weights = [1.5,2.5,3.1]
    bias = 3

    output = np.dot(weights, inputs) + bias
    print(output)