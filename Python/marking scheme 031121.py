name = input("whats your name: ")
subject = input("what subject is this mark for: ")
mark = int(input("what is your mark: "))
print ("your name is ",name , "the subject is" ,subject ,)

if mark > (int(100)):
    print ("invalid")   
    
elif mark >= (int(90)):
    print ("H1")
    print ("exellent")
    
elif mark >= (int(80)):
    print ("H2")
    print ("Well done")
    
elif mark >= (int(70)):
    print ("H3")
    print ("good work")
    
elif mark >= (int(60)):
    print ("H4")
    print ("good")
    
elif mark >= (int(50)):
    print ("H5")
    print ("better work needed")
        
elif mark >= (int(40)):
    print ("H6")
    print ("not good")
    
else:
    print ("you failed!")
    print ("hard luck")
    

    
