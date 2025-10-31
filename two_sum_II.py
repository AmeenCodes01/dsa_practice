def twoSum(numbers,target):
    #it can be solved by hashmap, heh. add all to hashmap, then search thru hashmap fr target-number
    
    l,r=0,len(numbers)-1
    
    while l < r:
        if numbers[l]+numbers[r] > target:
            r-=1
        elif numbers[l]+numbers[r]==target:
            print(numbers[l],numbers[r],l,r)
            return [l+1,r+1]
        else:
            l+=1
        
numbers = [2,3] 
print(twoSum(numbers=numbers,target=5))

##ehh, medium ? luckyy