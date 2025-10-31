def threesum(nums):
    ""
    ans=[ ]
    nums.sort()
    #now we need to figure out how to skip duplicates.
    for i in range(len(nums)-2):
        j,k=i+1,len(nums)-1
        
        while j < k :
            if nums[i] == nums[k]:
                continue
            sum = nums[i]+nums[j]+nums[k]
            if sum < 0:
                j+=1
            elif sum > 0:
                k-=1
            else:
                
                a = [nums[i],nums[j],nums[k]]
                # a.sort()
                # if a not in ans:
                #     ans.append(a)
                while j < k and nums[j]==nums[j+1]:  
                    j+=1
                while j<k and nums[k] ==nums[k-1]:
                    k-=1
                j+=1
                k-=1
    return ans

print(threesum([0,0,0,-1,1,0]))


# time limit exceeded, we need to optimise. on every iteration, all possible combinations are found so nums[i] should never be repeated, creates duplicates.
# when we find a sum, only j changes but not i & k. Now, we know only 1 unique solution exists if 2 nums are fixed. so we'll move j until nums[j] is not that exact solution. 
# that will then trigger k to move. 