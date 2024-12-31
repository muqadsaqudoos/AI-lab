import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))
    
def cross_entropy_loss(y_true, y_pred):
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)  
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def gradient_descent(X, y, weights, learning_rate, iterations):
    m = len(y)
    for i in range(iterations):
        predictions = sigmoid(np.dot(X, weights))
        gradient = np.dot(X.T, (predictions - y)) / m
        weights -= learning_rate * gradient
    return weights

def predict(X, weights):
    probabilities = sigmoid(np.dot(X, weights))
    return (probabilities >= 0.5).astype(int)

def logistic_regression(X, y, learning_rate=0.01, iterations=1000):
    X = np.hstack((np.ones((X.shape[0], 1)), X)) 
    weights = np.zeros(X.shape[1]) 
    weights = gradient_descent(X, y, weights, learning_rate, iterations)
    return weights

def evaluate(y_true, y_pred):
    accuracy = np.mean(y_true == y_pred)
    return accuracy

def plot_decision_boundary(X, y, weights):
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k', s=20)
    x_values = [np.min(X[:, 0]), np.max(X[:, 0])]
    y_values = -(weights[0] + np.dot(weights[1], x_values)) / weights[2]
    plt.plot(x_values, y_values, label='Decision Boundary')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()

def main():
    data = np.array([
        [0.1, 1.1, 0],
        [1.2, 0.9, 0],
        [1.5, 1.6, 1],
        [2.0, 1.8, 1],
        [2.5, 2.1, 1],
        [0.5, 1.5, 0],
        [1.8, 2.3, 1],
        [0.2, 0.7, 0],
        [1.9, 1.4, 1],
        [0.8, 0.6, 0],
    ])

    X = data[:, :-1]
    y = data[:, -1]
    X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    weights = logistic_regression(X, y, learning_rate=0.1, iterations=1000)
    predictions = predict(np.hstack((np.ones((X.shape[0], 1)), X)), weights)
    accuracy = evaluate(y, predictions)
    print(f'Accuracy: {accuracy:.2f}')

    plot_decision_boundary(X, y, weights)

main()