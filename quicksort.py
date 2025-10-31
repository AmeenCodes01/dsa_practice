
def quicksort(arr,left, right):
    # if one, return same element
    if right > left:
        #pivot 
        partition_pos = partition(arr,left,right)
        quicksort(arr,left,partition_pos-1 )
        quicksort(arr,partition_pos+1,right )
 
def partition(arr,left,right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i<j:
        # have to check if i within index of arr
        while i <right and arr[i] < pivot:
            i+=1
        while j>left and arr[j] > pivot:
            j-=1
        if i < j:
            arr[i],arr[j]= arr[j], arr[i] #constant

    if arr[i] > pivot:
        arr[i], arr[right] = pivot, arr[i]    #constant

    return i   


arr = [22,11,88,66,55,77,34]
quicksort(arr,0,len(arr)-1)

print(arr)
