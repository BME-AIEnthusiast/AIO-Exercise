# Exercise 2
# Write a function that simulates 3 activation functions.
# "sigmoid", "relu", "elu"

import math

# Given
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def sigmoid(x):     # Implements the sigmoid activation function.
    return 1 / (1 + math.exp(-x))

def relu(x):        # Implements the ReLU activation function.
    return max(0, x)

def elu(x, alpha=0.01): # Implements the ELU activation function
    return x if x >= 0 else alpha * (math.exp(x) - 1)

def exercise2():
    x_input = input("Input x = ")
    
    if not is_number(x_input):
        print("x must be a number")
        return
    
    x = float(x_input)
    
    activation_function = input("Input activation Function (sigmoid| relu| elu) : ").strip().lower()
    
    if activation_function not in ["sigmoid", "relu", "elu"]: #Checks if the provided activation function is one of the supported functions.
        print(f"{activation_function} is not supported")
        return
    
    if activation_function == "sigmoid" :
        result = sigmoid(x)
    elif activation_function == "relu" :
        result = relu(x)
    elif activation_function == "elu" :
        result = elu(x)
    
    print(f"{activation_function}: f({x}) = {result}")

exercise2()
