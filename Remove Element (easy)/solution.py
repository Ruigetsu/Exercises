nums = input("Введите числа через запятую: ")
nums_list = nums.split(",")
val = int(input("Введите val: "))
new_list = []
for num in nums_list: 
    num1 = int(num)
    if num1 != val:
        new_list.append(num1)
k = len(new_list)
print(f"nums = {new_list} \t k = {k}")