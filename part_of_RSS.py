from random import randint
import matplotlib.pyplot as plt
X = [[1,2],
     [3,4],
     [7,8],
     [9,10],
     [5,2],
     [3,4],
     [2,5],
     [7,2],
     [3,9],
     [10,2]]

Y = [0,0,0,0,0,
     1,1,1,1,1]

def line(x, k, b) -> float:
    return k * x + b

def calc_RSS(X, k, b):
    RSS = 0
    for i in X:
        RSS += (i[1] - line(i[0], k, b)) ** 2
    return RSS

def grad_RSS(X, k, b):
    for i in X:
        grad_k = 0
        grad_k += (-2 * i[1] * i[0]) + (2 * k * (i[0]**2)) + (2 * i[0] * b )
        grad_b = 0
        grad_b += (-2 * i[1]) + (2 * k * i[0]) + (2 * b )
    return grad_k, grad_b

print(grad_RSS(X, randint(0,10), randint(0,10)))