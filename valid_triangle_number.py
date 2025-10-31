def triangleNumber_brute(nums):
    
    count = 0 
    arr =[]
    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum = nums[i]+nums[j]
            for k in range(j+1,len(nums)):
                if nums[i]==0 or nums[j]==0 or nums[k]==0:
                    continue
                print(nums[i],nums[j],nums[k], sum)
                sum1 = nums[i]+nums[k]
                sum2 = nums[j]+nums[k]
                if nums[k] < sum and (sum1 > nums[j]) and (sum2>nums[i]) :
                    count+=1
                    
                    arr.append([nums[i],nums[j],nums[k]])
    print(arr)
   
   
    
def triangleNumber(nums):
    
    count = 0 
    arr =[]
    nums.sort()
    for i in range(len(nums)):
        l,r= i+1,len(nums)-1
        sum2 = nums[l]+nums[r]
        if sum2 < nums[i]:
            continue
            
        print("i:",i)
        while l < r:
            sum = nums[i]+nums[l]
            sum1 = nums[i]+nums[r]
            sum2 = nums[l]+nums[r]

            if sum2 < nums[i]:
                l=r
                break
        
            small=min(nums[i],nums[l],nums[r])
           # print(nums[i],nums[l],nums[r], "sums:",sum,sum1,sum2)
            
            if sum > nums[r] and (sum1 > nums[l]) and (sum2>nums[i]) :
                count +=1
                arr.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
            else:
                l+=1
                continue            
            #we cud get min out of these & increment that. 
            
            
        
    print(arr,count)
    
nums = [24,3,82,22,35,84,19]




        
triangleNumber(nums)




#Valid Triangle means if you added length of any 2 side it will be
# greater than 3rd side length.

#brute force ? 3 loops. find one num, choose another num, then loop to
# find 3rd num that is greater than sum of the two. 
# are duplicates allowed ? so (2,3,4) (2,3,4) is okay because 2 came two times. but (3,2,4) are not okay. 

# [4,2,3,4,1,5] overthinked, heh.

## woo, can't have 0. ahh, we need to make sure ALL combinations of 2 sides greater than 3rd.


#2,3,4
# 2+3, 2+4, 3+4
#OUTPUT LIMIT exceeded but we got our logic to find triplets

#two-pointers
# sorting ? it wud help yes, cuz we're summing.
# sort -> i fixed, j & k. do the 3 possible sums. whichever side is less, increment that. but because we sort, it's auto that nums[i] wud be least value.