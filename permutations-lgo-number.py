#! /usr/bin/python
# computes the number of a permutation in the lexicographic order
# see permutations-lgo.py

from math import factorial

def renumber(p,  excludedIndex):
  for i in range(len(p)):
    if p[i] > excludedIndex:
      p[i] -= 1
  return p

def computePermNumber(p):
  if len(p) == 1:
    return 0
  elif len(p) == 2:
    if p[0] > p[1]:
      return 1
    else:
      return 0
  else:
    return p[0] * factorial(len(p) - 1) + computePermNumber(renumber(p[1:],  p[0]))

print computePermNumber(eval(raw_input("Enter permutation (like [2, 0, 1]): ")))

