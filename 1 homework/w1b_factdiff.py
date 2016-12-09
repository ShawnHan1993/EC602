# -*- coding: utf-8 -*-
# AUTHOR ShenHan shawnhan@bu.edu
# AUTHOR ChanglongJiang cljiang@bu.edu
def myFactorial(x):
    if x==0:
        return 0
    else:       
        result=1;
        for i in range(1,x+1):
            result=result*i
        return result
        
def calcuByte(x,result=0):
    if int(x/2)==0:
        return result+1
    else:
        result+=1
        return calcuByte(int(x/2),result)
    
X=input("please input X: ")
Y=input("please input Y: ")
X=int(X)
Y=int(Y)
Z=myFactorial(X)-myFactorial(Y)
print(Z)
tmp=len(str(Z))
print(tmp)
cc=calcuByte(Z)
#cc=len(str(bin(Z)))
print(cc)
cc=int(cc/8)+1
print(cc)
    