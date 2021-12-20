#a program to demonstrate the single if staement
import random

name = (input("what is your name: "))
number = random.randint(1,10)
print (number)

guess=int(input("enter a number between 1 and 10: "))

#evaluate the condition
if number == guess:
    print("your guess was correct")
    print ("well done!")
    
elif guess < number:
    print ("hard luck!")
    print ("your guess was" ,number - guess , "lower than the number")
    
elif guess > number:
    print ("hard luck!")
    print ("your guess was",guess - number ," more than the number")

print ("goodbye" , name )