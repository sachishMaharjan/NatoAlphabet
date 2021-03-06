# TODO 1. Create a dictionary in this format:
import pandas
from ascii import logo

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print(logo)
print("Nato Alphabet Generator\n")
user_name = input("Enter your name: ").upper()
user_nato = [nato_dict[letter] for letter in user_name]
print(user_nato)
