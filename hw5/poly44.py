                                   

class Polynomial(dict):
    def __init__(self, poly=[]):
        self.poly = {}
        poly.reverse()
        keys = []
        values = []
        for i,v in enumerate(poly):
            if (v != 0):
                keys.append(i)
                values.append(v)
        self.poly = dict(zip(keys,values))
        
        
    def __add__(self, b):
        "Return a+b"
        result = Polynomial()
        for i in self.poly:
            if ((i in b.poly)):
                result.poly[i] = self.poly[i] + b.poly[i]
            elif(i not in b.poly):
                result.poly.update({i:self.poly[i]})
        for j in b.poly:
            if(j not in self.poly):
                result.poly.update({j:b.poly[j]})
        return result
        
    def __sub__(self, b):
        "Return a-b"
        result = Polynomial()
        for i in self.poly:
            if ((i in b.poly)):
                result.poly[i] = self.poly[i] - b.poly[i]
            elif(i not in b.poly):
                result.poly.update({i:self.poly[i]})
        for j in b.poly:
            if(j not in self.poly):
                result.poly.update({j:0-b.poly[j]})
        return result
        
    def __mul__(self, b):
        "Return a*b"
        result = Polynomial()
        for i in self.poly:
            for j in b.poly:
                if ((i+j) in result.poly):
                    result.poly[i+j] += self.poly[i] * b.poly[j]
                else:
                    result.poly[i+j] = self.poly[i] * b.poly[j]
        return result
        
    def __eq__(a,b):
        "Return a == b"
        for i in a.poly:
            if ((i in b.poly) & (a.poly[i] == b.poly[i]) & (len(a.poly) == len(b.poly))):
                return True
            else:
                return False
        
    def eval(self, n):
        "Evaluation of Polynomial"
        result = complex()
        for i in self.poly:
            result += (self.poly[i]*(n**i))
        return result
             
    def __setitem__(self, exp, number):
        "Return modified polynomial"
        result = Polynomial()
        result.poly = {exp:number}
        self.poly.update(result.poly)
        return self.poly
    
    def __getitem__(self, exp):
        "Return value of a at that exponent"
        n = complex()
        if exp in self.poly:
            n = self.poly[exp]
        else:
            n = 0
        return n
        
    def derive(self):
        "Derivative of Polynomial"
        result = Polynomial()
        for i in self.poly:
            result.poly.update({i-1:(i*self.poly[i])})
        return str(result)

    def __str__(self):
            return "".join(( "{:+}" if not exp else "{:+}(x^{})").format(val, exp)
                       for exp, val in sorted(self.poly.items()) if val)
                           
    def __repr__(self):
        return str(self.poly)