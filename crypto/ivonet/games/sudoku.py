#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOTE!!!: run this one with a python 2 interpreter!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

try:
    import ui
except:
    pass

import sys
def r(a):
    i=a.find('0')
    if i<0:
        y = 0
        print 25*"-"
        for i in range(9):
            y +=1
            print "|",
            for j in range(3):
                print ' '.join(list(a[i*9:(i+1)*9][j*3:((j+1)*3)])),
                print "|",
            print
            if y%3 == 0:
                print 25*"-"


            #print ' '.join(list(a[i*9:((i+1)*9)]))
    [m in[(i-j)%9*(i/9^j/9)*(i/27^j/27|i%9/3^j%9/3)or a[j] for j in range(81)] or r(a[:i]+m+a[i+1:]) for m in`14**7*9`]

#r("035000009000087043070304501300900804100008000007010305020006090006020008041700000")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        r(sys.argv[1].strip())
    else:
        print "syntaxis: sudoku.py [000010000301400860900500200700160000020805010000097004003004006048006907000080000]"
    #raw_input("Press enter to quit...")

