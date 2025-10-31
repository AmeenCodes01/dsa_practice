# 153. Find Minimum in Rotated Sorted Array

def find_min(nums):
    ""
    l,r = 0,len(nums)-1
    
    while l < r:
        mid = (l+r)//2
        
        if nums[mid] < nums[r]:
            r = mid 
            # we need to find min in this subarray now. 
        else:
            l = mid + 1 
    return nums[l] 

print(find_min([4,5,6,7,0,1]))