"""
Author: chiu cam minh
Date: 13/08/2021
Program: project_10_page_165.py
Problem:
    Conversations often shift focus to earlier topics.
    Modify the therapist program to support this capability.
    Add each patient input to a history list.
    Then, occasionally choose an element at random from this list, change persons, 
    and prepend (add at the beginning) the qualifier “Earlier you said that” to this reply. 
    Make sure that this option is triggered only after several exchanges have occurred.
Solution:
    
"""

import random

history = []
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
  probability = random.randint(1, 5)

  if probability in (1, 2):
    answer = random.choice(hedges)

  elif probability == 3 and len(history) > 3:
    answer = 'Earlier you said that' + changePerson(random.choice(history))

  else: 
    answer = random.choice(qualifiers) + changePerson(sentence)
  history.append(sentence)
  return answer

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
  