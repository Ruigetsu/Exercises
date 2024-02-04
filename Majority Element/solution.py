nums = [2,2,1,1,1,2,2]
k = len(nums)
for num in nums: 
    counts = nums.count(num)
    if counts > k/2: 
        major = num 
print(major)