import numpy as np

def calculate_mean(values):
    return sum(values) / len(values)

def calculate_slope(X, Y, mean_X, mean_Y):
    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X)))
    denominator = sum((X[i] - mean_X) ** 2 for i in range(len(X)))
    return numerator / denominator

def calculate_intercept(mean_X, mean_Y, slope):
    return mean_Y - slope * mean_X

def predict(X, theta_0, theta_1):
    return [theta_0 + theta_1 * x for x in X]

def calculate_mse(Y, Y_pred):
    return sum((Y[i] - Y_pred[i]) ** 2 for i in range(len(Y))) / len(Y)

def fit_linear_regression(X, Y):
    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)
    
    slope = calculate_slope(X, Y, mean_X, mean_Y)
    intercept = calculate_intercept(mean_X, mean_Y, slope)
    
    return intercept, slope

def main():
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 7, 8]
    intercept, slope = fit_linear_regression(X, Y)
    
    print(f"Slope (theta_1): {slope}")
    print(f"Intercept (theta_0): {intercept}")
    
    Y_pred = predict(X, intercept, slope)
    print(f"Predictions: {Y_pred}")
    mse = calculate_mse(Y, Y_pred)
    print(f"Mean Squared Error (MSE): {mse}")

main()
