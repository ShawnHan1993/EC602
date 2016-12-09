                                 
                                       

class Polynomial():
    def __init__(self,ori=[]):
        self.n=len(ori)                                                               
        self.Coe=ori
        self.Ord=[]
        for i in range(self.n):
            self.Ord.append(self.n-i-1)
        try:
            while True:
                loc=self.Coe.index(0)
                del self.Coe[loc]
                del self.Ord[loc]
                self.n=self.n-1
        except:
            pass
            
    def __add__(self,value):
        if hasattr(value,'Coe'):
            result=Polynomial([])
            for i in range(self.n):
                result[self.Ord[i]]=result[self.Ord[i]]+self.Coe[i]
            for i in range(value.n):
                result[value.Ord[i]]=result[value.Ord[i]]+value.Coe[i]
                                                                      
            return result
        else:
            pass          
                                          
    def __radd__(self,value):
        return self.__add__(value)
                
    def __sub__(self,value):
        if hasattr(value,'Coe'):
            return self+(-1)*value
        else:
            pass
            
    def __rsub__(self,value):
        if hasattr(value,'Coe'):
            return (-1)*self+value
        else:
            pass
            
    def __mul__(self,value):
        result=Polynomial([])                                                                                   
        if hasattr(value,'Coe'):
            for i in range(self.n):
                for j in range(value.n):
                    loc=self.Ord[i]+value.Ord[j]
                    result[loc]=self.Coe[i]*value.Coe[j]+result[loc]
        else:
            for i in range(self.n):
                result.Coe.append(self.Coe[i]*value)
                result.Ord.append(self.Ord[i])
                result.n=result.n+1
        return result
        
    def __rmul__(self,value):
        return self.__mul__(value)
        
    def __eq__(self,value):
        if hasattr(value,'Coe'):
            if self.n!=value.n:
                return False
            else:
                for i in range(self.n):
                    if (self.Coe[i]!=value.Coe[i]) or (self.Ord[i]!=value.Ord[i]):
                        return False
                return True
        else:
             return False
            
    def __getitem__(self,ID):
        try:
            loc=self.Ord.index(ID)
            return self.Coe[loc]
        except:
            return 0  
            
    def __setitem__(self,key,value):
        flag=0
        for i in range(self.n):
            if self.Ord[i]==key:
                loc=i
                flag=1
                break
            if self.Ord[i]<key:
                loc=i
                flag=2
                break
        if flag==1:
            if value==0:
                del self.Coe[loc]
                del self.Ord[loc]
                self.n=self.n-1
            else:
                self.Coe[loc]=value
        elif flag==2:
            if value!=0:
                self.Coe.insert(loc,value)
                self.Ord.insert(loc,key)
                self.n=self.n+1
        else:
            if value!=0:
                self.Coe.append(value)
                self.Ord.append(key)
                self.n=self.n+1
    
    def eval(self,value):
        result=0
        for i in range(self.n):
            result=result+self.Coe[i]*(value**(self.Ord[i]))
        return result
    
    def deriv(self):
        result=self.copy()
        try:
            loc=result.Ord.index(0)
            del result.Ord[loc]
            del result.Coe[loc]
            result.n=result.n-1                                                  
        except:
            pass
        for i in range(result.n):
            result.Coe[i]=result.Coe[i]*result.Ord[i]
            result.Ord[i]=result.Ord[i]-1
        return result
        
    def copy(self):
        result=Polynomial([])
        result.n=self.n
        result.Coe=self.Coe.copy()
        result.Ord=self.Ord.copy()
        return result
                
    def __str__(self):
        return " ".join(str(items) for items in self.Coe)
        

def main():
    pass

if __name__=="__main__":
    main()