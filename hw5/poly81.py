                                     

class Polynomial():
    def _init_(self,List = []):
        self.dict = {}
        for key in range(len(List)):
            self.dict[len(List)-key-1] = List[key]
    def _str_(self):
        return str(self.dict)
        
    def _add_(self,poly):
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
        
    def _sub_(self,poly):
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
                result[key]= -poly.dict[key]
        a.dict = result
        return a
