import pandas as pd
import string

class Solver:

    incorrect_letters = []
    correct_letters = ""

    def letter_count(self, word, letter):
        return word.count(letter)
    
    def find_fuzzy(self, temp_df, letter, location):
        return temp_df.loc[(temp_df[f'{letter}_count'] > 0) & (temp_df[f'letter_{location}'] != letter)]

    def find_exact(self, temp_df, letter, location):
        return temp_df.loc[temp_df[f'letter_{location}'] == letter.lower()]
    
    def remove_missing(self, letter, correct_count):
        self.filtered_df = self.filtered_df.loc[self.filtered_df[f'{letter}_count'] == correct_count]
    
    def __init__(self):
        data_path_one = 'data/valid_solutions.csv'
        data_path_two = 'data/valid_guesses.csv'

        word_bank_one = pd.read_csv(data_path_one)
        word_bank_two = pd.read_csv(data_path_two)
        word_bank = pd.merge(word_bank_one, word_bank_two, how="outer")
        word_bank['letter_1'] = word_bank['word'].str[0:1]
        word_bank['letter_2'] = word_bank['word'].str[1:2]
        word_bank['letter_3'] = word_bank['word'].str[2:3]
        word_bank['letter_4'] = word_bank['word'].str[3:4]
        word_bank['letter_5'] = word_bank['word'].str[4:5]
        for index in range(26):
            letter = string.ascii_lowercase[index]
            word_bank[f'{letter}_count'] = self.letter_count(word_bank['word'].str, letter)
        word_bank

        self.filtered_df = word_bank
        
    def find_next_guess(self):
        letters = []
        temp_df = self.filtered_df
        for char_count in range(1,6):
            letter = temp_df[f'letter_{char_count}'].value_counts().index[0]
            temp_df = self.find_exact(temp_df, letter, char_count)
            letters.append(letter)
        return ''.join(letters)
    
    def filter_dataset(self):
        # filter out wrong letters
        for incorrect_letter in self.incorrect_letters:
            correct_list = [i for i, letter in enumerate(self.correct_letters) if letter.lower() == incorrect_letter.lower()]
            self.remove_missing(incorrect_letter, len(correct_list))
        
        # filter for correct letters
        for correct_letter in self.correct_letters:
            if correct_letter != "_":
                if correct_letter.islower():
                    self.filtered_df = self.find_fuzzy(self.filtered_df, correct_letter, self.correct_letters.index(correct_letter) + 1)
                elif correct_letter.isupper():
                    self.filtered_df = self.find_exact(self.filtered_df, correct_letter, self.correct_letters.index(correct_letter) + 1)

        

        