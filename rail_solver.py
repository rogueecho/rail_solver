#!/usr/bin/env python
"""
This script brute-forces possible solutions for rail fence ciphers.
"""

import sys

def main():
    if len(sys.argv) != 2:
        print "Usage:\n    railSolver.py <ciphertext>"
        return 1

    #Set N = to 
    N = 2

    #Read in ciphertext
    cipher = sys.argv[1]
    with open(cipher,"r") as text:
        text=text.read().replace("\n","")
    
    #Loop until a large enough N-space has been covered
    while N <= (.5 * len(text)):
        #Set number of columns and rows
        cols = len(text) // N
        rows = N
        #Each rail is going to be a list of chars which will get printed at the end of each row
        rail = ""
        x = 0   #Counter for not blowing past end of text
        i = 0   #This is going to keep track of where we are in the rail
        
        #Loop over entire ciphertext and insert '-'s incrementally
        while x < len(text):
            if i % N == 0:
                rail += text[x]
                x += 1
                i += 1
            elif i % N != 0:
                rail += '-'
                i += 1

        #Insert newlines to split the text into individual rails
        n = 0   #Again, our counter for iterating over the whole string
        railList = list(rail)    #Gotta make this a list to work
        inserts = 0
        
        """
        FIX BELOW: For some reason it isn't inserting the \n at the correct locations
        """
        
        while n < len(rail):
            if n > cols - 1:
                if cols % n == 0:
                    railList.insert(n + inserts,"\n")
                    inserts += 1
            n += 1

        print ''.join(railList) + "\n\n\n\n"
        N += 1

if __name__ == "__main__":
    main()
