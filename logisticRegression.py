import numpy as np
import math
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def model(X, theta):
    return sigmoid(np.dot(X, theta))

def cost_function(X, y, theta):
    m = len(y)
    h = model(X, theta)
    return -1/m * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))

def grad(X, y, theta):
    m = len(y)
    h = model(X, theta)
    return 1/m * np.dot(X.T, (h - y))

def gradient_descent(X, y, theta, learning_rate, n_iterations):
    cost_history = np.zeros(n_iterations)
    for i in range(n_iterations):
        theta = theta - learning_rate * grad(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
    return theta, cost_history
    