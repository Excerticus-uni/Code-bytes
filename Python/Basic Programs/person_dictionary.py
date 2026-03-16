# store information in a dictionary
person_dict = {"name" : "John", "age" : 23, "is_student" : True, "sleep_late" : False, "descriptive_message" : "loves programming"}

# print name and message
print(person_dict["name"])
print(person_dict["descriptive_message"])

# update the message and print updated info
person_dict["descriptive_message"] = "I hate programming"
print(person_dict["descriptive_message"])

# add new attribute and print
person_dict["favourite_colour"] = "pink"
print(person_dict["favourite_colour"])