import matplotlib.pyplot as plt
import time

def fib(n):
    if n <= 1:
       return n
    else:
       return(fib(n-1) + fib(n-2)) 

def plotFunc(func, n):
    result = []
    for i in range(n):
        start = time.time()
        func(i)
        end = time.time()
        result.append(end - start)
    return result

plt.plot(plotFunc(fib, 10), color='red')
plt.xlabel('n')
plt.ylabel('time')
plt.show()
print(fib(6))
