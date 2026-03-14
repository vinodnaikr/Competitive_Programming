from numpy import*

def sigmoid(x):
    # activation function
    return 1/(1+exp(-x))

class Neuron:
    def __init__(self,weights,bias):
        self.weights=weights
        self.bias=bias

    def feedforward(self,inputs):
        total=dot(self.weights,inputs)+self.bias
        return sigmoid(total)

weights=array([0,1])
bias=4
n=Neuron(weights,bias)

x=array([2,3])
print(n.feedforward(x))