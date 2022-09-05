# -*- coding: utf-8 -*-
"""PCA4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OQ36RwggKj4343CoF5UToIQ9qaf9WFuG
"""

import matplotlib.pyplot as plt
import numpy as np
import time

# O(n)
def m01(n):
  round = 0
  sum = 0
  while round < n:
    sum = sum + 1
    round = round + 1
  return sum

# O(n)
def m02(n):
  round = 0
  sum = 0
  while round < n:
    sum = sum + 1
    round = round + 2
  return sum

# O(n^2)
def m03(n):
  round1s = 0
  sum = 0
  while round1s < n:
    round2s = 0
    while round2s < n:
      sum = sum + 1
      round2s = round2s + 1
    round1s = round1s + 1
  return sum

# O(n^2)
def m04(n: int):
    round1s = 0
    sum = 0
    while round1s < n:
        round2s = 0
        while round2s < n:
            sum += 1
            round2s += 10
        round1s += 20
    return sum

# O(2n)
def m05(n: int):
    round1s = 0
    sum = 0
    while round1s < n:
        sum += 1
        round1s += 1

    round2s = 0
    while round2s < n:
        sum += 1
        round2s += 1
    return sum

# O(n^3)
def m06(n: int):
    round1s = 0
    sum = 0
    while round1s < n:
        round2s = 0
        while round2s < (n*n):
            sum += 1
            round2s += 1
        round1s += 1
    return sum

# O(n^2)
def m07(n: int):
    round1s = 0
    sum = 0
    while round1s < n:
        round2s = 0
        while round2s < round1s:
            sum += 1
            round2s += 1
        round1s += 1
    return sum

# O(n^2)
def m08(n: int):
    round1s = 0
    sum = 0
    while round1s < n:
        round2s = 0
        while round2s < (100*round1s):
            sum += 1
            round2s += 1
        round1s += 1
    return sum

# O(n^4)
def m09(n: int):
    round1s = 0
    sum = 0
    while round1s < n:
        round2s = 0
        while round2s < (n*n):
            round3s = 0
            while round3s < round2s:
                sum += 1
                round3s += 1
            round2s += 1
        round1s += 1
    return sum

# O(log2 (n))
def m10(n: int):
    rounds = 1
    sum = 0
    while rounds < n:
        sum += 1
        rounds = rounds*2
    return sum

# O(log2 (n))
def m11(n: int):
    i = n
    sum = 0
    while i > 0:
        sum += 1
        i = i/2
    return sum

# O(log(n))
def m12(n: int):
    rounds = 1
    sum = 0
    while rounds < n:
        sum += 1
        rounds = 10*rounds
    return sum

def plotFunc(func, n):
  result = []
  for i in range(n):
    start = time.time()
    func(i)
    end = time.time()
    result.append(end - start)
  return result

n = 100
plt.plot(plotFunc(m01, n), color='red')
plt.plot(plotFunc(m02, n), color='orange')
plt.plot(plotFunc(m03, n), color='yellow')
plt.plot(plotFunc(m04, n), color='green')
plt.plot(plotFunc(m05, n), color='cyan')
plt.plot(plotFunc(m07, n), color='magenta')
plt.plot(plotFunc(m10, n), color='gray')
plt.plot(plotFunc(m12, n), color='salmon')
plt.plot(plotFunc(m12, n), color='salmon')
plt.xlabel('n')
plt.ylabel('time')
plt.show()

n = 10
plt.plot(plotFunc(m06, n), color='blue')
plt.plot(plotFunc(m08, n), color='purple')
plt.plot(plotFunc(m09, n), color='black')
plt.plot(plotFunc(m11, n), color='pink')
plt.xlabel('n')
plt.ylabel('time')
plt.show()

import random
import math
import matplotlib.pyplot as plt
import numpy as np
import time

class Point:
  def __init__(self, x_init, y_init):
    self.x = x_init
    self.y = y_init
  def get_x(self):
    return self.x
  def get_y(self):
    return self.y
  def __repr__(self):
    return "".join(["(", str(self.x), ",", str(self.y), ")"])
  def __str__(self):
    return "(%s,%s)" % (self.x, self.y)
  def getCord(self):
    return [self.x,self.y]
  def distance(self, other):
    x = (self.x - other[0]) ** 2
    y = (self.y - other[1]) ** 2
    return math.sqrt(x+y)

def findClosest(n):
  smallest = 9999999
  points = []
  fPoint = []
  sPoint = []
  #Gen num
  for i in range(n):
    randx = random.randint(-n,n)
    randy = random.randint(-n,n)
    points.append(Point(randx,randy))
  # print(points)
  for i in range(n-1):
    for j in range(len(points) - 1):
      # print(f"Point 1 is {points[i].getCord()}")
      # print(f"Point 2 is {points[j + 1].getCord()}")
      # print("=============")
      d = points[i].distance(points[j+1].getCord())
      if d < smallest and d != 0:
        smallest = d
        fPoint = points[i].getCord()
        sPoint = points[j + 1].getCord()
  # print(fPoint)
  # print(sPoint)
# findClosest(5)

def plotFunc(func, n):
  result = []
  for i in range(int(n/100)):
    start = time.time()
    func(i * 100)
    end = time.time()
    result.append(end - start)
  return result

plt.plot(plotFunc(findClosest, 2000), color='red')
#plt.plot(plotFunc(findClosest, 500), color='blue')
# plt.plot(plotFunc(findClosest, 1000), color='green')