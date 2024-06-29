import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

start = time.time()
print(factorial(998))
end = time.time()
print (end - start)


def factoriall(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

start = time.time()
print(factoriall(998))
end = time.time()
print (end - start)  




      
        