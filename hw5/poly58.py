                       
                             

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
        poly = ""        
        for i in reversed(sorted(self.exponents())):
            if(self[i]!=0):
                if len(poly) > 0:
                    poly = poly + " + "
                poly = poly + str(self[i]) + "x^" + str(i)
            
        return poly
            

    def __add__(self,a):
        sum = self
        for j in a.exponents():
            if j in sum.exponents():
                sum[j] += a[j]
            else:
                sum[j] = a[j]
                
        return sum
    
    def __sub__(self,a):
        poly = self
        for j in a.exponents():
            if j in poly.exponents():
                poly[j] +=  -1 * a[j]
            else:
                poly[j] = a[j]
                
        return poly

    def __mul__(self,a):
        product = Polynomial([])
        for exp1 in self.exponents():
            for exp2 in a.exponents():
                newexp = exp1 + exp2
                newcoef = self[exp1] *  a[exp2]
                try:
                    product[newexp] += newcoef
                except KeyError:
                    product[newexp] = newcoef
        return product
        
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



    def __eq__(self,a):
        if len(self.coef) != len(a.coef):
            return False
        
        for i in self.coef:
            if self[i] != a[i]:
                return False
        
        return True

    def deriv(self):
            deriv = Polynomial([])
            for i in self.coef:
                try:
                    deriv[i-1] = self[i]*(i)
                except KeyError:
                    deriv[i-1] = self[i]*(i)                
            return deriv
            

def main():
    p1 = Polynomial([1,3,5,7])
    print(p1)
    p1[3] = 4
    p1[0] = 9
    print(p1)
    p2 = Polynomial([1,2,3,4])
    print(p2)
    p3 = p1 + p2
    p4 = p1 - p2
    p5 = p1 * p2
    p6 = Polynomial([1,4,3])
    p7 = Polynomial([1,2,3])
    print(p3)
    print(p4)
    print(p5)
    print(p6)
    print(p7)
    print(p6 == p7)
    print(p1.deriv())

if __name__ == '__main__':
    main()
