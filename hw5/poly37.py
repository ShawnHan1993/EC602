                                

class Polynomial():
    def __init__(self,poly = []):
        self.dict = {}
        for i in range(len(poly)):
            self.dict[len(poly)-i-1] = poly[i]    


    def __getitem__(self,val):
        if val in self.dict:
            return self.dict[val]
        else:
            return 0


    def __setitem__(self,i,val):
        self.dict[i] = val

    def __str__(self):
        return str(self.dict)

  
    def __add__(self,poly):
        result = {}
        a = Polynomial()
        for i in self.dict:
            if i in poly.dict:
                result[i] = self.dict[i] + poly.dict[i]
            else:
                result[i] = self.dict[i]
        for i in poly.dict:
            if i in self.dict:
                pass
            else:
                result[i] = poly.dict[i]
        a.dict = result
        return a


    def __sub__(self,poly):
        result = {}
        a = Polynomial()
        for i in self.dict:
            if i in poly.dict:
                result[i] = self.dict[i] - poly.dict[i]
            else:
                result[i] = self.dict[i]
        for i in poly.dict:
            if i in self.dict:
                pass
            else:
                result[i] = -poly.dict[i]
        a.dict = result
        return a
        


    def __mul__(self,poly):
        result = {}
        a = Polynomial()
        for i in self.dict:
            for j in poly.dict:
                if (i + j) in result:
                    result[ i+ j ] = result[ i + j ] + self.dict[i] * poly.dict[j]
                else:
                    result[ i+ j ] = self.dict[i] * poly.dict[j]
        a.dict = result
        return a



        
    def __eq__(self, poly):
        if len(self.dict) != len(poly.dict):
            return False
        else:
            for i in self.dict:
                if i not in poly.dict:
                    return False
                elif self.dict[i] != poly.dict[i]:
                    return False
                else:
                    continue
            return True
    
            
    def eval(self,val):
        result = 0
        for i in self.dict:
            result = result + (val ** i) * self.dict[i]
        return result
        

    def deriv(self):
        result = {}
        a = Polynomial()
        for i in self.dict:
            result[i-1] = self.dict[i] * i
        if -1 in result:
            del result[-1]
        a.dict = result
        return a
        

def main():
     p = Polynomial([1,2,3])
     q = Polynomial([3,-4,7,9])
     d = p + q
     print(q==p)
     print(d==Polynomial([4,4,4]))
     print(p)
     t = Polynomial([])
     t[-2] = 6
     print(t)

if __name__=="__main__":
    main()
