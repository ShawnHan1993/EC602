                                  
                                   
                                  
class Polynomial():
    def __init__(self,List = []):
        self.dict = {}
        for key in range(len(List)):
            self.dict[len(List)-key-1] = List[key]                   
    def __str__(self):
        pass
        
    def __add__(self,poly):
        result = {}
        for key in self.dict:
            if key in poly.dict:
                result[key] = self.dict[key] + poly.dict[key]
            else:
                result[key] = self.dict[key]
        for key in poly.dict:
            if key in self.dict:
                pass
            else:
                result[key] = poly.dict[key]
        return result

    def __sub__(self,poly):
        result = {}
        for key in self.dict:
            if key in poly.dict:
                result[key] = self.dict[key] - poly.dict[key]
            else:
                result[key] = self.dict[key]
        for key in poly.dict:
            if key in self.dict:
                pass
            else:
                result[key] = -poly.dict[key]
        return result
        
    def __mul__(self,poly):
        result = {}
        for key in self.dict:
            for jey in poly.dict:
                if (key + jey) in result:
                    result[ key+ jey ] = result[ key + jey ] + self.dict[key] * poly.dict[jey]
                else:
                    result[ key+ jey ] = self.dict[key] * poly.dict[jey]
        return result
        
    def __eq__(self, poly):
        if isinstance(poly,Polynomial):
            if len(self.dict) != len(poly.dict):
                return False
            else:
                for key in self.dict:
                    if key not in poly.dict:
                        return False
                    elif self.dict[key] != poly.dict[key]:
                        return False
                    else:
                        continue
                    return True
        else:
            if len(self.dict) != len(poly):
                return False
            else:
                for key in self.dict:
                    if key not in poly:
                        return False
                    elif self.dict[key] != poly[key]:
                        return False
                    else:
                        continue
                    return True
            
    def __getitem__(self,val):
        return self.dict[val]
     
    def __setitem__(self,key,val):
        self.dict[key] = val
            
    def eval(self,val):
        result = 0
        for key in self.dict:
            result = result + (val ** key) * self.dict[key]
        return result
        
    def deriv(self):
        result = {}
        for key in self.dict:
            result[key-1] = self.dict[key] * key
        if -1 in result:
            del result[-1]
        return result
            
        
def main():
     p = Polynomial([1,2,3])
     q = Polynomial([3,2,1])
     print(p+q)
     print(p-q)
     print(p*q)
     print(p == q)
     print(p[1])
     p[-10]=10
     print(p.eval(10))
     print(p.deriv())
if __name__=="__main__":
    main()
