import random

def partition(massive):    
  x = random.randint(0, len(massive)-1)
  left = []
  right = []
  i = 0
  while i <= x:
        left.append(massive[i])
        i += 1
  while i <= len(massive) - 1:
        right.append(massive[i])
        i += 1
  return left, right

def merge(a, b):
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result += a
    result += b
    return result

def sort(array):
    if len(array) <= 1:
        return array

    a, b = partition(array)
    a = sort(a)
    b = sort(b)
    result = merge(a, b)
    return result
