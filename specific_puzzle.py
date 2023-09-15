from the_solver import Solver

class SpecificPuzzle:
    def play():
        solver = Solver()
        loop = True
        while loop:
            recommended = solver.find_next_guess()
            print(f'Our recommended word is {recommended}')

            incorrect_letters = input('Enter the letters that are incorrect (leave blank if none):')
            for incorrect_letter in incorrect_letters:
                solver.incorrect_letters.append(incorrect_letter)

            print('Enter the correct letters in the following format:')
            print('Lowercase = correct letter, but wrong location')
            print('Uppercase = correct letter, correct location')
            print('Hyphen = incorrect letter')
            print("Ex:  s---E indicates there is an 'S' in the word, but not in the first position and that the word ends with 'E'")

            correct_letters = input('Enter the correct letters in the above format (leave blank if none):')

            solver.correct_letters = correct_letters

            if (incorrect_letters == '') & (correct_letters.find('-') == -1):
                print('Looks like we got it.  Glad we could help!')
                loop = False
            else:
                solver.filter_dataset()
