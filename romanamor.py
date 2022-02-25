#!/usr/bin/env python3
import sys
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
    
def namor(input):
    #using tuples of tuples for each unique roman num val, 3rd val being instances of number allowed into string to be used
    tup = (('M', 1000, 3), ('CM', 900, 1),('D', 500, 1), ('CD', 400, 1),('C', 100, 3), ('XC', 90, 1),('L', 50, 1), ('XL', 40, 1),('X', 10, 3), ('IX', 9, 1),('V', 5, 1), ('IV', 4, 1), ('I', 1, 3))
    #get length/declare vars for nested loops
    length = len(input)
    result = 0
    i = 0
    for n, x, max in tup:
        c = 0
        #check and match
        while input[i:i+len(n)] == n:
            c += 1
            if c > max:
                return 0;
            #add on
            result += x
            i += len(n)
    return result

k=0
val = 0
for i in {k, 4000}:
         str = roman(i)
         if(i == namor(str)):
             pass
         else:
             val += 1
             print("Converted",i,"to Error back to 0, which is wrong.")
             print("Checked values from 0 to 4000. Errors =",val)
