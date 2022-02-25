#!/usr/bin/env python3
import sys
# II. Given a Roman Numeral String, parse it and return the number.
#   If it does not match a legal roman numeral from above
#   (in the range 1 to 3,999), return 0.
#   2. Very Important: Put each list in reverse order
#      E.g., look for XC then LXXX then LXX then LX then L, etc.
#   3. Use the str.upper() and str.startswith() methods.

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

if __name__ == "__main__":
    # pretty much same driver code from roman, except this uses the concatenation on the user input to see if works and is in range
    n = len(sys.argv)
    for i in range(1, n):
        input = sys.argv[i]
        input = str.upper(input)
        num = int(namor(input))
        if (num <= 0) or (num > 3999):
            print(input, "is 0")
        else:
            print(input, "is", num)
            