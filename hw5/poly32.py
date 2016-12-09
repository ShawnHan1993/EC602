                              
class Polynomial():
    def __init__(self,c=[],dictionary={}):
        self.d={}
        if dictionary !={}:
            self.d=dictionary
            return 
        c.reverse()
        for i in range(len(c)):
            self.d.update({i:c[i]})
                         
        
    def __add__(self,value):
        newdic={}
        if(self.d=={}):
            newdic=value.d.copy()
            return Polynomial([],newdic)
        if(value.d=={}):
            newdic=self.d.copy()
            return Polynomial([],newdic)
        newdic=self.d.copy()
        for i in value.d.keys():
            if i in newdic.keys():
                newdic.update({i:newdic.get(i)+value.d.get(i)})
            else:
                newdic.update({i:value.d.get(i)})
        
        return Polynomial([],newdic)
        
    def __radd__(self,value):
        newdic={}
        if(self.d=={}):
            newdic=value.d.copy()
            return Polynomial([],newdic)
        if(value.d=={}):
            newdic=self.d.copy()
            return Polynomial([],newdic)
        newdic=self.d.copy()
        for i in value.d.keys():
            if i in newdic.keys():
                newdic.update({i:newdic.get(i)+value.d.get(i)})
            else:
                newdic.update({i:value.d.get(i)})
        
        return Polynomial([],newdic)
        
    def __sub__(self,value):
        newdic={}
        if(self.d=={}):
            newdic=value.d.copy()
            for i in newdic.keys():
                newdic.update({i:-1*newdic.get(i)})
            return Polynomial([],newdic)
        if(value.d=={}):
            newdic=self.d.copy()
            return Polynomial([],newdic)
        newdic=self.d.copy()
        for i in value.d.keys():
            if i in newdic.keys():
                newdic.update({i:newdic.get(i)-value.d.get(i)})
            else:
                newdic.update({i:-1*value.d.get(i)})
        
        return Polynomial([],newdic)
        
    def __mul__(self,value):
        newdic={}
        if self.d=={} or value.d=={}:
            return Polynomial()
        for i in self.d.keys():
            for j in value.d.keys():
                if i+j in newdic.keys():
                    newdic.update({i+j:self.d.get(i)*value.d.get(j)+newdic.get(i+j)})
                else:
                    newdic.update({i+j:self.d.get(i)*value.d.get(j)})
        
        
        return Polynomial([],newdic)
    def __rmul__(self,value):
        newdic={}
        if self.d=={} or value.d=={}:
            return Polynomial()
        for i in self.d.keys():
            for j in value.d.keys():
                if i+j in newdic.keys():
                    newdic.update({i+j:self.d.get(i)*value.d.get(j)+newdic.get(i+j)})
                else:
                    newdic.update({i+j:self.d.get(i)*value.d.get(j)})
        
        
        return Polynomial([],newdic)
    def __eq__(self,value):
        for i in self.d.keys():
            if i in value.d.keys():
                if self.d.get(i)==value.d.get(i):
                    pass
                else:
                    return False
            else:
                if self.d.get(i)==0:
                    pass
                else:
                    return False
        for i in value.d.keys():
            if i in self.d.keys():
                if self.d.get(i)==value.d.get(i):
                    pass
                else:
                    return False
            else:
                if value.d.get(i)==0:
                    pass
                else:
                    return False
        
        return True
    def eval(self,x):
        result=0
        for i in self.d.keys():
            result+=(x**i)*self.d.get(i)
        return result
    def deriv(self):
        newdic={}
        for i in self.d.keys():
            newdic.update({i-1:i*self.d.get(i)})
        
        return Polynomial([],newdic)
    def __str__(self):
        s=''
        for i in self.d.keys():
            s+=str(i)+':'+str(self.d.get(i))+' '
        return s
    def _repr_(self):
        return str(self)
    def __setitem__(self,k,v):
        self.d.update({k:v})
    def __getitem__(self,k):
        if k in self.d.keys():
            return self.d.get(k)
        else:
            return 0


def main():
                   
    x=Polynomial([3,0,0])
    x[3]=0
                   
    y=Polynomial([])
    y[2]=3
    y[45]=-0.0
    print(x)
                                    
    print(y)
    print(x==y)
    y[2]=30
    print(x==y)
    
                        
          
                   

if __name__=="__main__":
    main()
