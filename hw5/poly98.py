                                

                       
\
\
\
\
   

class Polynomial():
    
    
    def __init__(self,s=[],f=0):
        
        self.poly = list(s)
        self.flag = f
        self.len = len(s)   
                                 
                               
        self.len_p = self.len - f
        self.len_n = f
        self.exp = []
        
        for i in range(self.len_p)[::-1]:
            self.exp.append(i)
        for i in range(1,self.len_n+1):
            self.exp.append(-i)
                         
        
    
    def __str__(self):
        
        self.v = ""
        sign = '+'
        x = 'x'
        power = '^'
        
        if self.poly != []:
            self.v = self.v + "{}{}{}{}".format(self.poly[0],x,power,self.exp[0]) 
        else:
            self.v = self.v
        
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
               
        if self.v == "":
            return '0'
        else:
            return self.v
    
    def __getitem__(self,key):
        
        if key > self.len_p:
            return 0
        else:
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
        if self.poly == []:
            if value == 0:
                self.poly = self.poly
            if key < 0:
                self.poly.append(value)
                self.exp.append(key)
                self.len = self.len+1
                self.len_n = self.len_n+1

        else:
            
                    
            if key > (self.len_p-1):
                expoly.append(value)
                               
                
                for i in range(key-(self.len-1)-1):
                    expoly.append(0)
                               
                for i in range(self.len):
                    expoly.append(self.poly[i])
                               
                self.poly = expoly
                self.len = key+1
                self.len_p = key+1
                self.exp = range(key+1)[::-1]
                                  
                
            elif key < 0:
                coe = []
                exp = []
                if key < self.poly[self.len-1]:
                    dif_neg = 0
                                     
                                    
                    for i in range(self.len):
                        coe.append(self.poly[i])
                        exp.append(self.exp[i])
                                       
                                                     
                    dif_neg = abs(key)-abs(self.exp[self.len-1])
                    for i in range(abs(self.exp[self.len-1])+1,abs(key)):
                        coe.append(0)
                        exp.append(-i)
                    coe.append(value)
                    exp.append(key)
                    self.poly = coe
                                                  
                    
                    self.len_n = dif_neg+abs(self.exp[self.len-1])
                    self.len = self.len+dif_neg
                           
                                             
                    self.exp = exp
                                            
                                             
                else:
                    for i in range(self.len):
                        if self.exp[i] == key:
                            mark2 = i
                    self.poly[mark2] = value
                        
                
            else:
                self.poly[self.len-1-key] = value
        
                                  
        
    def __add__(self,value):
        self.temp = []
        len_flag = 0
        if hasattr(value,'poly'):
            if self.len_p >= value.len_p:
                
                dif_len = self.len_p - value.len_p

                for j in range(dif_len):
                    self.temp.append(self.poly[j])
                for i in range(value.len_p):
                    self.temp.append(self.poly[i+dif_len] + value.poly[i])                    
            else:
                
                dif_len = value.len_p - self.len_p
                
                for j in range(dif_len):
                    self.temp.append(value.poly[j])
                for i in range(self.len_p):
                    self.temp.append(self.poly[i] + value.poly[i+dif_len]) 
            
                                     
                                      
            if self.len_n >= value.len_n:
                
                dif_lenn = self.len_n - value.len_n
                
                for i in range(value.len_n):
                    self.temp.append(self.poly[self.len_p+i] + value.poly[value.len_p+i])
                for j in range(dif_lenn):
                    self.temp.append(self.poly[self.len_p+value.len_n+j])
                               
                len_flag = self.len_n
            
            else:
                dif_lenn = value.len_n - self.len_n
                
                for i in range(self.len_n):
                    self.temp.append(self.poly[self.len_p+i] + value.poly[value.len_p+i])
                for j in range(dif_lenn):
                    self.temp.append(value.poly[value.len_p+self.len_n+j])
                    
                len_flag = value.len_n
                
                              
                                  
                    
        else:
                                
            for i in range(0,self.len-1):
                self.temp.append(self.poly[i])
                
            self.temp.append(self.poly[self.len-1] + value)    
            
                                     
        
        return Polynomial(self.temp,len_flag)   
            
                                     
        
                                     
        
    def __sub__(self,value):

        self.temp = []
        len_flag = 0
        if hasattr(value,'poly'):
            if self.len_p >= value.len_p:
                
                dif_len = self.len_p - value.len_p

                for j in range(dif_len):
                    self.temp.append(self.poly[j])
                for i in range(value.len_p):
                    self.temp.append(self.poly[i+dif_len] - value.poly[i])                    
            else:
                
                dif_len = value.len_p - self.len_p
                
                for j in range(dif_len):
                    self.temp.append(-value.poly[j])
                for i in range(self.len_p):
                    self.temp.append(self.poly[i] - value.poly[i+dif_len]) 
            
                                     
                                      
            if self.len_n >= value.len_n:
                
                dif_lenn = self.len_n - value.len_n
                
                for i in range(value.len_n):
                    self.temp.append(self.poly[self.len_p+i] - value.poly[value.len_p+i])
                for j in range(dif_lenn):
                    self.temp.append(self.poly[self.len_p+value.len_n+j])
                               
                len_flag = self.len_n
            
            else:
                dif_lenn = value.len_n - self.len_n
                
                for i in range(self.len_n):
                    self.temp.append(self.poly[self.len_p+i] - value.poly[value.len_p+i])
                for j in range(dif_lenn):
                    self.temp.append(-value.poly[value.len_p+self.len_n+j])
                    
                len_flag = value.len_n
                
                              
                                  
                    
        else:
                                
            for i in range(0,self.len-1):
                self.temp.append(self.poly[i])
                
            self.temp.append(self.poly[self.len-1] - value)    
            
                                     
        
        return Polynomial(self.temp,len_flag)
        

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
            val = val + self.poly[i]*(value**(self.exp[i]))   
                               
        return val
        
    def deriv(self):
        
        der = []
        
        if self.len_n == 0:
            negnum = 0
            for i in range(self.len_p-1):    
                der.append(self.poly[i]*(self.exp[i]))
                         
        else:
            for i in range(self.len_p):
                
                der.append(self.poly[i]*(self.exp[i]))
                       
            for i in range(self.len_n):
                der.append(self.poly[self.len_p+i]*self.exp[self.len_p+i])
                       
                negnum = self.len_n+1

        return Polynomial(der,negnum)

    
      
def main():
    

    
    num = Polynomial([])
    num[-6] = 10
    print("num=",num)
    
    print(num.eval(2))
    if num.eval(2) == 0.15625:
        print("yaerma")
    else:
        print("mao")
    

    
    
    

    
if __name__=="__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
