import random
import sys
import os

#This is the code for PartB,assignment1 of EC602.
#aothor Changlong Jiang

def f(n):
    if n > 1:
        return n*f(n-1)
    else:
        return 1
R = len(str(bin(f(X) -f(Y))))%8
A = len(str(bin(f(X) -f(Y))))
C = A - R
X = int(input('X = '))
Y = int(input('Y = '))

print('Z = ', f(X)-f(Y))
print(len(str(f(X) -f(Y))))
print(int(C/8+1))


