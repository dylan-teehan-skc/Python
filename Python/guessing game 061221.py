import random

number = random.randint (1, 10)

print (number)

guess = int(input("enter a number between 1 and 10: "))

if guess == number:
    print ("your guess is correct")
    print ("well done")
    
print ("goodbye")