import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #if row.student == "Angela":
        #print(row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# Create the dataframe from csv file
nato_df = pandas.read_csv("26-nato-alphabet/nato-project/nato_phonetic_alphabet.csv")
#print(nato_df.iterrows())

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
#print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What word do you want in NATO Alphabet ? ").upper()
# OPTION 1
input_letters = [letter for letter in user_input]
nato_words_list = []
for l in input_letters:
    nato_word = {letter : word for (letter, word) in nato_dict.items() if letter == l}
    nato_words_list.append(nato_word)
#print(nato_words_list) return [{'S': 'Sierra'}, {'O': 'Oscar'}, {'F': 'Foxtrot'}, {'A': 'Alfa'}]
# OPTION 2
output_list = [nato_dict[letter] for letter in user_input]
print(output_list)
#return ['Tango', 'Alfa', 'Bravo', 'Lima', 'Echo']

