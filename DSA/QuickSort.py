def quicksort(arr, low, high):
    if low < high: 
           pivot_index = partition(arr, low, high)
           quicksort(arr, low, pivot_index-1)
           quicksort(arr, pivot_index+1, high)

def partition(arr, low, high):
    i=low
    j= high-1
    pivot= arr[high]
    while True:
        while  i<high and arr[i]<=pivot:
            i +=1
        while j > low and arr[j]>=pivot:
            j-= 1
        if i<j:
            arr[i],arr[j]= arr[j],arr[i]
        else:
            break
    arr[i],arr[high]=arr[high],arr[i]
    return i

arr= [20,30,25,12,6,34,90,4,56]
quicksort(arr,0, len(arr)-1)
print("sorted array:",arr)
