nums = input("Введите числа через запятую: ")
nums_list = nums.split(",")
new_list = []
for num in nums_list:
    if int(num) not in new_list:
        new_list.append(int(num))
k = len(new_list)
print(f"nums = {new_list}, k = {k}")