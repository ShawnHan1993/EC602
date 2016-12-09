                                           


class Polynomial():
                   
    def __init__(self,seq2):
        self.seq = dict({})
        for i in range(len(seq2)):
            if(seq2[i] != 0):
                self.seq.update({(len(seq2)-i-1):seq2[i]})   
      
            
    
    def __add__(self,other):
        res = Polynomial([0])
        for i in self.seq:
            if(i in other.seq):
                res.seq[i] = self.seq[i] + other.seq[i]
            else:
                res.seq[i] = self.seq[i]
        for i in other.seq:
            if(not(i in self.seq)):
                res.seq[i] = other.seq[i]
        return res

    def __sub__(self,other):
        res = Polynomial([0])
        for i in self.seq:
            if(i in other.seq):
                res.seq[i] = self.seq[i] -  other.seq[i]
            else:
                res.seq[i] = self.seq[i]
        for i in other.seq:
            if(not(i in self.seq)):
                res.seq[i] = -other.seq[i]
        return res
    
    def __mul__(self,other):
        res = Polynomial([0])
        for i in self.seq:
            for j in other.seq:
                res.seq[i+j]=0
        for i in self.seq:
            for j in other.seq:
                res.seq[i+j]+=self.seq[i]*other.seq[j]
        return res
        
    def __eq__(self,other):
        res = True
        for i in self.seq:
            if(self.seq[i]!=other.seq[i]):
                res=False
        for i in other.seq:
            if(other.seq[i]!=self.seq[i]):
                res=False
        return res
        
    def __setitem__(self,index,value):
        if(value!=0):
            self.seq.update({index:value}) 
        
    def eval(self,val):
        res=0
        for i in self.seq:
            res += (self.seq[i]*(val**i))
        return res
        
    def deriv(self):
        res = Polynomial([0])
        for i in self.seq:
            if(i!=0):
                res.seq[i-1] = self.seq[i]*i
        return res
        
if __name__ == '__main__':
    main()