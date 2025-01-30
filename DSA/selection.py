arr= [20,30,25,12,6,34,90,4,56]
num= len(arr)
for i in range(num-1):
    min_index= i
    for j in range(i+1, num):
        if arr[j]< arr[min_index]:
            min_index = j
    value= arr.pop(min_index)
    arr.insert(i, value)
print("sorted array:",arr)