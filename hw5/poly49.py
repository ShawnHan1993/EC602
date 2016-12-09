                                             
               

          

class Polynomial():
    
    
                                                                            
                                                           
    def __init__(self, coefficient):
        self.coefficient = coefficient
        self.poly = {}
        
        for i in range(len(coefficient)):
            if coefficient[i] == 0:
                pass
            else:
                self.poly[len(coefficient)-i-1] = coefficient[i]
        

                                                           
    def __getitem__(self,key):
        try:
            return self.poly[key]
        except:
            IndexError
            print ("There is no exponent " +str(key) + " in this polynomial.")
            
            
                                                                
    def __setitem__(self,key, value):
        if value == 0:
               del self.poly[key]
        else:
              self.poly[key] = value
                
    def keys(self):
        return self.poly.keys()
    
    def items(self):
        return self.poly.items()
      
                                                                    
    def __str__(self):
        return str(self.poly)
    
    def eval(self,x):
        y = 0
        for i in self.poly.keys():
            y += self.poly[i]*x**i
        return y
    
    def deriv(self):
        dx = {}
        for i in list(self.poly.keys()):
            if i == 0:
                pass
            else:
                dx[i-1] = self.poly[i]*i
        return dx

        
        
    def __add__(self,B):
        c = Polynomial([])
        for i in list(self.keys()):
            if i in list(B.keys()):
                c[i] = B[i]+self[i]
            else:
                c[i] = self[i]
        for j in list(B.keys()):
            if j in list(self.keys()):
                c[j] = self[j] + B[j]
            else:
                c[j] = B[j]
        return c
            
    
            
    def __sub__(self,B):
        c = Polynomial([])
        for i in list(self.keys()):
            if i in list(B.keys()):
                c[i] = B[i]-self[i]
            else:
                c[i] = self[i]
        for j in list(B.keys()):
            if j in list(self.keys()):
                c[j] = self[j] - B[j]
            else:
                c[j] = B[j]
        return c
            
            
    def __mul__(self,B):
        c = Polynomial([])
        for i in list(self.keys()):
            for j in list(B.keys()):
                    if c[i+j] != None:
                        c[i+j] += self[i]*B[j]
                    else:
                        c[i+j] = self[i]*B[j]
        return c
    
    def __eq__(self,other):
        if self.eval(10) == other.eval(10):
            return True
        else:
            return False
    
    
def main():
    pass

if __name__=="__main__":
    main()
    
