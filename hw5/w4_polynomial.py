# AUTHOR Shen Han shawnhan@bu.edu
# AUTHOR Changlong Jiang cljiang@bu.edu

class Polynomial():
    def __init__(self,ori=[]):
        self.n=len(ori)#n is the length of list Coe, different from the length of Poly
        self.Coe=ori[:]
        self.Ord=[]
        for i in range(self.n):
            self.Ord.append(self.n-i-1)
            
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
            #can be achieved by recurssion
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
        result=Polynomial([])# what if i do result=self? that would be bad, cause the name is actually a pointer
        if hasattr(value,'Coe'):
            for i in range(self.n):
                for j in range(value.n):
                    loc=self.Ord[i]+value.Ord[j]
                    tar=self.Coe[i]*value.Coe[j]
                    if result.n==0:
                        result.Coe.append(tar)
                        result.Ord.append(loc)
                        result.n=result.n+1
                        #print(result.Coe)
                        #print(result.Ord)
                    else:
                        for k in range(result.n):
                            if loc>result.Ord[0]:
                                result.Ord.insert(0,loc)
                                result.Coe.insert(0,tar)
                                result.n=result.n+1
                                #print(result.Coe)
                                #print(result.Ord)
                                #print(loc)
                                break
                            elif loc>=result.Ord[result.n-1]:
                                for b in range(result.n):
                                    if loc>result.Ord[b]:
                                        result.Coe.insert(b,tar)
                                        result.Ord.insert(b,loc)
                                        result.n=result.n+1
                                        #print(result.Coe)
                                        #print(result.Ord)
                                        #print(loc)
                                        break
                                    elif loc==result.Ord[b]:
                                        result.Coe[b]=result.Coe[b]+tar
                                        #print(result.Coe)
                                        #print(result.Ord)
                                        break
                                break
                            else:
                                result.Ord.append(loc)
                                result.Coe.append(tar)
                                result.n=result.n+1 
                                #print(result.Coe)
                                #print(result.Ord)
                                break
                    #result[loc]=self.Coe[i]*value.Coe[j]+result[loc]
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
            self.Coe[loc]=value
        elif flag==2:
            self.Coe.insert(loc,value)
            self.Ord.insert(loc,key)
            self.n=self.n+1
        else:
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
            result.Ord.pop(loc)
            result.Coe.pop(loc)
            result.n=result.n-1#take care of the n here, as it copy from the self
        except:
            pass
        for i in range(result.n):
            result.Coe[i]=result.Coe[i]*result.Ord[i]
            result.Ord[i]=result.Ord[i]-1
        return result
        
    def copy(self):
        result=Polynomial([])
        result.n=self.n
        result.Coe=self.Coe[:]
        result.Ord=self.Ord[:]
        return result
                
     

def main():
    a=Polynomial([1,2,3])
    b=Polynomial([1,2,3])
    #b[-100]=6
    #b[-11]=-7
    c=b.deriv();
    v=a*b  
    print(v.Coe)

if __name__=="__main__":
    main()        