import random

number =  random.randint (1,10)
print (number)

counter = 0

while counter < 3:
    
    
    guess = int(input("Enter a number between 1 and 10: "))
    if guess == number:
        print("Correct")
        break #exit the loop immediately
    elif guess < number:
        print("Too low")
    else:
        print("Too high")

    counter = counter + 1

print("Goodbye")
    
    