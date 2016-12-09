                                  

                       
\
\
\
\
   

class Polynomial():
    
    def __init__(self,s):
        
        self.poly = s
        self.len = len(s)    
        self.exp = range(self.len)[::-1]
    
    def __str__(self):
        
        self.v = "f(x)="
        sign = '+'
        x = 'x'
        power = '^'
        
        self.v = self.v + "{}{}{}{}".format(self.poly[0],x,power,self.exp[0])        
        
        for n in range(1,self.len):
            if self.poly[n] < 0:           
                sign = ''
                if self.exp[n] == 0:
                    self.v = self.v + "{}{}".format(sign,self.poly[n]) 
                else:
                    self.v = self.v + "{}{}{}{}{}".format(sign,self.poly[n],x,power,self.exp[n])
                sign = '+'
            
            elif self.poly[n] == 0:
                self.v = self.v
            
            else:
                if self.exp[n] == 0:
                    self.v = self.v + "{}{}".format(sign,self.poly[n]) 
                else:
                    self.v = self.v + "{}{}{}{}{}".format(sign,self.poly[n],x,power,self.exp[n])
               
        return self.v
    
    def __getitem__(self,key):
        ncounter = 0
        mark = 0
        for i in range(self.len):
            if self.exp[i] < 0:
                ncounter = ncounter+1
                if self.exp[i] == key:
                    mark = i
            
                              
                               
        if key >=0 :
            return self.poly[self.len-1-ncounter-key]
        else:
            return self.poly[mark]
          
    def __setitem__(self,key,value):
        
        expoly = []        
        
        if key > (self.len-1):
            expoly.append(value)
                           
            
            for i in range(key-(self.len-1)-1):
                expoly.append(0)
                           
            for i in range(self.len):
                expoly.append(self.poly[i])
                           
            self.poly = expoly
            self.len = key+1
            self.exp = range(key+1)[::-1]
                              
            
        elif key < 0:
            coe = []
            exp = []
                             
                            
            for i in range(self.len):
                coe.append(self.poly[i])
                exp.append(self.exp[i])
            coe.append(value)
            exp.append(key)
            self.poly = coe
                                          
            self.len = self.len+1
                   
                                     
            self.exp = exp
                                    
                                     
            
        
        else:
            self.poly[self.len-1-key] = value
        
        
        
    def __add__(self,value):
        self.temp = []
        if hasattr(value,'poly'):
            if self.len >= value.len:
                
                dif_len = self.len - value.len

                for j in range(dif_len):
                    self.temp.append(self.poly[j])
                for i in range(value.len):
                    self.temp.append(self.poly[i+dif_len] + value.poly[i])
        
            else:
                
                dif_len = value.len - self.len
                
                for j in range(dif_len):
                    self.temp.append(value.poly[j])
                for i in range(self.len):
                    self.temp.append(self.poly[i] + value.poly[i+dif_len]) 
        
            
        else:
            
            for i in range(0,self.len-1):
                self.temp.append(self.poly[i])
                
            self.temp.append(self.poly[self.len-1] + value)    
            
                                     
        
        return Polynomial(self.temp)
        
    def __sub__(self,value):

        self.temp = []
        if hasattr(value,'poly'):
            if self.len >= value.len:
                
                dif_len = self.len - value.len

                for j in range(dif_len):
                    self.temp.append(self.poly[j])
                for i in range(value.len):
                    self.temp.append(self.poly[i+dif_len] - value.poly[i])                    
            else:
                
                dif_len = value.len - self.len
                
                for j in range(dif_len):
                    self.temp.append(value.poly[j])
                for i in range(self.len):
                    self.temp.append(self.poly[i] - value.poly[i+dif_len]) 
                    
        else:
            
            for i in range(0,self.len-1):
                self.temp.append(self.poly[i])
                
            self.temp.append(self.poly[self.len-1] - value)    
            
                                     
        
        return Polynomial(self.temp)
        

    def __mul__(self,value):
        
        if self.len < value.len:
            na = value.poly
            nb = self.poly
            la = value.len
            lb = self.len
        
        else:
            na = self.poly
            nb = value.poly
            la = self.len
            lb = value.len
            
        y = []
        
        bias = lb
        counter = la-1
        counter2 = 0
        counter3 = bias-2
        
        for i in range(la-1,la-lb-1,-1):
            
            summ = 0.0;
            for j in range(la-1,i-1,-1):
                
                                                 
                summ = summ + float(na[j])*float(nb[lb-1-j+counter])
                
            counter = counter-1
            y.append(summ)
                          
            
        for i in range(la-lb-1,-1,-1):
            
            summ = 0.0
            for j in range(i+lb-1,i-1,-1):
        
                summ = summ + float(na[j])*float(nb[lb-1-j])
                
                counter2 = counter2 + 1
            y.append(summ)
                         
            
        for i in range(bias-2,-1,-1):
            
            summ = 0.0
            for j in range(i,-1,-1):
                summ = summ + float(na[j])*float(nb[counter3-j])
                
            counter3 = counter3 -1
            y.append(summ)
            
        y = y[::-1]
    
        return (Polynomial(y))    
        
    def __eq__(self,value):
        
        if self.poly == value.poly:
            return True
        else:
            return False
    
    def eval(self,value):
        
        val = 0
        for i in range(self.len):
            val = val + self.poly[i]*(value**(self.len-1-i))   
            print('val=',val)
        return val
        
    def deriv(self):
        
        der = []
        for i in range(self.len-1):
            der.append(self.poly[i]*(self.len-1-i))
            
        return Polynomial(der)

    
      
def main():
    
    p = Polynomial([1,2,3,4])
    
   
    
    q = Polynomial([4,4,4])
    
    p[-5] = 7
    
    p[-7] = 8

    print(p)
    print(q)
    print(p[-7])
    print(p[-5])
    print(p[3])


    
if __name__=="__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
