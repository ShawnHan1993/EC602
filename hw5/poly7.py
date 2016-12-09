                                

class Polynomial():
    def __init__(self,List = []):
        self.dict = {}
        for key in range(len(List)):
            self.dict[len(List)-key-1] = List[key]    



    def __str__(self):
        return str(self.dict)



        
    def __add__(self,poly):
        result = {}
        a = Polynomial()
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
        a.dict = result
        return a




    def __sub__(self,poly):
        result = {}
        a = Polynomial()
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
        a.dict = result
        return a
        


    def __mul__(self,poly):
        result = {}
        a = Polynomial()
        for key in self.dict:
            for jey in poly.dict:
                if (key + jey) in result:
                    result[ key+ jey ] = result[ key + jey ] + self.dict[key] * poly.dict[jey]
                else:
                    result[ key+ jey ] = self.dict[key] * poly.dict[jey]
        a.dict = result
        return a



        
    def __eq__(self, poly):
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
            



    def __getitem__(self,val):
        if val in self.dict:
            return self.dict[val]
        else:
            return 0
     



    def __setitem__(self,key,val):
        self.dict[key] = val



            
    def eval(self,val):
        result = 0
        for key in self.dict:
            result = result + (val ** key) * self.dict[key]
        return result
        



    def deriv(self):
        result = {}
        a = Polynomial()
        for key in self.dict:
            result[key-1] = self.dict[key] * key
        if -1 in result:
            del result[-1]
        a.dict = result
        return a
        



def main():
     p = Polynomial([1,2,3])
     q = Polynomial([3,2,1])
     z = p + q
     print(q==p)
     print(z==Polynomial([4,4,4]))

if __name__=="__main__":
    main()