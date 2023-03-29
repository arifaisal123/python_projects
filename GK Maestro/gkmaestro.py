""" 
Developed by: ARIF FAISAL (arifaisal123@gmail.com)
This game tests your general knowledge skills! 
You just need to answer the 10 questions correctly to become the winner!
"""

from question_bank import easy_question, hard_question
from answer_bank import answer
from random import randint, choice
from art import *


def main():
    ques_count = 1
    score = 0
    while ques_count <= 10:
        question_tuple = generate_question()
        question = question_tuple[1]

        print(f"Question No. {ques_count}: {question}")
        ques_count += 1
        user_answer = input("Answer: ")
        correct_answer = generate_answer(question_tuple[0])
        if user_answer.lower() == correct_answer.lower():
            score += 1
            print(f"Correct Answer. Your Score: {score}")
        else:
            print(f"Wrong Answer. Your Score: {score}")
    print(f"Your final score: {score}")
    if score == 10:
        tprint("Congratulations!")
        print("You have answered all 10 questions correctly!")
        

# Generates question for the player
def generate_question():
    easy_qlist = [2, 3, 4, 8, 9, 14, 15, 16]
    hard_qlist = [1, 5, 6, 7, 10, 11, 12, 13]
    difficulty = randint(1, 2)
    if difficulty == 1:
        random_choice = choice(easy_qlist)
        ques = easy_question(random_choice)
    elif difficulty == 2:
        random_choice = choice(hard_qlist)
        ques = hard_question(random_choice)
    return random_choice, ques


# Generates and matches answer of the player
def generate_answer(num):
    actual_answer = answer(num)
    return actual_answer


# Executes all the code when the file is run, not on imports
if __name__ == "__main__":
    main()
