
def binary_search(arr,x,left,right):
    print("hi")
    #base condition
    if right - left > 1:
        #half 
        mid = (left + right)//2
        
        if arr[mid] == x:
            print(mid)
            
        elif arr[mid] > x:
            binary_search(arr,x,left,mid)
        else:
            binary_search(arr,x,mid+1,right)
    else:
        if arr[right]==x:
            print(right)
        else:
            print(left)

def binarysearch(arr,x):
    left = 0 
    right=len(arr)-1

    #iterative, we play with indexes & loop

    while left <= right:
        mid = (left + right)//2
        
        if arr[mid] == x:
            return mid
         
        if arr[mid]>x:
            right=mid-1  
        
        if arr[mid]<x:
            left = mid+1

    return -1


def searchRange( nums, target):
    left, right = 0, len(nums)

    first_index,last_index = [-1,-1]
    # try to find leftmost index 
    # while left < right:
    #         mid = (left + right)//2 
    #         if nums[mid] >= target:
    #             right = mid
    #         else:
    #             left = mid + 1 
    # print(left)
    # if nums[left-1] == target:
    #         first_index = left-1

# try to find last index
    # left, right = 0, len(nums)

    while left < right:
            mid = (left+right)//2 
            if nums[mid] >=  target:
                right = mid
            else:
                left = mid + 1
    # if nums[left-1] == target:
    #         last_index = left -1

    # return [first_index,last_index]
            

# half array, then based on it, half forward or half backward

# arr = [4,9,11,17,21,25,29,32,38]

# binarysearch(arr, 32)

# test = [4,5,5,6,6,7,7]
# print(searchRange(test,6)
# )
#iterative version 



# I could go from one direction(lets say left) & then check if right a pair or not ? 



def findMin(nums):
        # so use divide & conquer again & make sure i get it /
        left,right = 0,len(nums)

        while left < right: 
            mid = (left+right) // 2
            
            if mid +1 < len(nums):
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
            elif mid -1> -1 and nums[mid-1] > nums[mid]:
                    return nums[mid]
            else:
                left=mid+1
        return nums[0]
            
# nums=[11,12,13,14]
# print(findMin(nums))




def search( nums,target):
        
        left,right = 0, len(nums)-1

        mid = (left+right)//2
        if nums[mid]==target:
            return mid

        while left <= right:
            mid = (left+right)//2
            print(mid,"mid")
            if nums[left] <= nums[mid]:
                #left is sorted
                if nums[left]<= target < nums[mid]:
                    if mid -1 > -1:
                        right = mid-1
                    else:
                        right = mid
                else:
                    left = mid+1
            else:
                #right hand is sorted
                if nums[mid]< target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            print(left,right,mid,"l r m")
        if nums[left] == target:
            return left
        else:
            return -1
        
        
# nums= [3,1]

# print(search(nums,0))


def searchMatrix( matrix,target):
        if len(matrix)==0:
            return False

        r = len(matrix[0])
        c = len(matrix)

        left,right = 0, r*c-1

        while left <= right:
            mid = (left+right)//2
            print(mid," mid")
            mid_r = mid//r
            
            mid_c = mid - r*(mid//r) 
            print(mid_r,mid_c," mid_r, mid_c")
            print(matrix[mid_r][mid_c])
            if matrix[mid_r][mid_c] == target:
                return True

            if matrix[mid_r][mid_c] < target:
                left = mid +1
            else:
                right = mid-1
        return False
    
# matrix =[[1],[3],[5]]
# target = 0
# print(searchMatrix(matrix,target))



#  69. Sqrt BINARY SEARCH METHOD
def mySqrt( x: int) -> int:
        if x == 0:
            return 0
        if x <=2:
            return 1
        left,right = 2,x//2
        if left <= right:
            return left
        while left < right:
            middle = (left+right)//2
            if middle*middle == x:
                return middle 
            print(left,middle,right)
            if  middle*middle > x: 
                right = middle 
            else:
                left = middle + 1  
        return left-1
 
 
# print(mySqrt(3))


# brute force

def mySqrt_bf( x: int) -> int:
        if x == 0:
            return 0
        if x <=2:
            return 1
        left,right = 2,x//2

        while left < right:
            if left*left <= x <= (left+1)*(left+1):
                return left 
            left += 1
 



def findMin_dupl( nums):
        # duplicate will only change our equality signs
    left,right = 0, len(nums)-1

    while left < right:
        mid = (right + left)//2
        print(left,right,mid)
        if nums[mid] < nums[right]:
                right= mid
        elif nums[mid] == nums[right]:
                left = mid 
        else:
             left = mid +1
    return nums[left]

nums = [1,3,3]
print(findMin_dupl(nums))