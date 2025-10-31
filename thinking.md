# 34. Find First and Last Position of Element in Sorted Array

[1,3] (1)
=> [0,0]
 
 found 1, checked next index, == 1 ? [mid,mid+1] : [mid,mid]
  check prev index, <0 ? [mid,mid] 

[1,1,3] (1)
=> [0,1]

[1,3,3] (3)
=> [2,3]

but it could have any number of repeating elements. 
run once from right
run once from left 

[right,left]

[5,7,7,8,8,10] (8)

mid = 0 + 5) // 2 = 2

7>8 ?
[7,8,8,10]

8 
found.

[5,7,7,8,8,10] (10)

mid = 5 - (5)//2 = 3

8>10 ? [8,10]


Example 2:
array = [1,2,2,2,3,4]
target = 2
binary_search(array, lambda mid: array[mid] > target) --> 4
"""
def binary_search(array, condition):
    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) 
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

mid = 0 + (6-0) //2 == 3 
    if (arr[mid]=2 > 4):
        right = 2
    else:
    left = 3

[2,3,4]

mid = 3 + (6-3)//2 = 2

[4]

does this mean our normal binary search returns right most always then ?



# find-minimum-in-rotated-sorted-array

so we need to find minimum using binary search. binary search is used on sorted array so first element would be ans automatically.

// so we need to find min value first, then 




✅ So your code fails because it tries to “catch the pivot directly” by checking neighbors, instead of gradually shrinking the search range. That shortcut only works in special cases.

Binary search shrinks searching range. use right & left.

