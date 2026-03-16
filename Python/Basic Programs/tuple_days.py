# creating my tuple
days_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday")

# print first and last item
print(days_tuple[0])

print(days_tuple[(len(days_tuple) - 1)])

# print all items except last item
x = slice(0, (len(days_tuple) - 1))
print(days_tuple[x])

'''
days_tuple[0] = "Help"

causes an error as tuple cannot be changed once initialized, this includes
no adding, changing, removing or any other operations that may alter its values
'''
