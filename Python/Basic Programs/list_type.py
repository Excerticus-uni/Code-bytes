# create a list of 4 numbers
numbers_list = [1, 2, 3, 4]

# print first item
print(numbers_list[0])

# print last item
print(numbers_list[3]) 

# change first item and print whole list
print("")
numbers_list[0] = 0
for i in range(0, len(numbers_list)):
    print(numbers_list[i])

# append item to nd of lits and reprint entire list
print("")
numbers_list.append(5)
for i in range(0, len(numbers_list)):
    print(numbers_list[i])