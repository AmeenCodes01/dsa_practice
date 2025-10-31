
def character_replacement(s,k):
    count={}
    maxL = 0
    l=0
    for r in range(len(s)):
        count[s[r]]=count.get(s[r],0)+1
        
        while (r-l+1)-max(count.values()) > k: 
            count[s[l]]=count.get(s[l],0)-1
            l+=1
        maxL=max(maxL,r-l+1)
            
            
    return maxL
            
        

print(character_replacement("AABABBA",1))