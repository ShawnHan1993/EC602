                       

                               
                                

class Polynomial():

    def __init__(self,coef = {}):
        exponent = len(coef) - 1
        result = {}
        for c in coef:
            if (c != 0):
                result[exponent] = c
            exponent -= 1
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
        new = ""        
        for i in reversed(sorted(self.exponents())):
            if(self[i]!=0):
                if len(new) > 0:
                    new +=  " + "
                new += str(self[i]) + "x^" + str(i)
            
        return new
            

    def __add__(self,a):
        
        psum = self
        for k in a.exponents():
            if k in psum.exponents():
                psum[k] += a[k]
            else:
                psum[k] = a[k]
                
        return psum
    
    def __sub__(self,a):
        
        psum = self
        for k in a.exponents():
            if k in psum.exponents():
                psum[k] +=  -1 * a[k]
            else:
                psum[k] = a[k]
                
        return psum

    def __radd__(self,a):
       
        psum = self
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
        new = 0
        for i in self.coef:
            new += self[i] * (x ** i)
            return new
        


   
    
        
def main():
    pass

if __name__ == '__main__':
    main()
