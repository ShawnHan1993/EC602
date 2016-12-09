                                
class Polynomial():
    def __init__(self,coeffs=[0]):
        self.c=coeffs[:]
        powers=[0]
        self.p=powers[:]
        if(len(self.p)!=len(self.c)):
            self.p.pop()
            for i in range(len(self.c)):
                self.p.insert(0,i)
            
    def __str__(self):
        return str(self.c)
    __repr__=__str__
    
    def __len__(self):
        return len(self.c)
        
    def __add__(self,value):
        sum=Polynomial([])
        sum.c=self.c
        sum.p=self.p
        for i in range(len(value)):
            if(value.p[i]>sum.p[0]):
                sum.c.insert(0,value.c[i])
                sum.p.insert(0,value.p[i])
            elif value.p[i]>=sum.p[len(sum.c)-1]:
                for j in range(len(sum.c)-1):
                    if value.p[i]>sum.p[j+1]:
                        sum.c.insert(j+1,value.c[i])
                        sum.p.insert(j+1,value.p[i])
                        break
                    elif value.p[i]==sum.p[j+1]:
                        sum.c[j+1]=sum.c[j+1]+value.c[i]
                        break
            else:
                sum.c.append(value.c[i])
                sum.p.append(value.p[i]) 
        return sum
                
        
    def __sub__(self,value):
        sum=Polynomial([])
        sum.c=self.c
        sum.p=self.p
        for i in range(len(value)):
            if(value.p[i]>sum.p[0]):
                sum.c.insert(0,-value.c[i])
                sum.p.insert(0,value.p[i])
            elif value.p[i]>=sum.p[len(sum.c)-1]:
                for j in range(len(sum.c)-1):
                    if value.p[i]>sum.p[j+1]:
                        sum.c.insert(j+1,-value.c[i])
                        sum.p.insert(j+1,value.p[i])
                        break
                    elif value.p[i]==sum.p[j+1]:
                        sum.c[j+1]=sum.c[j+1]-value.c[i]
                        if sum.c[j+1]==0:
                            sum.c.pop(j+1)
                            sum.p.pop(j+1)
                        break
            else:
                sum.c.append(-value.c[i])
                sum.p.append(value.p[i]) 
        return sum
            
    def __getitem__(self,key):
        return self.c[len(self.c)-key-1]
    
    def __setitem__(self,key,value):
        if(key>self.p[0]):
            self.c.insert(0,value)
            self.p.insert(0,key)
        elif key>=self.p[len(self.c)-1]:
            for i in range(len(self.c)-1):
                if key>self.p[i+1]:
                    self.c.insert(i+1,value)
                    self.p.insert(i+1,key)
                    break
                elif key==self.p[i+1]:
                    self.c[i+1]=value
                    break
        else:
            self.c.append(value)
            self.p.append(key)
                    
    def __mul__(self,value):
        prod=Polynomial([0])
        for i in range(len(self.c)):
            for j in range(len(value)):
                temp1=self.c[i]*value.c[j]
                temp2=self.p[i]+value.p[j]
                for k in range(len(prod)):
                    if(temp2>prod.p[0]):
                        prod.c.insert(0,temp1)
                        prod.p.insert(0,temp2)
                        break
                    elif temp2>=prod.p[len(prod.c)-1]:
                        for q in range(len(prod.c)):
                            if temp2>prod.p[q]:
                                prod.c.insert(q,temp1)
                                prod.p.insert(q,temp2)
                                break
                            elif temp2==prod.p[q]:
                                prod.c[q]=prod.c[q]+temp1
                                break
                        break
                    else:
                        prod.c.append(temp1)
                        prod.p.append(temp2)
                        break
        for i in range(len(prod)):
            if prod.c[i]==0:
                prod.c.pop(i)
                prod.p.pop(i)
        return prod
            
    def __eq__(self,value):
        if(len(self.c)!=len(value)):
            return False
        else:
            k=0
            sum=0
            while k<len(value):
                if(self.c[k]!=value.c[k]):
                    return False
                    break
                elif (self.p[k]!=value.p[k]):
                    return False
                    break
                else:
                    sum=sum+1
                    k=k+1
            if(sum==len(value)):
                return True
                
                
    def eval(self,x):
        L=len(self.c)
        sum=0
        for i in range(L):
            sum+=self.c[i]*(x**self.p[i])
            print(sum)
        return sum
    
    def deriv(self):
        for i in range(len(self.c)):
            if self.p[i]==0:
                self.p.pop(i)
                self.c.pop(i)
                break
        for i in range(len(self.c)):
            self.c[i]=self.c[i]*self.p[i]
            self.p[i]=self.p[i]-1
        return self.c
        

def main():
    p1=Polynomial([3,2,5])
    p2=Polynomial([1,2,4])
               
                  
                
                 
                   
                   
    p3=p1-p2
    print(p3)
    print(p3.p)
    print(p1-p2)
             
              
                
            
                  
                      
                      
                
if __name__=="__main__":
    main()