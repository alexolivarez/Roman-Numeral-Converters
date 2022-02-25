#!/usr/bin/env python3
import sys
#I. Given a number, return a Roman Numeral string. (20 points)
#   1.    Any number <= 0 or > 3,999, or invalid number, return "Error".
#   2.    Use only these standard values

    
def roman(input):
    # create 4 lists and put "" for zero values
    thou = ["", "M", "MM", "MMM"]
    hund = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    # look at thous and then hunds ... etc. / using // for int div and % for mod
    #get int value for array to pick val
    if input > 3999:
        return "";
    thouval = thou[input // 1000]
    thousand = thouval
    hundval = hund[(input % 1000) // 100]
    hundred = hundval
    tensval = tens[(input % 100) // 10]
    ten = tensval
    onesval = ones[input % 10]
    one = onesval


    # add string results from pulling vars from lists and return
    result = (thousand + hundred + ten + one)
    return result;



if __name__ == "__main__":
    # get amt of cmd line args because "Each one should accept one or more values using sys.argv(1:) "
    n = len(sys.argv)
    # run loop depending on how many cmd line args after basic run command
    for i in range(1, n):
        # get ints to convert to roman
        num = int(sys.argv[i])
        # print error for out of range
        if (num <= 0) or (num > 3999):
            print(num,"is error")
        #convert to roman and print
        else:
            ans = roman(num)
            print(num, "is", ans)
