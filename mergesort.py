
# keep breaking array until it's only one element. 
    # break in middle
# rejoin elements & keep going up

def merge_sort(arr,left,right):

    if left<right: #to check if more than 2 elements
        print(arr[left:right])
        middle = (left+right)//2
        print(middle, "Middle")
        merge_sort(arr,left,middle)
        merge_sort(arr,middle+1,right)
        merge(arr,left,middle,right)
        #rejoin now
        

def merge(arr,left,middle,right):
    print(left,middle,right, " left,midmright")
    i = 0
    j=0
    k=left
    left_arr = arr[left:middle+1]  
    right_arr = arr[middle+1:right+1]
    print(left_arr," left_arr")
    while i < len(left_arr) and j<len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k]=left_arr[i]
            i+=1
        else:
            arr[k]= right_arr[j]
            j+=1
        k +=1

    
    if i <len(left_arr):
        for n in range(i,len(left_arr)):
            arr[k]= left_arr[n]
    if j <len(right_arr):
        for n in range(j,len(right_arr)):
            arr[k]= right_arr[n]


arr = [38, 27, 43, 10]
merge_sort(arr,0,len(arr)-1)
print(arr)




#  if n >=0:
#                 if n <= target:
#                     if (target-n) in count:
#                         return [i, count[target-n]]
#                 if n > target:
#                     if (n-target) in count:
#                         return [i, count[-target+n]]
                        
#             if n <0:
#                 n=n*-1
#                 if n