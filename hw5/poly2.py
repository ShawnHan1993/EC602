\
\
\
\
   

class Polynomial():
    "Polynomial([4,-9,5.6]) "

    def __init__(self, lst=[]):     
        a = len(lst)
        if a ==0:
            self.coef=[]
            self.exp=[]
        
        b = a - 1
        self.coef=[]
        self.exp=[]
        for i in range(a):
            if lst[i]!= 0:
                self.coef.append(lst[i])
                self.exp.append(b)
            b-=1
        
    def __add__(self,value):
        "Return self+value."
        if value!=[]:
            c = Polynomial(value)
            for j in range(len(c.exp)):
                flag = 0
                for i in range(len(self.exp)):
                    if self.exp[i] == c.exp[j]:
                        self.coef[i] += c.coef[j]
                        flag = 1
                if flag == 0:
                    z = 0
                    for m in range(len(self.exp)):
                        p = len(self.exp) - 1
                        if c.exp[j] > self.exp[p-m]:
                            z +=1
                    if z > 0:
                        self.exp.insert(p-z, c.exp[j])
                        self.coef.insert(p-z, c.coef[j])
                    else:
                        self.coef.append(c.coef[j])
                        self.exp.append(c.exp[j])
                                     
        return self.coef, self.exp
                        
    def __sub__(self, value): 
        n=0 
        if value!=[]:
            c = Polynomial(value)
            for j in range(len(c.exp)):
                flag = 0
                for i in range(len(self.exp)):
                    if self.exp[i] == c.exp[j]:
                       
                        self.coef[i] -= c.coef[j]
                        flag = 1
                        
                if flag == 0:
                    z = 0
                    for m in range(len(self.exp)):
                        p = len(self.exp) - 1
                        if c.exp[j] > self.exp[p-m]:
                            z +=1
                    if z > 0:
                        self.exp.insert(p-z, c.exp[j])
                        self.coef.insert(p-z, -c.coef[j])
                    else:
                        self.coef.append(-c.coef[j])
                        self.exp.append(c.exp[j])
            while (n<len(self.coef)):
                if self.coef[n] == 0:
                    y = self.exp[n]
                    self.coef.remove(0)
                    self.exp.remove(y) 
                else:
                    n += 1
                 
        return self.coef, self.exp
        
    def __equal__(self,value):
        equality = True
        if value!=[]:
            c = Polynomial(value)
            if len(c.coef) != len(self.coef):
                equality = False
            else:
                for i in range(len(self.coef)):
                    if self.coef[i]==c.coef[i] and self.exp[i]==c.exp[i]:
                        equality = True
                    else:
                        equality = False
        else:
            if self !=[]:
                equality = False
            else:
                equality =True
        return equality
        
    def deriv(self):
        temp=[]
        for i in range(len(self.coef)):
            temp.append(self.coef[i]*(self.exp[i]))
        for i in range(len(temp)):
            if temp[i]==0:
                temp.remove(0)
        self.coef = temp
        for j in range(len(self.exp)):
            self.exp[i]=self.exp[i]-1
        for i in range(len(self.exp)):
            if self.exp[i]==-1:
                self.exp.remove(-1)
        return self.coef, self.exp
                    
    def __getitem__(self,Key):
        for i in range(len(self.exp)):
            if self.exp[i] == Key:
                return self.coef[i]
            else:
                return 0
                
    def __setitem__(self,Key,value):
        for i in range(len(self.exp)):
            if self.exp[i] == Key:
                self.coef[i] = value
            else:
                self.exp.append(Key)
                self.coef.append(value)
    
    
