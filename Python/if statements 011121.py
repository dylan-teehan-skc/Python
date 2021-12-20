#Guessing game
#program to guess colour of room your going to walk into

import random

possible = ["blue","green","red","orange"]
colour = random.choice(possible)
print (colour)

guess = (input("enter colour you think the room is: "))

if guess == colour:
  print ("welldone")
  print ("your guess was correct")


