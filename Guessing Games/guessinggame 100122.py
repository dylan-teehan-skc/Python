import random

number = random.randint(1,10)
print (number)

guess = (int(input("pick a number from 1 to 10: ")))

if guess == number:
    print ("correct")
    
else:
    print ("wrong")