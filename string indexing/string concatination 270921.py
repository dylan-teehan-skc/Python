word1 = "4"
word2 = "3"

subject = word1 + word2
print (subject)

#the result will be 43 as python sees 4 and 3 as string not number

word1 = 4
word2 = 3

subject = word1 + word2
print (subject)

#if you take away the qoutation marks it automatically sees the number not string
#another technique is casting

word1 = float("4")
word2 = float("3")

subject = word1 + word2
print (subject)

#float will print the number with decimal places