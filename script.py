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