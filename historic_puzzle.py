import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from the_solver import Solver

class HistoricPuzzle:
    def getUserStats():
        num_of_plays = input("How many times have you played?")
        guesses = []
        prompts = ["1","2","3","4","5","6"]
        for prompt in prompts:
            guess_count = input(f"How many times have you solved in {prompt} attempt?")
            
            item_count = {
                "key": prompt,
                "guesses": int(guess_count)
            }

            guesses.append(item_count)

        return pd.DataFrame(guesses), num_of_plays
        
    def getHistoricAnswers():
        results_response = requests.get("https://www.rockpapershotgun.com/wordle-past-answers")
        results_html = results_response.content.decode("utf-8")
        results_html_parsed = BeautifulSoup(results_html, features="lxml")

        answers = results_html_parsed.body.find('ul', attrs={'class': 'inline'}).find_all('li')
        return [answer.text for answer in answers]

    def getCorrectIncorrectLetters(answer, guess):
        tmp_answer = answer
        incorrect_letters = []
        correct_letters = ["-","-","-","-","-"]

        for index in range(5):
            if (guess[index].upper() == tmp_answer[index]):
                correct_letters[index] = guess[index].upper()
                tmp_answer_list = list(tmp_answer)
                tmp_answer_list[index] = "_"
                tmp_answer = "".join(tmp_answer_list)
            elif (tmp_answer.find(guess[index].upper()) < 0):
                incorrect_letters.append(guess[index])
                correct_letters[index] = "-"

        for index in range(5):
            if (correct_letters[index] == "-"):
                if (tmp_answer.find(guess[index].upper()) >= 0):
                    correct_letters[index] = guess[index].lower()
    
        return incorrect_letters, "".join(correct_letters)
    
    def getSolverStats(historical_answers):
        guesses = [
            { "key": "1", "guesses": 0},
            { "key": "2", "guesses": 0},
            { "key": "3", "guesses": 0},
            { "key": "4", "guesses": 0},
            { "key": "5", "guesses": 0},
            { "key": "6", "guesses": 0}
        ]

        guesses_df = pd.DataFrame(guesses)

        for answer in historical_answers:
            solver = Solver()
            solver.incorrect_letters.clear()
            solver.correct_letters = ""

            print("------------")
            print(f"Answer: {answer}")
            keep_looking = True
            guess_number = 0

            while keep_looking:
                guess_number += 1

                guess = solver.find_next_guess()
                print(f' - Guess {guess_number}: {guess}')
                if (guess.upper() == answer):
                    guesses_df.loc[guesses_df['key'] == str(guess_number), 'guesses'] = guesses_df.loc[guesses_df['key'] == str(guess_number),'guesses'] + 1 
                    keep_looking = False
                else:
                    if guess_number == 6:
                        print(" - Didn't get this one.  :-(")
                        keep_looking = False
                    else:
                        (incorrect, correct) = HistoricPuzzle.getCorrectIncorrectLetters(answer, guess)
                        [solver.incorrect_letters.append(letter) for letter in incorrect]
                        solver.correct_letters = correct
                        solver.filter_dataset()

        return guesses_df

    def play():
        (user_stats_df, num_of_plays) = HistoricPuzzle.getUserStats()
        historical_answers = HistoricPuzzle.getHistoricAnswers()

        solver_stats_df = HistoricPuzzle.getSolverStats(historical_answers)

        user_success = round((user_stats_df['guesses'].sum() / int(num_of_plays)) * 100, 2)
        solver_success = round((solver_stats_df['guesses'].sum() / len(historical_answers)) * 100, 2)

        merged_results_df = pd.merge(user_stats_df, solver_stats_df, how="outer", on="key")
        
        merged_results_df.plot(kind="bar")
        plt.legend([f"Your success rate: {user_success}", f"Solver's success rate: {solver_success}"])
        plt.show()

