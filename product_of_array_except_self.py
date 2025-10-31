def productExceptSelf_(nums):
        # [1,2,3,4] so for 3 we wud need [1*2] * [4]  
        # prefix sum(product). for suffix. [5,4,3,2,1] --> [4 ,4*3 ,4*3*2 ,4*3*2*1]
        # [1, 1*2, 1*2*3, 1*2*3*4, 1*2*3*4*5]
        prefix = [0]*(len(nums))
        prefix[0]= nums[0]
        for i in range(1,len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
        print(prefix)
        n = len(nums)
        suffix = [0] * n
        suffix[-1] = nums[-1]  # last element

        for i in range(n-2, -1, -1):  # go backwards
            suffix[i] = nums[i] * suffix[i+1]

        print(suffix)
        nums[0]=suffix[1]
        nums[-1]=prefix[-2]
        #nums = [24,]
        for i in range(1,len(nums)-1):
            nums[i] = prefix[i-1]*suffix[i+1]
        print(nums)
nums = [4,3,2,1,2]
#productExceptSelf(nums)

[1,2,3,4]
[1,2,6,24]
[24,24,12,4]

# def productExceptSelf(nums):
#         # [1,2,3,4] so for 3 we wud need [1*2] * [4]  
#         # prefix sum(product). for suffix. [5,4,3,2,1] --> [4 ,4*3 ,4*3*2 ,4*3*2*1]
#         # [1, 1*2, 1*2*3, 1*2*3*4, 1*2*3*4*5]
        
#         for i in range(1,len(nums)):
#             nums[i] = nums[i] * nums[i-1]
        
#         n = len(nums)
#         suffix = [0] * n
#         suffix[-1] = nums[-1]  # last element

#         for i in range(n-2, -1, -1):  # go backwards
#             suffix[i] = nums[i] * suffix[i+1]

#         print(suffix)
#         nums[0]=suffix[1]
       
#         #nums = [24,]
#         for i in range(1,len(nums)-1):
#             nums[i] = prefix[i-1]*suffix[i+1]
#         print(nums)
# nums = [4,3,2,1,2]
# productExceptSelf(nums)

# [1,2,3,4]

# #this is nums now
# [1,2,6,24]

# #result [24,12,8,6]
# [24,24,12,4]



