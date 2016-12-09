# AUTHOR Yuxuan Mao yxmao@bu.edu
class Polynomial():
    def __init__(self,coeffs=[]):
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
        temp=Polynomial([])
        for k in range(len(self.c)):
            temp.c.append(self.c[k])
            temp.p.append(self.p[k])
        sum=Polynomial([])
        for i in range(len(value)):
            if len(temp.c) == 0:
                sum.c=value.c
                sum.p=value.p
                break
            else:
                sum.c=temp.c
                sum.p=temp.p
            if(value.p[i]>sum.p[0]):
                sum.c.insert(0,value.c[i])
                sum.p.insert(0,value.p[i])
            elif value.p[i]>=sum.p[len(sum.c)-1]:
                for j in range(len(sum.c)):
                    if value.p[i]>sum.p[j]:
                        sum.c.insert(j,value.c[i])
                        sum.p.insert(j,value.p[i])
                        break
                    elif value.p[i]==sum.p[j]:
                        sum.c[j]=sum.c[j]+value.c[i]
                        break
            else:
                sum.c.append(value.c[i])
                sum.p.append(value.p[i]) 
        return sum
    
                
        
    def __sub__(self,value):
        temp=Polynomial([])
        for k in range(len(self.c)):
            temp.c.append(self.c[k])
            temp.p.append(self.p[k])
        sum=Polynomial([])
        for i in range(len(value)):
            if len(temp.c) == 0:              
                sum.c=value.c
                sum.p=value.p
                for j in range(len(value)):
                    sum.c[j]=-sum.c[j]
                break
            else:
                sum.c=temp.c
                sum.p=temp.p
            if(value.p[i]>sum.p[0]):
                sum.c.insert(0,-value.c[i])
                sum.p.insert(0,value.p[i])
            elif value.p[i]>=sum.p[len(sum.c)-1]:
                for j in range(len(sum.c)):
                    if value.p[i]>sum.p[j]:
                        sum.c.insert(j,-value.c[i])
                        sum.p.insert(j,value.p[i])
                        break
                    elif value.p[i]==sum.p[j]:
                        sum.c[j]=sum.c[j]-value.c[i]
                        if sum.c[j]==0:
                            sum.c.pop(j)
                            sum.p.pop(j)
                        break
            else:
                sum.c.append(-value.c[i])
                sum.p.append(value.p[i]) 
        return sum
            
    def __getitem__(self,key):
        for i in range(len(self.p)):
            if self.p[i] == key:
                return self.c[i]
        return 0
    
    def __setitem__(self,key,value):
        if(len(self.p)== 0):
            self.c.insert(0,value)
            self.p.insert(0,key)
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
        count=0
        for i in range(len(prod)):
            if prod.c[i]==0:
                count=count+1
        for i in range(len(prod)-count):
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
        return sum
    
    def deriv(self):
        deriv=Polynomial([])
        for k in range(len(self.c)):
            deriv.c.append(self.c[k])
            deriv.p.append(self.p[k])
        for j in range(len(deriv)):
            if self.p[j]==0:
                deriv.p.pop(j)
                deriv.c.pop(j)
                break
        for i in range(len(deriv)):
           deriv.c[i]=deriv.c[i]*deriv.p[i]
           deriv.p[i]=deriv.p[i]-1
        print(deriv)
        return deriv
        

def main():
    p1=Polynomial([4,0,5])
    p2=Polynomial([])
    #p2[2]=3
    p2[1]=3
    p2[-1]=-2
    #p1[-2]=-2
    #print(p1)    
    #print(p1.p)
    #print(p2[2])
    #print(p2.p)
    #print(len(p1))
    #p3=p1-p2
    #print(p3)
    #print(p3.p)
    #print(p1-p2)
    p4=p1*p2
    print(p4)
    print(p4.p)
    #p1[-1]=4
    #print(p1)
    #print(p1==p2)
    #print(p2.eval(2))
    #print(p1)
    #print(p1.deriv())
    #print(p1)
if __name__=="__main__":
    main()