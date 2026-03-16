person1 = {'name': 'Alice', 'age': 25, 'message': 'Loves programming'}
person2 = {'name': 'Bob', 'age': 30, 'message': 'Enjoys AI'}
person3 = {'name': 'Charlie', 'age': 22, 'message': 'Learning Python'}

# hold dicts in a list
people_list = (person1, person2, person3)

# print message for each dict in list
for i in people_list:
    print(i['message'])

# update message for charlie
people_list[2]['message'] = 'completed python'
for i in people_list:
    print(i['message'])