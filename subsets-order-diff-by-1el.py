#! /usr/bin/python
# enumeration of all subsets of a set in such order that
# consecutive subsets differ by (in/ex)clusion of 1 element

def enumOrdered(n):
  s = [False] * n
  even = True
  while True:
    yield list(s)
    if even:
      s[0] ^= True
    else:
      j = 1
      while j < n and not s[j - 1]:
        j += 1
      if j == n:
        break
      s[j] ^= True
    even ^= True

def toNumberList(set):
  l = []
  for i in range(len(set)):
    if set[i]:
      l.append(i)
  return l


for s in enumOrdered(int(raw_input("Set cardinality: "))):
  print toNumberList(s)

