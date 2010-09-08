# k-subsets

def genKSubsets(k,  n):
  result = []
  s = list(range(k))
  result.append(list(s))
  while True:
    i = 1
    while i <= k and s[-i] >= (n - i):
      i += 1
    if i > k:
      return result
    s[-i] += 1
    base = s[-i]
    while i > 1:
      i -= 1
      base += 1
      s[-i] = base
    result.append(list(s))


