# Nato Alphabet Program

##################################
###### Created by 4bd3ss4md ######
##################################

import csv


def main():
    # Open the file that contains nato phonetic alphabets
    with open('nato_phonetic_alphabet.csv', 'r') as csv_file:
        # Create an empty dictionary
        nato_alphabet = {}
        # Read text file using csv module
        csv_reader = csv.DictReader(csv_file)
        # Loop through each dictionary
        for dictio in csv_reader:
            # Adjust the dictionary
            nato_alphabet[dictio['letter']] = dictio['code']

    # Control the program
    is_on = True
    while is_on:

        # Get user input
        user_input = input('Enter a word: ')

        # To quit the program
        if user_input == 'Exit' or user_input == 'exit':
            is_on = False
        else:
            # loop through each character of the word given
            nato_words = []
            for char in user_input:
                char = char.upper()
                word = nato_alphabet[char]
                nato_words.append(word)

            # Print the nato alphabet to the user
            count = 0
            char_num = len(user_input) - 1
            for word in nato_words:
                if count == char_num:
                    print(f'{word}.')
                else:
                    print(f'{word}, ', end='')
                    count += 1


main()
