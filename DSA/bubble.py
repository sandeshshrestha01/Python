arr= [20,30,25,12,6,34,90,4,56]
num= len(arr)
for i in range(num-1):
    for j in range(num-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]= arr[j+1], arr[j]

print("sorted array:",arr)