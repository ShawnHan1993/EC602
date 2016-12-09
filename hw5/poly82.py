                       

                             
                                   
                                     
                             

class Polynomial():
    def __init__(self,value=[0]):
        self.p=value
        self.pp=dict()
        i=len(self.p)-1
        for y in self.p:
            if y != 0:
                self.pp[i]=y
            i-=1

    def __add__(self,value):
        result={}      
        for n in self.pp:
            if n in value.pp:
                result[n]=self.pp[n]+value.pp[n]
            else:
                result[n]=self.pp[n]
        for m in value.pp:
            if m in self.pp:
                result[m]=self.pp[m]+value.pp[m]
            else:
                result[m]=value.pp[m]
        return result
    def __sub__(self,value):
        sub=Polynomial()
        for n in self.pp:
            if n in value.pp:
                sub[n]=self.pp[n]-value.pp[n]
            else:
                sub[n]=self.pp[n]
        for n in value.pp:
            if (n in self.pp)==False:
                sub[n]=0-value.pp[n]
        return sub;
        
    def __mul__(self,value):
        prod={}
        for n in self.pp:
            for m in value.pp:
                if m+n in prod:
                    prod[m+n]=prod[m+n]+self.pp[n]*value.pp[m]
                else:
                    prod[m+n]=self.pp[n]*value.pp[m] 
        return prod
    def __eq__(self,value): 
        if self.pp==value:
            return True
        else:
            return False
    def __setitem__(self,key,value):
            self.pp[key]=value

    def __getitem__(self,key):
        if key in self.pp:
            return self.pp[key]
        else:
            return 0

    def eval(self, value):
        sum = 0
        for i in self.pp:
            sum = sum + self[i] * value**i
        return sum

    def deriv(self):
        deriv=Polynomial()
        for n in self.pp:
             if n!=0:
                 deriv[n-1]=n*self.pp[n]
        return deriv


def main():
    pass

if __name__=="__main__":
    main()

