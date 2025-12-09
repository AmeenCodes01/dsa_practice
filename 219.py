# 219. Contains Duplicate II

def duplicates(nums,k):
    
    count = {}
    l = 0 
    
    for i,n in enumerate(nums):
            
        #check if window larger than k. 
        if (i - l) > k:
            del count[nums[l]]
            l+=1
    
        # we'll add n always. 
        if n not in count:
            count[n]=i 
        elif count[n] != i:  #if in window, check fr same index.
            return True 
    return False
    
print(duplicates([1,2,3,1,2,3],k=2))   
    
# [1,2,3,1] k=2
# [1,2,3,1], now l will update  
#  [2,3,1] check if 1 exist in n. doesn't, add to count
# loop done, return FaLSE