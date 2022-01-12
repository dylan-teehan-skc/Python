import random

colour = ["blue",'red','green','pink','orange','black','brown']
list = random.choice(colour)
print(list)

guess = (input("Enter a colour: "))
    
if guess == list:
    print("Correct")
    
    

print("Goodbye")

