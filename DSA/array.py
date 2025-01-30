my_array=[2,1,45,12,45]
arrValu = my_array[0]
for i in range(len(my_array)):
    if(my_array[i] < arrValu):
        arrValu = my_array[i]
print('Lowest value: ',arrValu)