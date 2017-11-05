import math
# number of test cases
n = int(input())
# convert decimal to binary
def tobinary(dec):
    return "{0:b}".format(dec)
# take in test cases

array = [None] * n
for i in range(int(n)):
    # Take in array
    # fills array
    for case in range(0,n):
        array[case] = input()
    # takes each individual test case
    for j in array:
        x = int(j[0:(str(j).index(","))])
        y = int(j[(str(j).index(",")+1):])
    # define a sum var
        total = 0
    # convert nums to binary
        xbin = tobinary(x)
        ybin = tobinary(y)
    # goes through all digits of the binary number, up until the shortest length
        for k in range(-1,(min(len(xbin),len(ybin))+1) * -1,-1):
    # if both at each index equal each other and 1, add one to sum
            if ((xbin[int(k)]==ybin[int(k)]) & (xbin[int(k)]==("1"))):
                total += 1
    # upon completion of scan, print total
        print (total)    
        
    
    
