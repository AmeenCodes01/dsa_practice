# 128. Longest Consecutive Sequence

def longest_seq(nums):
    maxL = 0
    nums = set(nums)
  
    for n in nums:
        if n-1 not in nums:
                 
            #go full forward
            k= n
            while k+1 in nums:
                k+=1
            maxL=max(maxL,k-n+1)
    return ( maxL)
        
        
        

print(longest_seq([0,3,7,2,5,8,4,6,0,1]))
    # go as back as possible, then count forward.            