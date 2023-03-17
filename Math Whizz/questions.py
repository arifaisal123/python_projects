# Question dictionary
question_bank = {
    1: "What is next in the following number series: 254, 287, 322, 359 . . . ?",
    2: "Name the only even prime number?",
    3: "What number equals 805+540+281?",
    4: "What is the sum of 111 + 222 + 333?",
    5: "What is 50 times 5 equal to?",
    6: "What is the value of pi (upto two decimal places)?",
    7: "How many hours in 90 minutes?",
    8: "What is -10 - (-6) equals to?",
    9: "What is the cube root of 1331?",
    10: "What percentage should be added to 40 to make it 50?",
    11: "What is the Next Prime Number after 7 ?",
    12: "Solve 23 + 3 ÷ 3 = ?",
    13: "What is 6% Equals to?",
    14: "50 times of 8 is equal to: ",
    15: "Find the missing terms in multiple of 3: 3, 6, 9, __, 15",
    16: "Solve 24 ÷ 8 + 2 = ?",
    17: "What is the next prime number after 5?",
    18: "128 raised to the power 0 is equal to:",
    19: "72 divided by 8 is equal to:",
    20: "9 x 7 is equal to:",
    21: "The square of 8 is equal to:",
    22: "What is the sum of 130+125+191?",
    23: "The square root of 81 is: ",
    24: "What is 1000 X 990?",
    25: "What is 5X5X5?",
}


# Returns a question randomly from the question dictionary
def generate_questions(num):
    return question_bank[num]
