"""
Author: chiu cam minh
Date: 13/08/2021
Program: project_09_page_165.py
Problem:
    In Case Study 5.5, when the patient addresses the therapist personally,
    the therapist’s reply does not change persons appropriately.
    To see an example of this problem, test the program with “you are not a helpful therapist.”
    Fix this problem by repairing the dictionary of replacements.
Solution:
    
"""
import random

hedges = (
  'Please tell me more.',
  'Many of my patients tell me the same thing.',
  'Please continue.'
)

qualifiers = (
  'Why do you say that ',
  'You seem to think that ',
  'Can you explain why '
)

replacements = {
  'I': 'you', 'me': 'you', 'my': 'you',
  'we': 'you', 'us': 'you', 'mine': 'yours',
  'you': 'I', 'your': 'my', 'yours': 'mine'
}

def reply(sentence):
  probability = random.randint(1, 4)
  if probability == 1:
    return random.choice(hedges)
  return random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence):
  words = sentence.split()
  replyWords = []
  for w in words:
    replyWords.append(replacements.get(w, w))
  return ' '.join(replyWords)
  
def main():
  print('Good morning, I hope you well to day.')
  print('What can I do you?')

  while True:
    sentence = input('\n>> ')
    if sentence.upper() == 'QUIT':
      print('Have a nice day!')
      break
      
    print(reply(sentence))

if __name__ == '__main__':
  main()
  