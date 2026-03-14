from numpy import*

def sigmoid(x):
    return 1/(1+exp(-x))

class Neuron:
    def __init__(self,weights,bias):
        self.weights=weights
        self.bias=bias
    def feedforward(self,inputs):
        total=dot(self.weights,inputs)+self.bias
        return sigmoid(total)
    
class NeuralNetwork:
    def __init__(self):
        weights=array([0,1])
        bias=0
        self.n1=Neuron(weights,bias)
        self.n2=Neuron(weights,bias)
        self.o1=Neuron(weights,bias)
    def feedforward(self,x):
        out_n1=self.n1.feedforward(x)
        out_n2=self.n2.feedforward(x)
        # the output for o1 are the outputs of n1 and n2
        out_o1=self.o1.feedforward(array([out_n1,out_n2]))
        return out_o1
network=NeuralNetwork()
x=array([1,3])
print(network.feedforward(x))
