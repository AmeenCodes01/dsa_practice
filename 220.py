#220. Contains Duplicate III
# MY FIRST HARD, LESGOOO

def containsNearbyAlmostDuplicate(nums,indexDiff,valueDiff):
    l=0
    #looked at first hint. we make windows that satisfy indexDiff, then check first 2. if they don satisfy, whole window won't satisfy cuz it's the smallest sum possible.
    if len(nums)==2:
        if abs(nums[0])-abs(nums[1]) <= valueDiff:
            return True
        else:
            return False
            
    for r,n in enumerate(nums):
        print(r,l)
        if (r-l) == indexDiff or r==(len(nums)-1): 
            temp = sorted(nums[l:r+1])
            print(temp)
            i,j = 0,1
            while j < len(temp):
                if abs(temp[i]-temp[j])<=valueDiff:
                            return True
                else:
                    i
                    if i==j:
                        i+=1
                        j+=1
                    
                    
                
            l+=1
            
    return False

print(containsNearbyAlmostDuplicate([1,2,2,3,1],3,0))