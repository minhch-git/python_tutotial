"""
Author: chiu cam minh
Date: 05/08/2021
Program: project_11_page_132.py
Problem:
    Jack just completed the program for the Flesch text analysis from this chapter’s case study.
    His supervisor, Jill, has discovered an error in his code. 
    The error causes the program to count a syllable containing consecutive vowels as multiple syllables.
    Suggest a solution to this problem in Jack’s code and modify the program so that it handles these cases correctly.

Solution:
    
"""

# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + text.count(':') + text.count(';') + text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():

    for vowel in vowels:
        syllables += word.count(vowel)

    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1

    if word.endswith('le'):
        syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")
