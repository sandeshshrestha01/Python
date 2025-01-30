arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]

arrange = []
another = []

# Arrange elements of arr1 based on the order in arr2
for num in arr2:
    print(num)
    arrange.extend([num]* arr1.count(num))

# Add elements not in arr2, sorted in ascending order
another = [num for num in arr1 if num not in arr2]
arrange.extend(sorted(another))

print(arrange)
