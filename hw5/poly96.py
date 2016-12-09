                                 
                   
                       

class Polynomial():
    def __init__(self, coef=[]):
        self.coef=coef
        self.exp=[]
        for i in range(len(coef)) :
            self.exp.insert(-i,i)
        while (1):
            try:
                a=self.coef.index(0)
                del self.coef[a]
                del self.exp[a]
            except ValueError:
                break
    
    def __add__(a,b):
        c=Polynomial([])
        for i in a.exp:
            if i in b.exp:
                c.exp.append(i)
                c.coef.append(a.coef[a.exp.index(i)]+b.coef[b.exp.index(i)])
            else:
                c.exp.append(i)
                c.coef.append(a.coef[a.exp.index(i)])
        for i in b.exp:
            if i not in a.exp:
                c.exp.append(i)
                c.coef.append(b.coef[b.exp.index(i)])
        return(c)


    def __mul__(a,b): 
        c=Polynomial([])
        for i in a.exp:
            for j in b.exp:
                k=i+j
                if k in c.exp:
                    c.coef[c.exp.index(k)]=c.coef[c.exp.index(k)]+a.coef[a.exp.index(i)]*b.coef[b.exp.index(j)]
                else:
                    c.exp.append(k)
                    c.coef.append(a.coef[a.exp.index(i)]*b.coef[b.exp.index(j)])
        return (c)
        
    def __eq__(self, value):
        a=sorted(self.exp)
        b=sorted(value.exp)
        if (a!=b):
            return ('Flase')
        else:
            for i in self.exp:
                for i in value.exp:
                    if (self.coef[self.exp.index(i)]==value.coef[value.exp.index(i)]):
                        pass
                    else:
                        return (print('Flase',self.exp.index,value.exp(i)))
                        break
                return(print('Ture'))

    def eval(self,x):
        output=0
        for i in self.exp:
            output=output+self.coef[self.exp.index(i)]*(x**i)
        return(output)
        
    def deriv(self):
         c=Polynomial([])
         for i in self.exp:
             if i!=0:
                 c.coef.append(self.coef[self.exp.index(i)]*i)
                 c.exp.append(i-1)
         if (c.exp==[]):
             c.exp=[0]
             c.coef=[0]
         return (c)
        
                       
    def __setitem__(self,nexp,ncoef):
         if ncoef==0:
             pass
         else:
             if nexp in self.exp:
                a=self.exp.index(nexp)
                self.coef[a]=ncoef
             else:
                self.exp.append(nexp)
                self.coef.append(ncoef)
            
    def __getitem__(self,exp,coef):
        return (self.exp,coef)
            
    def __str__(self):
        return "coef:{} exp:{}".format(self.coef,self.exp)

    def __repr__(self):
        return str(self)
