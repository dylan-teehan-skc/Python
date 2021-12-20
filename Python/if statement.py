#a program to demonstrate the single if staement
import random

number = random.randint(1,10)

guess=int(input("enter a number between 1 and 10: "))

if number == guess:
    print("your guess was correct")
    print ("well done")
    
print ("goodbye")