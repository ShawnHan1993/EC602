                       
\
\
\
\
   
                                     
                                

class Polynomial():
    "Print"
    def __init__ (self,value=[]):
       self.po = dict()
       for i in range(len(value)):
           self.po[i] = value[len(value)-i-1]
           if self.po[i] == 0:
               del self.po[i]
           
           
               
    def __setitem__ (self,a,value):
        self.po[a] = value
        if value == 0:
            del self.po[a]
            
    def __getitem__ (self,a):
        if a in self.po:
            return self.po[a]
        else:
            return 0
            
    def __delitem__ (self,a):
        if a in self.po:
            del self.po[a]
            
    def __str__ (self):
        return str(self.po)
    
    def __add__ (self,value):
        temp = Polynomial([])
        for i in self.po:
            temp[i] = self[i]
        for i in value.po:
            if i in self.po:
                temp[i] = self[i] + value[i]
            else:
                temp[i] = value[i]
        return temp
    
    def __sub__ (self,value):
        temp = Polynomial([])
        for i in self.po:
            temp[i] = self[i]
        for i in value.po:
            if i in self.po:
                temp[i] = self[i] - value[i]
            else:
                temp[i] = 0-value[i]
        return temp
              
        
    def __mul__ (self,value):
        temp = Polynomial()
        for i in self.po:
            for j in value.po:
                temp[i+j] = temp [i+j] + self[i] * value[j]
        return temp
        
    def __eq__ (self,value):
        if value.po == [] and self.po == []:
            return True
        for i in self.po:
            if value[i] != self[i]:
                return False
        return True
        
                    
                                   
                                 
                                  
                                                      
                       

    def eval (self,value):
        result = 0
        for i in self.po:
            result = result + (value ** i) * self[i]
        return result
            
    def deriv (self):
        temp = Polynomial([])
        for i in self.po:
            temp[i-1] = i * self[i]
            if temp[i-1] == 0:
                del temp[i-1]
        return temp
    
def main():
    pass



if __name__=="__main__":
    main()