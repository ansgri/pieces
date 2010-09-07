#! /usr/bin/python

## symmetric difference of two sets

from random import randint

def symDiff(a, b):
  ia = 0
  ib = 0
  result = []
  while ia < len(a) and ib < len(b):
    if a[ia] > b[ib]:
      result.append(b[ib])
      ib += 1
    elif a[ia] < b[ib]:
      result.append(a[ia])
      ia += 1
    else:
      ia += 1
      ib += 1
  return result + a[ia:] + b[ib:]

###

def makeSet(count, maxNum):
  l = list(set([randint(0, maxNum) for i in range(count)]))
  l.sort()
  return l
  
a = makeSet(20, 50)
print "a = ", a
b = makeSet(20, 50)
print "b = ", b
print "symDiff = ", symDiff(a, b)

