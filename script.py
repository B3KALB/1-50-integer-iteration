# Write a python program that iterates the integers from 1 to 50. 
# For multiples of three print "Cloud" instead of the number
# For multiples of seven print "Computing"
# For numbers which are multiples of both three and seven print "CloudComputing"

for oneToFifty in range(51):
    if oneToFifty % 3 == 0 and oneToFifty % 7 == 0:
        print("CloudComputing")
        continue
    elif oneToFifty % 3 == 0 :
        print("Cloud")
        continue
    elif oneToFifty % 7 == 0:
        print("Computing")
        continue
    print(oneToFifty)

# Made a second integer iteration.
# 1.The number is always printed.
# 2.For odd numbers print "oddBall"
# 3.For even numbers print "EvenSteven"
# 4.For multiples of five print "HighFive"
# 5.Except, for every other five print "EveryOtherFive"

for oneToOneHundred in range(101):
    if oneToOneHundred % 2 == 0 and oneToOneHundred % 5 == 0:
        print(oneToOneHundred,"EveryOtherFive")
        continue
    elif oneToOneHundred % 2 == 0 :
        print(oneToOneHundred,"EvenSteven")
        continue
    elif oneToOneHundred % 5 == 0:
        print(oneToOneHundred,"HighFive")
        continue
    print(oneToOneHundred,"oddBall")

