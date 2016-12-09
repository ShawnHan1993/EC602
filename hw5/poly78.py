                                  
                  

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
        return self.cf[keys]
        
    def __delitem__(self,keys):
        "Deletes the value stored at index exp."
        del self.cf[keys]
        
       
    def __add__(self,value):
        "Return self+value."
        result = Polynomial()                              
        if (len(self.cf.keys())>len(value.keys())):
            for i in value.keys():
                result[i] = self.cf[i] + value[i]
        else:
            for i in self.cf.keys():
                result[i] = value[i] + self.cf[i]
        return result                
    
    def __sub__(self,value):
        "Return self-value."
        print(self.cf)
        print(value)
        result = Polynomial()                              
        if (len(self.cf.keys())>len(value.keys())):
            for i in value.keys():
                result[i] = self.cf[i] - value[i]
        else:
            for i in self.cf.keys():
                result[i] = self.cf[i] - value[i]
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
        if (len(self.cf.keys())>len(value.keys())):
            for i in value.keys():
                result[i] = self.cf[i]==value[i]
        else:
            for i in self.cf.keys():
                result[i] = value[i]==self.cf[i]
        return result  


    def eval(self,value):
         "Return self evaluated at value."
         result = Polynomial()                              
         output = 0;
         for i in self.cf.keys():
             result[i] = value * self.cf[i]
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
        


def main():
        p = Polynomial([2, -4.6, 9]); 
        print(p)
        p[100] = 1;
        print(p)
        del p[100]
        print(p)
        q = Polynomial([1, 3, -5]);
        print(q)
        print('Mult: ', p*q)
        print('q after mult: ', q)
        print('Add: ', p+q)
        print('Q after add: ', q)
        print('Sub: ', p-q)
        print('Eq: ', p==q)
        p[-1] = 2;
        print(p)
        newp = Polynomial()
        newp[-1] = 3
        print(newp*q)
        p = Polynomial([2, -4.6, 9])
        print("eval: ", p.eval(2))
        print("deriv: ", p.deriv())
        print("d2: ", newp.deriv())
        

if __name__ == '__main__':
    main()