                       
\
\
\
\
   

           
                                
                              

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
                                                                                          

                                                                 

class Polynomial():

    def __init__(self,coef = {}):
        exp = len(coef) - 1
        result = {}
        for c in coef:
            if (c != 0):
                result[exp] = c
            exp -= 1
        self.coef = result
        

    def exponents(self):
        return self.coef.keys()
        
    def __getitem__(self,key):
        return self.coef[key]        
        
    def __setitem__(self,key, newcoef):
        self.coef[key] = newcoef
        
    def __delitem__(self,key):
        del self.coef[key]
        
    def __str__(self):
        res = ""        
        for i in reversed(sorted(self.exponents())):
            if(self[i]!=0):
                if len(res) > 0:
                    res = res + " + "
                res = res + str(self[i]) + "x^" + str(i)
            
        return res
            
    def copy(self):
        newselfpoly = Polynomial([])
        for i in self.coef:
            newselfpoly[i]=self[i]
        return newselfpoly

   
    def __add__(self,a):
        psum = self.copy()

        for k in a.exponents():
            if k in psum.exponents():
                psum[k] += a[k]
            else:
                psum[k] = a[k]
                
        return psum
    
    def __sub__(self,a):
        psum = self.copy()

        for k in a.exponents():
            if k in psum.exponents():
                psum[k] += (-1)*a[k]
            else:
                psum[k] = (-1)*a[k]
                
        return psum
        
                
        return psum

    def __radd__(self,a):

        psum = self.copy
        for k in a.exponents():
            if k in psum.exponents():
                psum[k] += a[k]
            else:
                psum[k] = a[k]
                
        return psum

    def __rsub__(self,a):
        psum = self
        for k in a.exponents():
            if k in psum.exponents():
                psum[k] += -1 * a[k]
            else:
                psum[k] = a[k]
                
        return psum


    def __mul__(self,a):
        result = Polynomial([])
        for exp1 in self.exponents():
            for exp2 in a.exponents():
                newexp = exp1 + exp2
                newcoef = self[exp1] *  a[exp2]
                try:
                    result[newexp] += newcoef
                except KeyError:
                    result[newexp] = newcoef
        return result

    def __eq__(self,a):
        if self.coef == 0 and a.coef == 0:
            return True
        if len(self.coef) != len(a.coef):
            return False
        
        for i in self.coef:
            if self[i] != a[i]:
                return False
        
        return True
        
        

    def deriv(self):
        newpoly = Polynomial([])
        for i in self.coef:
            try:
                newpoly[i-1] = self[i]*(i)
            except KeyError:
                    newpoly[i-1] = self[i]*(i)    
                
        return newpoly
            
     
    def eval(self,x):
        neweval = 0
        for i in self.coef:
            neweval += self[i] * (x ** (i) )
        return neweval
    
    
        
  
    
        
def main():
    p1 = Polynomial([1,2,0,4,5,6])
    
    print("p1=",p1)
    p2 = Polynomial([1,2,0,4,5])
    
    print("p2=",p2)
    p3 = p1-p2
    p6 = Polynomial()
    p7 = Polynomial()
    p8 = Polynomial([8,0])
    p6[5]=1
    p6[4]=0
    p7[5]=1
    
    print("p3=p2+p1=",p3)
    print("p1=",p1)
    print("p2=",p2)
                          
    print(p6 == p7)
    print(p8.deriv())
    print(p1.eval(2))

if __name__ == '__main__':
    main()
