"""
Program created by Arif Faisal, arifaisal123@gmail.com
"""
# Imports
import time
from questions import generate_questions
from answers import generate_answers
from art import *
from random import randint


def main():
    # Prints welcome message
    welcome_message()

    # Selects difficulty level
    while True:
        difficulty_level = int(input("Choose Difficulty Level (1-5): "))
        if difficulty_level >= 1 and difficulty_level <= 5:
            break
        else:
            print("Please select a valid difficulty level!")

    # Score and question variables
    TOTAL_QUES = 10
    TOTAL_TIME_IN_SEC = 10 * (6 - difficulty_level)
    current_score = 0
    question_num = 0

    # Prints game rules
    while True:
        print(f"Game Rules: You will get around {TOTAL_TIME_IN_SEC} seconds to complete all {TOTAL_QUES} questions!")
        user_input = input("Are you ready? (Type 'Yes' or 'No') ").lower()
        if user_input == "yes":
            break
        elif user_input == "no":
            print("Better luck next time!")
            exit()
        else:
            print("Please type 'Yes' or 'No' correctly!")
    
    
    # Game and timer starts
    start_time = time.time()
    end_time = start_time + TOTAL_TIME_IN_SEC
    
    # Iterates over each question until all the questions have been answered or the timer runs out
    while question_num < TOTAL_QUES and time.time() < end_time:
        print("---------------------------------------")
        question_num += 1
        print(f"Question No.: {question_num}")
        random_num = randint(1, 25)
        question = generate_questions(random_num)
        print(question)
        user_answer = input("Answer: ")
        answer = generate_answers(random_num)
        if user_answer == answer:
            current_score += 1
            print(f"Correct Answer! Your Score: {current_score}")
        else:
            print(f"Wrong Answer! Correct Answer is {answer}. Your score: {current_score}")
    
    if question_num != TOTAL_QUES:
        tprint("Time   is   up!!!!!")
    if current_score == 10:
        tprint("Congratulations! Full Score!")
    print(f"Final Score: {current_score}")


# Prints the welcome message for the user
def welcome_message():
    print("")
    print("-------- Welcome to Math Whizz! The game of the genius --------")
    tprint("Math Whizz!")
    print("                        by: arifaisal")
    print("----------------------------------------------------------------")


if __name__=="__main__":
    main()
