x = float(input("Введите число: "))
y = str(x)
X = x
num_1 = 0
c = 1
num = 0
total = 0
i = 0
z = 1
v = 3
num_2 = 0
k = 10**(len(y)-3)
while i < len(y):
    z *= 10
    num = (x%z)
    num_2 = num/c
    num_1 = num_2*k
    total += num_1
    x -= num    
    i += 1
    v += 1
    k /= 10
    c *= 10
if (total) == X:
    print(f"{X:.0f} is a palindrome")
else:
    print(f"{X:.0f} is not a palindrome")