import numpy as np

def calculate_mean(values):
    return np.mean(values)

def calculate_slope(X, Y, mean_X, mean_Y):
    numerator = np.sum((X - mean_X) * (Y - mean_Y))
    denominator = np.sum((X - mean_X)**2)
    return numerator / denominator

def calculate_intercept(mean_X, mean_Y, slope):
    return mean_Y - slope * mean_X

def predict(X, theta_0, theta_1):
    return theta_0 + theta_1 * X

def calculate_mse(Y, Y_pred):
    return np.mean((Y - Y_pred) ** 2)

def gradient_descent(X, Y, theta_0, theta_1, learning_rate, iterations):
    m = len(X)
    for _ in range(iterations):
        Y_pred = predict(X, theta_0, theta_1)
        gradient_theta_0 = (-2/m) * np.sum(Y - Y_pred)
        gradient_theta_1 = (-2/m) * np.sum((Y - Y_pred) * X)
        theta_0 -= learning_rate * gradient_theta_0
        theta_1 -= learning_rate * gradient_theta_1
        
    return theta_0, theta_1

def fit_linear_regression(X, Y, learning_rate=0.01, iterations=1000):
    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)
    slope = calculate_slope(X, Y, mean_X, mean_Y)
    intercept = calculate_intercept(mean_X, mean_Y, slope)
    theta_0, theta_1 = gradient_descent(X, Y, intercept, slope, learning_rate, iterations)
    
    return theta_0, theta_1

def main():

    X = np.array([30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000])
    Y = np.array([1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500])
    theta_0, theta_1 = fit_linear_regression(X, Y)
    Y_pred = predict(X, theta_0, theta_1)
    mse = calculate_mse(Y, Y_pred)
    
    print(f"Calculated intercept (theta_0): {theta_0}")
    print(f"Calculated slope (theta_1): {theta_1}")
    print(f"Predicted values: {Y_pred}")
    print(f"Mean Squared Error: {mse}")

main()
