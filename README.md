# wordle_solver

This project uses the following features to solve Wordle challenges:
* Loading CSV files in to Pandas DataFrames for the Wordle word bank.
* Web requests and HTML parsing to retrieve historical Wordle solutions.
* DataFrame filtering for narrowing down potential solutions.
* Matplotlib to generate a bar chart comparing user and algorithm success rates.

#### This repo has the following items:

| File | Description |
| - | - |
| `data/valid_guesses.csv` | List of valid 5-letter words, but aren't valid Wordle solutions |
| `data/valid_solutions.csv` | List of valid Wordle solutions |
| `historic_puzzle.py` | HistoricPuzzle class implementation.  All code and logic used to obtain user statistics, retrieve historical solutions via web request, perform guess analysis on historical solutions, and display a bar graph comparing user and algorithm success rates. |
| `specific_puzzle.py` | SpecificPuzzle class implementation.  All code and logic for the user to input correct and incorrect letters and have the algorithm suggest the next word to try. |
| `the_solver.py` | Solver class implementation.  Used by both the historical and specific puzzle logic.  Loads both word lists and merges them.  Has logic to filter the word list based on incorrect and correct letter input. |
| `wordle_solver.py` | Entry point for the application.  Has a menu interface to prompt the user if they want specific help, historical analysis, or to quit the program |


