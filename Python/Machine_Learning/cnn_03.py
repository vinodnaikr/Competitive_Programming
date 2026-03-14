from numpy import*
def sigmoid(x):
    return 1/(1+exp(-x))

def derivative_sigmoid(x):
    fx=sigmoid(x)
    return fx*(1-fx)

def mse_loss(y_true,y_pred):
    return ((y_true-y_pred)**2).mean()


class Neuralnetwork:
    def __init__(self):
        # weights
        self.w1=random.normal()
        self.w2=random.normal()
        self.w3=random.normal()
        self.w4=random.normal()
        self.w5=random.normal()
        self.w6=random.normal()
        # biases
        self.b1=random.normal()
        self.b2=random.normal()
        self.b3=random.normal()
    def feedforward(self,x):
        n1=sigmoid(self.w1*x[0]+self.w2*x[1]+self.b1)
        n2=sigmoid(self.w3*x[0]+self.w4*x[1]+self.b2)
        o1=sigmoid(self.w5*n1+self.w6*n2+self.b3)
        return o1
    def train(self,data,all_y_trues):
        learning_rate=0.1
        epochs=1000

        for epoch in range(epochs):
            for x,y_true in zip(data,all_y_trues):
                # --- feedforward---
                sum_n1=self.w1*x[0]+self.w2*x[1]+self.b1
                n1=sigmoid(sum_n1)

                sum_n2=self.w3*x[0]+self.w4*x[1]+self.b2
                n2=sigmoid(sum_n2)

                sum_o1=self.w5*n1+self.w6*n2+self.b3
                o1=sigmoid(sum_o1)
                y_pred=o1

                # --- calculate partial derivatives
                d_L_d_ypred=-2*(y_true-y_pred)

                # Neuron o1
                d_ypred_d_w5=n1*derivative_sigmoid(sum_o1)
                d_ypred_d_w6=n2*derivative_sigmoid(sum_o1)
                d_ypred_d_b3=derivative_sigmoid(sum_o1)

                d_ypred_d_n1=self.w5*derivative_sigmoid(sum_o1)
                d_ypred_d_n2=self.w6*derivative_sigmoid(sum_o1)

                # Neuron n1
                d_n1_d_w1=x[0]*derivative_sigmoid(sum_n1)
                d_n1_d_w2=x[1]*derivative_sigmoid(sum_n1)
                d_n1_d_b1=derivative_sigmoid(sum_n1)

                # Neuron n2
                d_n2_d_w3=x[0]*derivative_sigmoid(sum_n2)
                d_n2_d_w4=x[1]*derivative_sigmoid(sum_n2)
                d_n2_d_b2=derivative_sigmoid(sum_n2)

                # update weights and biases
                # Neuron n1
                self.w1-=learning_rate*d_L_d_ypred*d_ypred_d_n1*d_n1_d_w1
                self.w2-=learning_rate*d_L_d_ypred*d_ypred_d_n1*d_n1_d_w2
                self.b1-=learning_rate*d_L_d_ypred*d_ypred_d_n1*d_n1_d_b1

                # Neuron n2
                self.w3-=learning_rate*d_L_d_ypred*d_ypred_d_n2*d_n2_d_w3
                self.w4-=learning_rate*d_L_d_ypred*d_ypred_d_n2*d_n2_d_w4
                self.b2-=learning_rate*d_L_d_ypred*d_ypred_d_n2*d_n2_d_b2

                # Neuron o1
                self.w5-=learning_rate*d_L_d_ypred*d_ypred_d_w5
                self.w6-=learning_rate*d_L_d_ypred*d_ypred_d_w6
                self.b3-=learning_rate*d_L_d_ypred*d_ypred_d_b3

                # calculate total loss at the end of each epoch
                if epoch%10==0:
                    y_preds=apply_along_axis(self.feedforward,1,data)
                    loss=mse_loss(all_y_trues,y_preds)
                    print("Epoch %d loss:%.3f"%(epoch,loss))

# training data
data=array([[0,0],
            [0,1],
            [1,0],
            [1,1]])
all_y_trues=array([
    0, #Alice
    1,#Bob
    1,#Charlie
    0 # Diana
    ])
# Train our neural network
network=Neuralnetwork()
network.train(data,all_y_trues)


# make some predictions
emily=network.feedforward(array([0,0])) # 0
frank=network.feedforward(array([0,1])) # 1
print("Emily: %.3f"%(emily))
print("Frank: %.3f"%(frank))
