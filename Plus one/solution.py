def plus_one(digits):   
    for i in range(-1, len(digits)-1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits
nums = [9,9,9]
print(plus_one(nums))