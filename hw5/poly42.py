class Polynomial():
    
    def __init__(self,value=None):
        if(value ==None):
            self.index = 0
        else:
            self.index = len(value)
        self.value = {}
        i=0
        if (isinstance(value,list)):
            while(self.index>0):
                if (value[i]!=0):
                    temp = {(self.index-1):value[i]}
                    self.value.update(temp)
                self.index-=1
                i+=1
        if (isinstance(value,dict)):
            for keys in value:
                if (value[keys]!=0):
                    temp1 = {keys:value[keys]}
                    self.value.update(temp1)
    def __getitem__(self,i):
        if(i in self.value.keys()):
            return self.value[i]
        else:
            return 0
    def __setitem__(self,idx,val):
        if (val!=0):
            temp1 = {idx:val}
            self.value.update(temp1)
        else:
            del self.value[idx]
    def __add__(self,var):
        result={}
        result.update(self.value)
        for keys in var.value.keys():
            if keys in self.value.keys():
                result[keys]+=var.value[keys]
            else:
                temp ={keys:var.value[keys]}
                result.update(temp)
                temp.clear()
        return Polynomial(result)
        
                    
    def __sub__(self,var):
        result = {}
        result.update(self.value)
        for key in var.value.keys():
            var.value[key]=-var.value[key]
        result.update(var.value)
        for keys in self.value.keys():
            for keys1 in var.value.keys():
                if(keys1==keys):
                    result[keys]+=self.value[keys]
        
        return Polynomial(result)
    
    def __eq__(self,var):
        return self.value ==var.value
    def __ne__(self,var):
        result = self.value.__eq__(var.value)
        if result is NotImplemented:
            return result
        return not result
        
    def clear(self):
        self.value={}
        return self.value
        
    def __mul__(self,var):
        result={}
        temp={}
        temp1={}
        for keys in var.value.keys():
            for keys1 in self.value.keys():
                temp[keys+keys1]=self.value[keys1]*var.value[keys]
            temp1=result.copy()
            result.update(temp)
            for keys2 in temp1.keys():
                for keys3 in temp.keys():
                    if(keys2 == keys3):
                        result[keys2]+=temp1[keys2]
            temp.clear()
        return Polynomial(result)
        
    def deriv(self):
        
        derivative ={}
        for keys in self.value.keys():
            if (keys!=0):
                temp ={keys-1:(self.value[keys]*keys)}
                derivative.update(temp)
        return Polynomial(derivative)
                
    def __str__(self):
        string = ""
        a=sorted(self.value.keys(),reverse=True)
        for keys in a:
            string += "({}:{})".format(keys,self.value[keys])
        return string
        
    def eval(self,x):
        result = 0.0
        for keys in self.value.keys():
            result +=self.value[keys]*x**keys
        return result



                                   
