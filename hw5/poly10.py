                       
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
    "Polynomial to numbers"
    def __init__(self, list = None, dict = None):
        self.poly = {}
                     
        if list is None:
            list = []
        elif(type(list) == type({})):
            for e in list:
                if(list[e] != 0):
                    self.poly.update({e:list[e]})
        else:
                                 
                                              
                                        
                                     
                                     
                            
            
                            
            for j in range(0,len(list)):
                if (list[len(list)-j-1]!=0):
                    self.poly.update({j:list[len(list)-j-1]})
                

                                
                                    

    def __setitem__(self, num, value):
        if (num in self.poly):
            self.poly[num] = value
        else:
            if (value != 0):
                self.poly.update({num:value})

    def __getitem__(self, num):
        if (num in self.poly):
            return self.poly[num]
        else:
            return 0

    def eval(self, value):
        result = 0
        for i in self.poly:
            result += self.poly[i]*((value)**i)
        return result

    def __add__(self, num):
        "return self + num"
        if (not isinstance(num, Polynomial)):
            print ("num is not poly.")
            return 0
        result = {}
        for i in self.poly:
            if (i in num.poly):
                result.update({i:(self.poly[i] + num.poly[i])})
            else:
                result.update({i:self.poly[i]})
        for j in num.poly:
            if (j not in self.poly):
                result.update({j:num.poly[j]})
        return Polynomial(result)

    def __radd__(self, num):
        "return num + self"
        if (not isinstance(num, Polynomial)):
            print ("num is not poly.")
            return 0
        result = {}
        for i in self.poly:
            if (i in num.poly):
                result.update({i:(self.poly[i] + num.poly[i])})
            else:
                result.update({i:self.poly[i]})
        for j in num.poly:
            if (j not in self.poly):
                result.update({j:num.poly[j]})
        return Polynomial(result)

    def __sub__(self, num):
        "return num - self"
        if (not isinstance(num, Polynomial)):
            print ("num is not poly.")
            return 0
        result = {}
        for i in self.poly:
            if (i in num.poly):
                result.update({i:(self.poly[i] - num.poly[i])})
            else:
                result.update({i:self.poly[i]})
        for j in num.poly:
            if (j not in self.poly):
                result.update({j:(-num.poly[j])})
        return Polynomial(result)

    def __rsub__(self, num):
        "return num - self"
        if (not isinstance(num, Polynomial)):
            print ("num is not poly.")
            return 0
        result = {}
        for i in self.poly:
            if (i in num.poly):
                result.update({i:(num.poly[i] - self.poly[i])})
            else:
                result.update({i:(-self.poly[i])})
        for j in num.poly:
            if (j not in self.poly):
                result.update({j:(num.poly[j])})
        return Polynomial(result)

    def __mul__(self, num):
        "return self * num"
        if (not isinstance(num, Polynomial)):
            print ("num is not poly.")
            return 0
        result = {}
        for i in self.poly:
            for j in num.poly:
                if (i + j) in result:
                    result[i+j] += self.poly[i]*num.poly[j]
                else:
                    result[i+j] = self.poly[i]*num.poly[j]

        return Polynomial(result)

    def __rmul__(self, num):
        "return num * self"
        if (not isinstance(num, Polynomial)):
            print ("num is not poly.")
            return 0
        result = {}
        for i in self.poly:
            for j in num.poly:
                if (i + j) in result:
                    result[i+j] += self.poly[i] * self.poly[j]
                else:
                    result.update({i+j:self.poly[i]*self.poly[j]})

        return Polynomial(result)

    def __eq__(self, num):
        "return if num == self"
        if (not isinstance(num, Polynomial)):
            print ("num is not poly.")
            return False
        if (self is None):
            return False
        return self.poly == num.poly

    def __ne__(self, num):
        "return if num != self"
                                               
                                        
                          
        if (self is None):
            return True
        return self.poly != num.poly

    def deriv(self):
        "return the derivative of polynomials"
        if (self is None):
            return None
        result = {}
        for i in self.poly:
            result.update({(i-1):(self.poly[i]*i)})
        return Polynomial(result)

                        
                      
                
                             
                                                             
                               
                    
                  

    def __str__(self):
        "return str"
        s = ""
        for i in sorted(self.poly.keys()):
            item = "("+str(self.poly[i])+")*x^("+str(i)+")"
            s += item + " + "
        s = s[:-3]
        return s
        

def main():
    p1 = Polynomial([0,4,0,1])
    p2 = Polynomial([4,3,2,1])
    p3 = p1 - p2
    print(p3.poly)
    print(p3.eval(1.5))
          

if __name__=="__main__":
    main()
