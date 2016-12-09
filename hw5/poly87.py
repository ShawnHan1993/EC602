                                  
                  

\
\
   



class Polynomial():
    "Polynomial() -> a real polynomial"

    def __init__(self,cf={}):
        keys = len(cf) - 1                                  
        result = {}                              
        for i in cf:
            result[keys] = i
            keys -= 1
        self.cf = result

    def __setitem__(self,keys,val):
        "Sets value at index exp."
        self.cf[keys] = val
    
    def __getitem__(self,keys):
        "Returns value stored at index exp."
        if (keys in self.cf.keys()):
            return self.cf[keys]
        else:
            return 0
        
    def __delitem__(self,keys):
        "Deletes the value stored at index exp."
        if (keys in self.cf.keys()):
            del self.cf[keys]
        else:
            pass
       
    def __add__(self,value):
        "Return self+value."
        result = Polynomial()                              
        for i in self.cf.keys():
            if (i in value.keys()):
                result[i] = self.cf[i] + value[i]
            else:
                result[i] = self.cf[i]
        for i in value.keys():
            if (i in self.cf.keys()):
                pass
            else:
                result[i] = value[i]
        return result                
    
    def __sub__(self,value):
        "Return self-value."
        result = Polynomial()                              
        for i in self.cf.keys():
            if (i in value.keys()):
                result[i] = self.cf[i] - value[i]
            else:
                result[i] = self.cf[i]
        for i in value.keys():
            if (i in self.keys()):
                pass
            else:
                result[i] = - value[i]
        return result
    
    def keys(self):
        return self.cf.keys()
    
    def __mul__(self,value):
        "Return self*value."
        result = Polynomial()                              
        for i in self.cf.keys():
            for j in value.keys():
                if (i+j) in result.keys():
                    result[i+j] = result[i+j] + self.cf[i] * value[j]
                else:
                    result[i+j] = self.cf[i] * value[j]
        return result
        
    
    def __eq__(self,value):
        "Return self==value."
        result = Polynomial()                              
        if (len(self.cf.keys())!=len(value.keys())):
            result = "False"
        else:
            for i in value.keys():
                result[i] = self.cf[i]==value[i]
            for i in self.cf.keys():
                result[i] = value[i]==self.cf[i]
        if (False in result):
            result = "False"
        else:
            result = "True"
        return result  

    def __ne__(self,value):
        "Return self!=value."
        result = Polynomial()                              
        if (len(self.cf.keys())!=len(value.keys())):
            result = "True"
        else:
            for i in value.keys():
                result[i] = self.cf[i] != value[i]
            for i in self.cf.keys():
                result[i] = value[i] != self.cf[i]
        if (False in result):
            result = "False"
        else:
            result = "True"
        return result

    def eval(self,value):
         "Return self evaluated at value."
         result = Polynomial()                              
         output = 0;
         for i in self.cf.keys():
             result[i] = value ** i * self.cf[i]
             output = result[i] + output    
         return output    

    def deriv(self):
        "Return d/dx of self."
        result = Polynomial()                              
        for i in self.cf.keys():
            if i != 0:
                result[i - 1] = i * self.cf[i]
        return result
        
    def __str__(self):
        "Returns a string of the polynomial"
        return "{}".format(self.cf)