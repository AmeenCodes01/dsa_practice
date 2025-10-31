def lengthOfLongestSubstring(s):
        s= s.replace(" ","")
        if s =="":
            return 1
        l,r = 0,1
        maxLen = 1
        st=s[0]

        while r < len(s):
            print(s[r])
            if s[r] not in st:
                
                st+=s[r]
            else:
                
                while l < r and s[l] == s[r]:
                    l+=1
                print(l)
                st = st[l:]
                
            maxLen = max(len(st),maxLen)
            r+=1
            print(st)
           # print(maxLen)
        if maxLen == 0 :
            return 1 
        else:
            return maxLen
        
s="bcaad"
print(lengthOfLongestSubstring(s))

# []