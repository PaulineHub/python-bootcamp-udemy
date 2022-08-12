##############################################
# List Comprehension
# new_numbers = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
#print(new_numbers) # return [2, 3, 4]

#String as list
name = "Angela"
new_list = [letter for letter in name]
#print(new_list)  # return ['A', 'n', 'g', 'e', 'l', 'a']

# Range as List
new_range = [n * 2 for n in range(1, 5)]
#print(new_range)  # return [2, 4, 6, 8]

##############################################
# Conditional List Comprehension
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
#print(short_names)  # return ['Alex', 'Beth', 'Dave']
long_names = [name.upper() for name in names if len(name) > 5]
#print(long_names)  # return ['CAROLINE', 'ELEANOR', 'FREDDIE']

##############################################
# CHALLENGE 1
# You are going to write a List Comprehension to create a new list called squared_numbers. 
# This new list should contain every number in the list numbers but each number should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
#print(squared_numbers)

# CHALLENGE 2
# You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]
#print(result)

# CHALLENGE 3
# Create a list called result which contains the numbers taht are common in both files.
with open("26-nato-alphabet/examples/file1.txt") as file_1:
    f1_list = file_1.readlines()

with open("26-nato-alphabet/examples/file2.txt") as file_2:
    f2_list = file_2.readlines()

result2 = [int(n) for n in f1_list if n in f2_list]
#print(result2)

##############################################
# Dictionary Comprehension
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
import random
students_scores = {student:random.randint(1, 100) for student in names}
#print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
#print(passed_students)
# print(students_scores.items()) # return dict_items([('Alex', 50), ('Beth', 75), ('Caroline', 49), ('Dave', 69), ('Eleanor', 32), ('Freddie', 36)])

##############################################
# CHALLENGE 4
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#print(len(sentence_list[0]))
result = {word:len(word) for word in sentence.split()}
#print(result)
# return {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

# CHALLENGE 5
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
#print(weather_f)

##############################################
# Looping in Data Frame

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)
    # return
    # ['Angela', 'James', 'Lily']
    #[56, 76, 98]

import pandas

## Loop through data frame
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#for (key, value) in student_data_frame.items():
    #print(value)

## Loop through rows of a data frame with .iterrows()
for (index, row) in student_data_frame.iterrows():
    print(row.student)
