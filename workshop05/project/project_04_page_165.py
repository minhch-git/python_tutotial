"""
Author: chiu cam minh
Date: 13/08/2021
Program: project_04_page_165.py
Problem:
  Make the following modifications to the original sentence-generator program:
  a. The prepositional phrase is optional. (It can appear with a certain probability.)
  b. A conjunction and a second independent clause are optional: 
  The boy took a drink and the girl played baseball.
  c. An adjective is optional: The girl kicked the red ball with a sore foot.
  You should add new variables for the sets of adjectives and conjunctions.
Solution:
    
"""
import random

articles = ("A", "THE")
nouns = ("BOY", 'GIRL', 'BAT', 'BALL')
verbs = ('HIT', 'SAW', 'LIKED')
prepositions = ('WITH', 'BY')
adjectives = ('RED', 'LITTLE')
conjunctions = ('AND', 'BUT')

def sentence():
  first = independentClause()
  if random.randint(1, 5) == 1:
    return first + " " + random.choice(conjunctions) + " " + independentClause()
  
def independentClause():
  return nounPhrase() + " " + verbPhrase()

def nounPhrase():
  if random.randint(1, 2) == 1:
    adj = random.choice(adjectives) + " "
  else: 
    adj = " "
  return random.choice(articles) + " " + adj + random.choice(nouns)


def verbPhrase():
  if random.randint(1, 3) == 1:
    prepPhrase = " "+prepositionalPhrase()
  else:
    prepPhrase = " "

  return random.choice(verbs) + " " +nounPhrase() + " " + prepPhrase


def prepositionalPhrase():
  return random.choice(prepositions) + " "+nounPhrase()

def main():
  number = int(input('Enter the number of sentences: '))
  for count in range(number):
    print(sentence())

main()
