# Exercise 3
# Write 4 functions to evaluate the following functions.
# "sin(x)", "cos(x)", "sinh(x)", "cosh(x)"

import math

def factorial(k):
    if k == 0 or k == 1:
        return 1
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result

def approx_sin(x, n):
    sin_x = 0
    for i in range(n):
        term = ((-1)**i * x**(2*i + 1)) / factorial(2*i + 1)
        sin_x += term
    return sin_x

def approx_cos(x, n):
    cos_x = 0
    for i in range(n):
        term = ((-1)**i * x**(2*i)) / factorial(2*i)
        cos_x += term
    return cos_x

def approx_sinh(x, n):
    sinh_x = 0
    for i in range(n):
        term = (x**(2*i + 1)) / factorial(2*i + 1)
        sinh_x += term
    return sinh_x

def approx_cosh(x, n):
    cosh_x = 0
    for i in range(n):
        term = (x**(2*i)) / factorial(2*i)
        cosh_x += term
    return cosh_x

# Ví dụ sử dụng:
x = 3.14
n = 10

print("approx_sin(x=3.14, n=10) =", approx_sin(x, n))
print("approx_cos(x=3.14, n=10) =", approx_cos(x, n))
print("approx_sinh(x=3.14, n=10) =", approx_sinh(x, n))
print("approx_cosh(x=3.14, n=10) =", approx_cosh(x, n))
