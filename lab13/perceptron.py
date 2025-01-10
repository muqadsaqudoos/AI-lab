
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron

def plot_decision_boundary(X, y, model, title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Paired)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', s=20, cmap=plt.cm.Paired)
    plt.title(title)
    plt.show()

def perceptron_task():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])  

    model = Perceptron(max_iter=1000, eta0=0.1, random_state=0)
    model.fit(X, y)  

    plot_decision_boundary(X, y, model, title="Perceptron Decision Boundary")

def xor_nn_task():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0]) 

    model = MLPClassifier(
        hidden_layer_sizes=(4,),  
        activation='relu',       
        max_iter=5000,          
        learning_rate_init=0.1, 
        random_state=0          
    )
    model.fit(X, y) 

    plot_decision_boundary(X, y, model, title="Neural Network Decision Boundary for XOR")

def main():
    print("Running Perceptron Task...")
    perceptron_task()
    print("Running XOR Neural Network Task...")
    xor_nn_task()

main()
