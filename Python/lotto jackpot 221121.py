import itertools


#Irish lotto has 47 numbers 1 - 47
# total combinations = 10,737,573
# Cost of entry €4


numbers = [1,2,3,4,5,6,7,8,9,10]
for L in range(4,len(numbers)):
    for subset in itertools.combinations(numbers, L):
        print(subset)
