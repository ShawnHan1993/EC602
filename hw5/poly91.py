
                                  
                                          


class Polynomial():
    "Polynomial([4,-9,5.6]) "

    def __init__(self, lst=[]):   
        
        a = len(lst)
        result = []
        if a ==0:
            self.coef=[]
            self.exp=[]
            result.append(self.coef)
            result.append(self.exp)
        
        b = a - 1
        self.coef=[]
        self.exp=[]
        for i in range(a):
            if lst[i]!= 0:
                self.coef.append(lst[i])
                self.exp.append(b)
            b-=1
        result.append(self.coef)
        result.append(self.exp)
        
    def __add__(self,value):
        "Return self+value."
        "if value!=[]:"
        "c = Polynomial(value)"
        a_coef = []
        a_exp =[]
        for i in self.coef:
            a_coef.append(i)
        for i in self.exp:
            a_exp.append(i)
        for j in range(len(value.exp)):
            flag = 0
            for i in range(len(a_exp)):
                if a_exp[i] == value.exp[j]:
                    a_coef[i] += value.coef[j]
                    flag = 1
            if flag == 0:
                z = 0
                for m in range(len(a_exp)):
                    p = len(self.exp) - 1
                    if value.exp[j] > a_exp[p-m]:
                        z +=1
                if z > 0:
                    a_exp.insert(p-z, value.exp[j])
                    a_coef.insert(p-z, value.coef[j])
                else:
                    a_coef.append(value.coef[j])
                    a_exp.append(value.exp[j])
                    
        
        return a_coef, a_exp
                        
    def __sub__(self, value): 
        n=0 
        "if value!=[]:"
        a_coef = []
        a_exp =[]
        for i in self.coef:
            a_coef.append(i)
        for i in self.exp:
            a_exp.append(i)
        "c = Polynomial(value)"
        for j in range(len(value.exp)):
            flag = 0
            for i in range(len(a_exp)):
                if a_exp[i] == value.exp[j]:
                    
                    a_coef[i] -= value.coef[j]
                    flag = 1
                    
            if flag == 0:
                z = 0
                for m in range(len(a_exp)):
                    p = len(a_exp) - 1
                    if value.exp[j] > a_exp[p-m]:
                        z +=1
                if z > 0:
                    a_exp.insert(p-z, value.exp[j])
                    a_coef.insert(p-z, -value.coef[j])
                else:
                    a_coef.append(-value.coef[j])
                    a_exp.append(value.exp[j])
        while (n<len(a_coef)):
            if a_coef[n] == 0:
                y = a_exp[n]
                a_coef.remove(0)
                a_exp.remove(y) 
            else:
                n += 1
                 
        return a_coef, a_exp
        
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
        return 0
                
    def __setitem__(self,Key,value):
        for i in range(len(self.exp)):
            if self.exp[i] == Key:
                self.coef[i] = value
        self.exp.append(Key)
        self.coef.append(value)
        
    def eval(self,value):
        tempSum = 0
        dictionary = dict(zip(self.exp, self.coef))
        for i in dictionary:
            tempSum += dictionary[i]*(value**(i))
        return tempSum
    
    def __mul__(self,value):
        flag2=0
        temp = Polynomial([])
        "Return s*v."
        "x = Polynomial(value)"
        for i in range(len(value.exp)):
            for j in range(len(self.exp)):
                for m in range(len(temp.exp)):
                    if self.exp[j] + value.exp[i] == temp.exp[m]:
                        temp.coef[m] += self.coef[j]*value.coef[i]
                        flag2 = 1
                if flag2 == 0:
                    temp.exp.append(self.exp[j]+value.exp[i])
                    temp.coef.append(self.coef[j]*value.coef[i])
        return temp.coef, temp.exp
    
    def __str__(self):
        
        pass
    
    
    def __repr__(self):
        pass
    
    def __radd__(self,value):
        return self.__add__(value)
    
