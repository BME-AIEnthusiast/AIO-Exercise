# Exercise 3
# Write a function to select the regression loss function to calculate loss:
# "MAE", "MSE", "RMSE"


import random
import math

# Given function to check if a value is a number
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def calculate_mae(predictions, targets):
    n = len(predictions)
    mae = sum(abs(pred - target) for pred, target in zip(predictions, targets)) / n
    return mae

def calculate_mse(predictions, targets):
    n = len(predictions)
    mse = sum((pred - target) ** 2 for pred, target in zip(predictions, targets)) / n
    return mse

def calculate_rmse(predictions, targets):
    mse = calculate_mse(predictions, targets)
    rmse = math.sqrt(mse)
    return rmse

def exercise3():
    num_samples_input = input("Input number of samples ( integer number ) which are generated : ")

    if not is_number(num_samples_input):
        print("number of samples must be an integer number")
        return

    num_samples = int(num_samples_input)

    loss_name = input("Input loss name (MAE, MSE, RMSE): ").strip().upper()

    predictions = []
    targets = []

    for i in range(num_samples):
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)
        predictions.append(pred)
        targets.append(target)
        print(f"loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}")

    if loss_name == "MAE":
        loss = calculate_mae(predictions, targets)
    elif loss_name == "MSE":
        loss = calculate_mse(predictions, targets)
    elif loss_name == "RMSE":
        loss = calculate_rmse(predictions, targets)
    else:
        print(f"{loss_name} is not supported")
        return

    print(f"final {loss_name}: {loss}")


exercise3()
