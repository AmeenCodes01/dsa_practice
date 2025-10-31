def threeSum(nums):
    nums.sort()
    ans = []
    print(nums)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicate fixed numbers

        j, k = i+1, len(nums)-1
        while j < k:
            print(nums[i],nums[j],nums[k])
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif total < 0:
                j += 1
            else: #>0
                k -= 1
    return ans

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
