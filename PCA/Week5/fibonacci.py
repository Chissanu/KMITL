import matplotlib.pyplot as plt
import time

def fib(n):
    if n <= 1:
       return n
    else:
       return(fib(n-1) + fib(n-2)) 

#1 1 2 3 5
def fib2(n):
    sequence = []
    if n == 1:
        sequence = [1]
    else:
        sequence = [1,1]
        for i in range(1, n-1):
            sequence.append(sequence[i-1] + sequence[i])
    return sequence[n - 1]

def plotFunc(func, n):
    result = []
    for i in range(n):
        start = time.time()
        func(i)
        end = time.time()
        result.append(end - start)
    return result

print(fib(10))
print(fib2(10))