# List Comprehension
# new_numbers = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers) # return [2, 3, 4]

#String as list
name = "Angela"
new_list = [letter for letter in name]
print(new_list)  # return ['A', 'n', 'g', 'e', 'l', 'a']

# Range as List
new_range = [n * 2 for n in range(1, 5)]
print(new_range)  # return [2, 4, 6, 8]

# Conditional List Comprehension
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)  # return ['Alex', 'Beth', 'Dave']
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)  # return ['CAROLINE', 'ELEANOR', 'FREDDIE']

# CHALLENGE 1
# You are going to write a List Comprehension to create a new list called squared_numbers. 
# This new list should contain every number in the list numbers but each number should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

# CHALLENGE 2
# You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]
print(result)

# CHALLENGE 3
# Create a list called result which contains the numbers taht are common in both files.
with open("26-nato-alphabet/examples/file1.txt") as file_1:
    f1_list = file_1.readlines()

with open("26-nato-alphabet/examples/file2.txt") as file_2:
    f2_list = file_2.readlines()

result2 = [int(n) for n in f1_list if n in f2_list]
print(result2)
