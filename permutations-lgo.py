#! /usr/bin/python
# generator of permutations in lexicographic order

def genPermutations(N):
  def swap(p, j,  k):
    t = p[j]
    p[j] = p[k]
    p[k] = t
  def reverse(p,  iFrom,  iTo):
    for i in range((iTo - iFrom) / 2):
      swap(p,  iFrom + i,  iTo - i - 1)
  
  p = range(N)
  while True:
    yield list(p)
    i1 = N-2
    i2 = N-1
    while i1 >= 0 and p[i1] > p[i2]:
      i2 -= 1
      if i2 == i1:
        i1 -= 1
        i2 = N-1
    
    if i1 >= 0:
      swap(p,  i1, i2)
      reverse(p,  i1 + 1,  N)
    else: 
      break


for p in genPermutations(int(raw_input("Length of permutations: "))):
  print p

