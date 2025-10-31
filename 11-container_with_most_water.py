
#brute force
def maxArea_brute( height):
        if len(height)==2:
            return min(height)
        #brute force
        # find all possible areas, then return the larget. 

        #to find areas, have 2 loops. if i,j then area = abs(height[i]-height[j])*(j-i). add it to array. then return max of the array. 
        areas = []

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area= min(height[i],height[j])*(j-i)
                print(i,j,area)
                areas.append(area)
        print(areas,"areas")
        return max(areas)
    
    
def maxArea( height):
       # height.sort()
        maxArea=0
        i,j=0,len(height)-1
        while i < j:
            h = min(height[i],height[j])
            area= h*(j-i)
            print(i,j,area)
            maxArea=max(area,maxArea)
            if h == height[i]:
                i+=1
            else:
                j-=1
        return maxArea
nums = [1,8,6,2,5,4,8,3,7]
print(maxArea(nums))

#sort them ? no, cuz we need indexes fr width.
# use two pointers instead of nested loop. if area < maxArea, move l, else move r. 

# what impacts area ? min-height, so that shud be condition to move pointer.