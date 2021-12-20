import random
name = input ("enter your name: ")
age= (int(input("enter your age: ")))
counter = 0
number1 = random.randint(1,10)
if age <= 18:
    while counter < 3:
        print (number1)
        guess = (int(input("pick a number between 1-10: ")))
        if guess == number1:
            print ("well done")
            break
        else:
            print("incorrect")
            counter = counter + 1

    
