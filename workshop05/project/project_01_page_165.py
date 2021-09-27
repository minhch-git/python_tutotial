"""
Author: chiu cam minh
Date: 13/08/2021
Program: project_01_page_165.py
Problem:
    A group of statisticians at a local college has asked you to create a set of functions that
    compute the median and mode of a set of numbers, as defined in Section 5.4. 
    Define these functions in a module named stats.py. 
    Also include a function named mean, which computes the average of a set of numbers.
    Each function should expect a list of numbers as an argument and return a single number.
    Each function should return 0 if the list is empty. 
    Include a main function that tests the three statistical functions with a given list.
Solution:
    
"""

def mode(list):
  sum = 0
  for number in list:
    sum += number
  if len(list) == 0:
    return 0
  return sum/len(list)


def median(list):
  theDictionary = {}
  for number in list:
    freq = theDictionary.get(number, None)
    if freq == None:
      theDictionary[number] = 1
    else:
      theDictionary[number] = freq + 1
  if len(theDictionary) == 0:
    return 0
  theMaximum = max(theDictionary.values())
  for key in theDictionary:
    if theDictionary[key] == theMaximum:
      return key
    
def mean(list):
  numbers = []
  for number in list:
    numbers.append(number)

  numbers.sort()
  if len(numbers) == 0:
    return 0
  midpoint = len(numbers) // 2
  if len(numbers) % 2 == 1:
    return numbers[midpoint]
  return (numbers[midpoint] + numbers[midpoint - 1]) /  2

def main():
  lyst = [3, 1, 5, 6, 2]
  print('List: ', lyst)
  print('Mode: ', mode(lyst))
  print('Median: ', median(lyst))
  print('Mean: ', mean(lyst))

main()
