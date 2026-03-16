# creating list of numbers and letters
numbers_list = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
letters_list = ("A", "B", "C", "D", "E", "F", "H", "I", "J")

# pair numbers to letters and store in new variable
paired_values = zip(numbers_list, letters_list)

# convert pariued values to a dict
numbers_to_letters = dict(paired_values)

# print the dictionary
print(numbers_to_letters)

# convert numbers to text
print(numbers_to_letters[2], numbers_to_letters[0], numbers_to_letters[5], numbers_to_letters[4])

