                                
                              
                                
                                
class Polynomial:
    "Polynomial([]) -> a polynomial"
    
    def __init__ (self,poly):
        self.poly = poly
        
    def __add__(self,poly_new):
        "return self+poly_new"
        if len(self.poly) >= len(poly_new.poly):
            big = self.poly
            small = poly_new.poly
        else:
            big = poly_new.poly
            small = self.poly
        d = len(big)-len(small)
        for i in range(0,len(small)-1):
            big[i+d] = big[i+d]+small[i]
        return big
        
    def __sub__ (self,poly_new):
        if len(self.poly) >= len(poly_new.poly):
            big = self.poly
            small = poly_new.poly
        else:
            big = poly_new.poly
            small = self.poly
        d = len(big)-len(small)
        for i in range(0,len(small)-1):
            big[i+d] = big[i+d]-small[i]
        if len(self.poly) < len(poly_new.poly):
            for i in range(0,len(big)):
                big[i] = -big[i]
        return big
    
    def __mul__ (self,poly_new):
        a = Polynomial([])
        b = Polynomial([])
        if len(self.poly) >= len(poly_new.poly):
            big = self.poly
            small = poly_new.poly
        else:
            big = poly_new.poly
            small = self.poly
        for i in range(len(small)-1,0):
            for j in range(len(big)-1,0):
                a.poly.insert(0,small[i]*big[j])
            b.poly = Polynomial.__add__(a,b)
            del b.poly[0:len(big)]
            b.poly.insert(0,0)
        return a.poly

def main():
    a = Polynomial([1,2])
    b = Polynomial([4,-9,6.5])
    c = a+b
    print(c)
    

if __name__=="__main__":
    main()
    


