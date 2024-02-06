def trailing_zeroes(N): 
  factorial = 1
  x = 0
  for i in range(1,N+1):
      factorial *= i 
      i += 1 
  while str(factorial)[-1] == "0":
      factorial //= 10
      x += 1
  return x 
