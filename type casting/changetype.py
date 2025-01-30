num_string='12'
num_integer=23
print("Data type of num_string before type casting:",type(num_string))

num_string=int(num_string)
print("Data type of num_string before type casting:",type(num_string))

num_sum= num_integer + num_string
print("sum:",num_sum)
print("Data type :",type(num_sum))