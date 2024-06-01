def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True
            else:
                continue
            

print(containsNearbyDuplicate([1,2,3,1,2,3], 2))