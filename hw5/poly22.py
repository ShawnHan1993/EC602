                                       
                  

class Polynomial():
     def __init__(self, coeff=[]):
        self.coeff=coeff      
        self.coeff=dict({})
        aa=len(coeff)        
        for i in range(aa):
            if coeff[i] != 0:
                self.coeff.update({aa - i - 1:coeff[i]})
                          
                                
                            
                              
                    
                                
                                  
                                                             
     def __str__(self):
        outstr = ""
        a = reversed(sorted(self.coeff))
        for i in a:
                if i>1 or i<0:
                    outstr += "%sx^%d + " %(str(self.coeff[i]),i)
                if i==1:
                    outstr += "%sx + " %(str(self.coeff[i]))
                if i==0:
                    outstr += "%s + " %(str(self.coeff[i]))
        outstr += "0"
        return outstr
        
     def __setitem__(self,exp,coeff): 
        self.coeff.update({exp:coeff})

     def __getitem__(self,exp): 
        if exp in self.coeff:
             return self.coeff[exp]
        else:
             return 0
                           
     def __add__(self, other):
                                                       
        a=reversed(sorted(self.coeff))
        b=reversed(sorted(other.coeff))
        out=Polynomial([])
        
        for i in a:
            if i in other.coeff:
                out.coeff.update({i:self.coeff[i]+other.coeff[i]})
            if i not in other.coeff:
                out.coeff.update({i:self.coeff[i]})
        for i in b:
            if i not in self.coeff:
                out.coeff.update({i:other.coeff[i]})
        return out
        
     def __sub__(self, other):
                                                       
        a=reversed(sorted(self.coeff))
        b=reversed(sorted(other.coeff))
        out=Polynomial([])
        
        for i in a:
            if i in other.coeff:
                out.coeff.update({i:self.coeff[i]-other.coeff[i]})
            if i not in other.coeff:
                out.coeff.update({i:self.coeff[i]})
        for i in b:
            if i not in self.coeff:
                out.coeff.update({i:-other.coeff[i]})
        return out
        
     def __mul__(self, other):
        out=Polynomial([])
        for i in self.coeff:
            for j in other.coeff:
                if(i+j) in out.coeff:
                    out.coeff[i+j] += (self.coeff[i]*other.coeff[j])
                else:
                    out.coeff[i+j] = (self.coeff[i]*other.coeff[j])
        return out

     def __eq__(self, other):
        for i in self.coeff:
            if i not in other.coeff:
                if self.coeff[i] !=0:
                    return False
            if self.coeff[i] != other.coeff[i]:
                return False
        for j in other.coeff:
            if j not in self.coeff:
                if other.coeff[j] !=0:
                    return False
        return True
        
     def eval(self, val):
        out=0
        for i in self.coeff:
            out += self.coeff[i]*val**i
        return out
    
     def deriv(self):
        out=Polynomial([])
        for i in self.coeff:
             out.coeff[i-1]=self.coeff[i]*i
        return out

def main():
    pass
                          
                            
                   
            
              
          
              
     
                
                
           
           
 
                               
                               
                               
                               
                               
                                
                               
                                  
                              

if __name__=="__main__":
	main()