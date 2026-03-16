# create set of fruits
fruits_set = {"apple", "banana", "orange", "apple", "banana"}

# print set
for i in fruits_set:
    print(i)

# adding kiwi to set
fruits_set.add("kiwi")

# print set
print()
for i in fruits_set:
    print(i)

# remove orange and print
fruits_set.remove("orange")

print()
for i in fruits_set:
    print(i)

print(len(fruits_set))