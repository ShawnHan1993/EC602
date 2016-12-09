                       
\
\
\
\
\
\
   
                                    

class Polynomial():
    "Polynomial(a,b,c) -> ax^2+bx+c"
    def __init__(self,coefficients=[], power = None):
        self.poly = {}
                                                       
        if power is None:
            p= [ i for i in reversed(range(len(coefficients)))]
                                           
        else:
            p = power
        for k in range(len(p)):
                                     
            self.poly[p[k]] = coefficients[k]
        if self.poly == {}:
            self.poly[0] = 0
    
    def __add__(self,other):
        sumcoeff = []
        sumpow = []
                                                              
        for i in self.poly.keys():
            if i in other.poly:
                sumcoeff.append(self.poly[i]+other.poly[i])
                sumpow.append(i)
            else:
                sumcoeff.append(self.poly[i])
                sumpow.append(i)
                                                           
        for j in other.poly.keys():
            if j not in self.poly:
                sumcoeff.append(other.poly[j])
                sumpow.append(j)
        return Polynomial(sumcoeff,sumpow)
    
    def __sub__(self,other):
        difcoeff = []
        difpow = []
                                                                   
        for i in self.poly.keys():
            if i in other.poly:
                difcoeff.append(self.poly[i]-other.poly[i])
                difpow.append(i)
            else:
                difcoeff.append(self.poly[i])
                difpow.append(i)
                                                                   
        for j in other.poly.keys():
            if j not in self.poly:
                difcoeff.append(0-other.poly[j])
                difpow.append(j)
        return Polynomial(difcoeff,difpow)
    
    def __mul__(self,other):
        prod = {}
        prodcoeff = []
        prodpow = []
                                                                     
                                                     
        for i in self.poly.keys():
            for j in other.poly.keys():
                s = i + j
                if s in prod:
                    prod[s] = prod[s] + self.poly[i]*other.poly[j]
                else:
                    prod[s] = self.poly[i]*other.poly[j]
                                                              
        prodcoeff = [k for k in prod.values()]
        prodpow = [l for l in prod.keys()]
        return Polynomial(prodcoeff,prodpow)
        
                   
    def __eq__(self,other):
        if self.poly == other.poly:
            return True
        else:
            return False                
        
    def eval(self,x):
        y = 0
        for i in self.poly.keys():
            y = y + self.poly[i]*x**i
        return y
        
    def deriv(self):
        dcoeff = []
        dpow = []
        for i in sorted(self.poly.keys(),reverse = True):
                                                            
            if i == 0:
                dcoeff.append(0)
                dpow.append(0)
                                                              
                                         
            else:
                dcoeff.append(self.poly[i]*i)
                dpow.append(i-1)
        return Polynomial(dcoeff,dpow)
        
    def __getitem__(self,index):
                                                              
        try:
            return self.poly[index]
        except:
            return 0
   
    def __setitem__(self,index,value):
                       
                                          
                                     
              
        self.poly[index] = value
    
    def __str__(self):
        output = ""
        first = 0
                                                      
        for i in sorted(self.poly.keys(), reverse = True):
            if isinstance(self.poly[i],complex):
                sign="-" if self.poly[i].real<0 else "+"
            else:                
                sign="-" if self.poly[i]<0 else "+"
            if first == 0:
                if i == 1:
                    output = output + "{}X".format(self.poly[i])
                elif i == 0:
                    output = output + "{}".format(self.poly[i])
                else:    
                    output = output + "{}X^{}".format(self.poly[i],i)
                first = 1
            elif i == 1:
                output = output + " {} {}X".format(sign,abs(self.poly[i]))
            elif i == 0:
                output = output + " {} {}".format(sign,abs(self.poly[i]))
            else:
                output = output + " {} {}X^{}".format(sign,abs(self.poly[i]),i)
        return output
                    
        
def main():
    test1 = Polynomial([1,2,3,4])
    test2 = Polynomial()
    test2[-2] = 5678
    print(test1)
    print(test2)
    test3 = test1 - test2
    test4 = Polynomial([1,2,3,4])
    test4[-2] = -5678
    if test3 == test4:
        print("equal")
    else:
        print("not equal")
    print(test3)

    
if __name__ == '__main__':
    main()