"""
Author: chiu cam minh
Date: 13/08/2021
Program: project_03_page_165.py
Problem:
    Modify the sentence-generator program of Case Study 5.3 so that it inputs 
    its vocabulary from a set of text files at startup. 
    The filenames are nouns.txt, verbs.txt, articles.txt, and prepositions.txt. 
    (Hint: Define a single new function, getWords. 
    This function should expect a filename as an argument. 
    The function should open an input file with this name, 
    define a temporary list, read words from the file, and add them to the list.
    The function should then convert the list to a tuple and return this tuple.
    Call the function with an actual filename to initialize each of the four variables for the vocabulary.)
Solution:
    
"""
import random, os


def getWords(file_name):
    input_file = open(f"{os.getcwd()}/file_test/{file_name}", "r")
    words = []
    for line in input_file:
        words.extend(line.split())
    return tuple(words)


articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")


def sentence():
    return nounPhrase() + " " + verbPhrase()


def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)


def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionsPhrase()


def prepositionsPhrase():
    return random.choice(prepositions) + " " + nounPhrase()


def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


main()
