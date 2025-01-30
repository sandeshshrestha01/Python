list1 =['Apple','banana','Cherry','mango']
newlist =[]

# newlist = [i.lower() for i in list1 ] #lower case
# print(newlist)
newlist =[ i if i != 'banana'else 'orange' for i in list1]
print(newlist)