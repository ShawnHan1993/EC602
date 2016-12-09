                 
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
    def __init__(self,seq=[], powers=[] ):
        self.poly={}
        self.seq=[]
        self.powers=[]
        i=0;
        for i in range(len(powers)):
            if(seq[i]!=0):
                self.seq.append(seq[i])
                self.powers.append(powers[i])
                self.poly[self.powers[-1]]=self.seq[-1]
    
               

    def __getitem__(self, index):
        if index in self.poly.keys():
            return self.poly[index]
        else:
            return 0
        
    def __setitem__(self, index, value):
        self.poly[index]=value
        
    
    def __add__(self, poly1):
        "Return seq1+seq2."
        add=Polynomial(self.seq, self.powers)
        for i in poly1.poly.keys():
            if i in add.poly.keys():
                add.poly[i]+=poly1.poly[i]
            else:
                add.poly[i]=poly1.poly[i]
        for i in add.poly.keys():
            if add.poly[i]==0:
                add.poly.pop(i,)
        return add
            
        
    def __sub__(self,poly1):
        "Return seq1-seq2."
        sub=Polynomial(self.seq, self.powers)
        for i in poly1.poly.keys():
            if i in sub.poly.keys():
                sub.poly[i]-=poly1.poly[i]
            else:
                sub.poly[i]=-poly1.poly[i]
        for i in sub.poly.keys():
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
        der=[]
        for i in range(list(self.poly.keys())[-1]+1):
            if i in self.poly.keys():
                der.append(self.poly[i])
            else:
                der.append(0)
        return der
    
    
def main():
        p1=Polynomial([0,1,2,3],[1,2,3,4])
        p2=Polynomial([0,1,2,3],[1,2,3,4])
                                         
        p3=p1*p2
        print(p1.deriv())
        print(p3.deriv())
        print(p3.eval(10))


if __name__=="__main__":
    main()