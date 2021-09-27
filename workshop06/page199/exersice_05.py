"""
Author: chiu cam minh
Date: 04/09/2021
Program: exersice_05_page_199.py
Problem:
   Three versions of the summation function have been presented in this chapter. 
   One uses a loop, one uses recursion, and one uses the reduce function.
   Discuss the costs and benefits of each version, in terms of programmer time and
   computational resources required.
Solution:
   Recursion
      Recursion uses selection structure.
      Infinite recursion occurs if the recursion step does not reduce the problem in a manner that converges on some condition (base case) and Infinite recursion can crash the system.
      Recursion terminates when a base case is recognized.
      Recursion is usually slower than iteration due to the overhead of maintaining the stack.
      Recursion uses more memory than iteration.
      Recursion makes the code smaller.

   Loop
      Iteration uses repetition structure.
      An infinite loop occurs with iteration if the loop condition test never becomes false and Infinite looping uses CPU cycles repeatedly.
      An iteration terminates when the loop condition fails.
      An iteration does not use the stack so it's faster than recursion.
      Iteration consumes less memory.
      Iteration makes the code longer.
      
   Reduce Function
      It turns out that we can accomplish the above task using the reduce function instead of a for loop.
      The reduce function can take in three arguments, two of which are required.
      The two required arguments are: a function (that itself takes in two arguments), and an iterable (such as a list).
      The third argument, which is an initializer, is optional and thus we will discuss it later on.
"""
