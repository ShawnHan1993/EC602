# -*- coding: utf-8 -*-

# AUTHOR Shen Han shawnhan@bu.edu
# AUTHOR Changlong Jiang cljiang@bu.edu
# AUTHOR Xinyu Li lxinyu@bu.edu

# w2c_addinghalf.py

from math import inf

def number_from_half(s : str):
    """return the number represented by s, a binary16 stored as a 4-character hex number"""
    origin=int(s,16)
    binary=16*[0]
    for i in range(16):
        if (origin-2*(origin//2))==0:
            binary[15-i]=0
        else:
            binary[15-i]=1
        origin=origin//2
    sign=binary[0]
    expo=''.join(map(str,binary[1:6]))
    expo=int(expo,2)
    if expo==31:#if the expo is '11111'
        result=inf
    else:
        if expo==0:
            frac=0
            expo=-14
        else:
            frac=1
            expo=expo-15
        for i in range(10):
            frac=frac+binary[6+i]*(2**(-i-1))
        result=frac*(2**(expo))
    result=result*((-1)**sign)
    return result

def main():
    """add all binary16 numbers from standard input until a non-number is entered, then print the total.
    Numbers are represented in 4-character hex string format, one per line"""
    list1=[]
    while True:
        try:
            x=input()
            if x=="exit":
                break
            list1.append(x)
        except:
            break
    Sum=0
    for i in range(len(list1)) :
        #print(number_from_half(list1[i]))
        Sum=Sum+number_from_half(list1[i])
    print(Sum)
    return Sum
    # hint1: use int(input(),16)
    # hint2: use try: except: to halt


if __name__ == '__main__':
    main()
    