prices = [7,6,4,3,1]
total = [0]
j = 0
while j < len(prices):
    for num in prices[j: ]:
        if prices[j] < num: 
            val = num - prices[j]
            total.append(val)
    j = j + 1 
print(max(total))