# -*- coding: utf-8 -*-

class Polynomial():
    def __init__(self,coef = []):
        self.n = len(coef)
        self.d={}
        for i in range(self.n):
            self.d[i]=coef[i]
                   
    def __getitem__(self,key):
        if self.d.has_key(key):
            return self.d[key] 
        else:
            return 0
        
    def __setitem__(self,key,newcoef):
        self.d[key]=newcoef

    def __add__(self,v):
        result=Polynomial([])
        b=v.d.copy()
        for i in self.d:
            if i in b.d:
                result.d[i]=self.d[i]+b.d[i]
                del b.d[i]
            else:
                result.d[i]=self.d[i]
        for i in b:
            result.d[i]=b.d[i]
        return result
    
    def __sub__(self,a):
        temp=a*(-1)
        return self+temp

    def __radd__(self,a):
        return self+a

    def __rsub__(self,a):
        temp=self*(-1)
        return a+temp

    def __mul__(self,a):  
        if hasattr(a,'d'):
            result=Polynomial([])
            for i in self.d:
                for j in a.d:
                    if (i+j) in result.d:
                        result.d[i+j]=result.d[i+j]+self.d[i]*a.d[j]
                    else:
                        result.d[i+j]=self.d[i]*a.d[j]
        else:
            result=self.d.copy()
            for i in result.d:
                result.d[i]=result.d[i]*a
        return result

    def __eq__(self,a):
        if len(self.d) != len(a.d):
            return False        
        for i in self.d:
            if i in a.d:
                if self.d[i]==a.d[i]:
                    pass
                else:
                    return False
            else:
                return False
        return True

    def deriv(self):
        del self.d[0]
        result=Polynomial([])
        for i in self.d:
            result.d[i-1]=self.d[i]*i
        return result         
     
    def eval(self,x):
        new = 0
        for i in self.d:
            new += self.d[i] * (x ** i)
        return new 
        
def main():
    pass

if __name__ == '__main__':
    main()
