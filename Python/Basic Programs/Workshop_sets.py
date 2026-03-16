# create two sets of students
workshop_1 = {"Alice", "Bob", "Charlie"}
workshop_2 = {"Bob", "Diana", "Eve"}

# print those that appear in both
print( workshop_1 & workshop_2)

# print all who attended atleast one workshop
print( workshop_1 | workshop_2)

# print students who attend workshop_1 but not 2
print(workshop_1 - workshop_2)