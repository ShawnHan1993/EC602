                             
                                   
                                     

class Polynomial():
    def __init__(self,value=[0]):
        self.p=value
        self.pp={}
        i=len(self.p)-1
        for y in self.p:
            self.pp[i]=y
            i-=1
    def __add__(self,value):     
        sum={}
        temp={}        
        for n in self.pp:
            if n in value.pp:
                sum[n]=self.pp[n]+value.pp[n]
                
            else:
                sum[n]=self.pp[n]
        for m in value.pp:
            if m in self.pp:
                sum[m]=self.pp[m]+value.pp[m]
               
            else:
                sum[m]=value.pp[m]
        for k in sum:
            temp[k]=sum[k]
        for l in temp:
            if sum[l]==0:
                sum.pop(l)           
        return sum   
    def __sub__(self,value):     
        sub={}
        temp={}
        for n in self.pp:
            if n in value.pp:
                sub[n]=self.pp[n]-value.pp[n]
                
            else:
                sub[n]=self.pp[n]
        for m in value.pp:
            if m in self.pp:
                sub[m]=self.pp[m]-value.pp[m]
               
            else:
                sub[m]=value.pp[m]
        for k in sub:
            temp[k]=sub[k]
        for l in temp:
            if sub[l]==0:
                sub.pop(l)           
        return sub
    def __mul__(self,value):
        prod={}
        temp={}
        for n in self.pp:
            for m in value.pp:
                if m+n in prod:
                    prod[m+n]=prod[m+n]+self.pp[n]*value.pp[m]
                else:
                    prod[m+n]=self.pp[n]*value.pp[m] 
        for k in prod:
            temp[k]=prod[k]
        for l in temp:
            if prod[l]==0:
                prod.pop(l)           
        return prod
    def __eq__(self,value): 
        if self.pp==value.pp:
            return True
        else:
            return False
    def __setitem__(self,key,value):
        self.pp[key]=value
    def __getitem__(self,key):
        return self.pp[key]  
    def eval(self,value):
        sum=0
        for i in self.pp:
            sum=sum+(self.pp[i]*(value**(i)))
        return sum  
    def deriv(self):
        deriv={}
        for n in self.pp:
             if n!=0:
                 deriv[n-1]=n*self.pp[n]
        return deriv