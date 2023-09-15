from specific_puzzle import SpecificPuzzle
from historic_puzzle import HistoricPuzzle

loop = True
while loop:
    print('Welcome to Wordle Solver!')
    print('Do you want to:')
    print('1) Receive help with a specific puzzle')
    print('2) Compare your statistics against abilities')
    print('3) Quit')

    user_choice = input('Enter your selection:')

    if user_choice == "3":
        loop = False
    elif user_choice == "1":
        SpecificPuzzle.play()
    elif user_choice == "2":
        HistoricPuzzle.play()
    else:
        print('Invalid entry')

