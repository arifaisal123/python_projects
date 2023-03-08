"""
Developed by: arifaisal123@gmail.com
This program is an English dictionary, that can generate meanings, synonyms, and antonyms as per user input.
Note: working internet connection is required for the program to function.
"""
from PyMultiDictionary import MultiDictionary, DICT_WORDNET


def main():
    while True:
        # Stores the type of feature to be used, and the word from user
        feature, word = user_input()

        # Generates answer based on the word provided
        answer = get_answer(feature, word)

        # Prints out the answer
        generate_output(answer)

        # Prompts the user if they want to continue
        post_output = input("Do you want to continue?(Yes/ No) ").lower()
        if post_output == "no" or post_output == "n":
            break


def user_input():
    """
    Takes user input for feature type, and word.
    Returns feature, and word name
    """
    options = ["word meaning", "synonym", "antonym"]

    print("""
        Type the feature you want to use? 
        1 - Word Meaning
        2 - Synonym
        3 - Antonym
    """)
    
    while True:
        feature = input("Feature: ").lower()
        if feature in options:
            break
        else:
            print("Please select the correct feature!")
            
    word_name = input("Word Name: ").lower()
    
    return feature, word_name


def get_meaning(word):
    """
    Generates the meaning of the word using MultiDictionary library.
    """
    dictionary = MultiDictionary()
    meaning = dictionary.meaning("en", word, dictionary=DICT_WORDNET)
    return meaning


def get_synonym(word):
    """
    Generates the synonym of the word using MultiDictionary library.
    """
    dictionary = MultiDictionary()
    synonym = dictionary.synonym("en", word)
    return synonym


def get_antonym(word):
    """
    Generates the antonym of the word using MultiDictionary library.
    """
    dictionary = MultiDictionary()
    antonym = dictionary.antonym("en", word)
    return antonym


def get_answer(feature, word):
    """
    Returns the answer of the word as a dictionary(in case of word meaning) or list(synonym, antonym)
    """
    if feature == "word meaning":
        return get_meaning(word)
    elif feature == "synonym":
        return get_synonym(word)
    elif feature == "antonym":
        return get_antonym(word)


def generate_output(answer):
    """
    Prints out the answer in the console.
    """
    if type(answer) == dict:
        print("""
----------------------------------------------
         Word Type  |   Word Meanings
----------------------------------------------
        """)
        for key, values in answer.items():
            print(key)
            for value in values:
                print(end="        ")
                print(value)
            print("----------------------------------------------------------------")
    else:
        print("----------")
        for word in answer:            
            print(word)
            print("----------")


if __name__=="__main__":
    main()
