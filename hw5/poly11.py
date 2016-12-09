                 
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
   



               



                 

class Polynomial():
    def __init__(self,seq=[]):
        self.poly={}
        self.seq=seq
        i=0;
        for i in range(len(seq)):
            if(seq[len(seq)-i-1]!=0):
                self.poly[i]=seq[len(seq)-1-i]

    
               

    def __getitem__(self, index):
        if index in self.poly.keys():
            return self.poly[index]
        else:
            return 0
        
    def __setitem__(self, index, value):
        self.poly[index]=value
        
    
    def __add__(self, poly1):
        "Return seq1+seq2."
        add=Polynomial()
        key=list(self.poly.keys())
        for i in key:
            add.poly[i]=self.poly[i]
                
        for i in poly1.poly.keys():
            if i in add.poly.keys():
                add.poly[i]+=poly1.poly[i]
            else:
                add.poly[i]=poly1.poly[i]
        for i in list(add.poly.keys()):
            if add.poly[i]==0:
                add.poly.pop(i,)
        return add
            
        
    def __sub__(self,poly1):
        "Return seq1-seq2."
        sub=Polynomial()
        key=list(self.poly.keys())
        for i in key:
            sub.poly[i]=self.poly[i]
        for i in poly1.poly.keys():
            if i in sub.poly.keys():
                sub.poly[i]-=poly1.poly[i]
            else:
                sub.poly[i]=0-poly1.poly[i]
     
        for i in list(sub.poly.keys()):
            if sub.poly[i]==0:
                sub.poly.pop(i,)
        return sub


    def __mul__(self,poly1):
        "Return s*v."
        mul=Polynomial()
        for i in self.poly.keys():
            for j in poly1.poly.keys():
                if i+j in mul.poly.keys():
                    mul.poly[i+j]+=self.poly[i]*poly1.poly[j]
                else:
                    mul.poly[i+j]=self.poly[i]*poly1.poly[j]
        for i in mul.poly.keys():
            if mul.poly[i]==0:
                mul.poly.pop(i,)        
        return mul
    
    def __eq__(self,poly1):
        "Return s==v."
        for i in self.poly.keys():
            if i in poly1.poly.keys():
                if poly1.poly[i]==self.poly[i]:
                    pass
                else:
                    return False
            else:
                return False
        return True
    
    def eval(self, x=10):
        eval=0
        for i in self.poly.keys():
            eval+=self.poly[i]*(x**i)
        return eval
    
    def deriv(self):
        seq=[]
        powers=[]
        for i in self.poly.keys():
            if(self.poly[i]*i!=0):
                powers.append(i-1)
                seq.append(self.poly[i]*i) 
         
        der=""
        deriv=Polynomial()
        for i in range(len(seq)):
            if(seq[i]>0):
                der+=str(seq[i])
            else:
                der+='('+str(seq[i])+')'
                
            if(powers[i])>1:
                der+='x**'+str(powers[i])
            elif(powers[i]==1):
                der+="x"
            elif(powers[i])<-1:
                der+='x**'+'('+str(powers[i])+')'
            if(i!=len(seq)-1):
                der+="+"
            deriv[powers[i]]=seq[i]
        
        return deriv
    
def main():
        p1=Polynomial([0,1,2,3])
        p2=Polynomial([0,2,3,4])
        p3=Polynomial()
        p3=p1+p2
        print(p3[0],p1[0])
        
if __name__=="__main__":
    main()