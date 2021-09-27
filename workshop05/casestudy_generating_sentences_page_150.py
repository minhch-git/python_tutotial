"""
Author: chiu cam minh
Date: 10/08/2021
Program: casestudy_generating_sentences_page_150.py
Problem:
  Write a program that generates sentences.
Solution:
 
"""
import random
# Vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

# Builds and returns a sentence.
def sentence():
  return nounPhrase() + " " + verbPhrase()
# Builds and returns a noun phrase.

def nounPhrase():
  return random.choice(articles) + " " + random.choice(nouns)
# Builds and returns a verb phrase.

def verbPhrase():
  return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

# Builds and returns a prepositional phrase.
def prepositionalPhrase():
  return random.choice(prepositions) + " " + nounPhrase()

# Allows the user to input the number of sentences to generate.
def main():
  number = int(input("Enter the number of sentences: "))
  for count in range(number):
    print(sentence())

if __name__ == "__main__":
  main()
