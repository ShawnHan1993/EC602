                       
\
\
\
\
   

class Polynomial():
    def __init__(self,value=0):
        self={0:value}
        
    def __getitem__(self,key):
        try:
            return self[key]
        except KeyError:
            self.missing(self,key)
        
    def __missing__(self,key):
        return 0

    def __setitem__(self,keys,value):
        self[keys]=value
    
    def __add__(self,value):
        result={0:0}
        a=list(dict(self).keys())
        b=list(dict(value).keys())
        i=0
        j=0
        while(i<len(a)):
            result[a[i]]=self.get(a[i],0)+value.get(a[i],0)
            i+=1
        while(j<len(b)):
            result[b[j]]=self.get(b[j],0)+value.get(b[j],0)
            j+=1
        return result
    
    def __sub__(self,value):
        result={0:0}
        a=list(dict(self).keys())
        b=list(dict(value).keys())
        i=0
        j=0
        while(i<len(a)):
            result[a[i]]=self.get(a[i],0)-value.get(a[i],0)
            i+=1
        while(j<len(b)):
            result[b[j]]=self.get(b[j],0)-value.get(b[j],0)
            j+=1
        return result
        
    def __mul__(self,value):
        result={0:0}
        a=list(dict(self).keys())
        b=list(dict(value).keys())
        i=0
        while(i<len(a)):
            j=0
            while(j<len(b)):
                result[a[i]+b[j]]=result.get(a[i]+b[j],0)+self[a[i]]*value[b[j]]
                j+=1
            i+=1
        return result
    
    def __eq__(self,value):
        i=cmp(dict(self),dict(value))
        if(i==0):
            return True
        else:
            return False
            
    def eval(self,value):
        result = 0
        a=list(dict(self).keys())
        i=0
        while(i<len(a)):
            result+=self[a[i]]*value**a[i]
            i+=1
        return result
        
    def derive(self):
        result={0:0}
        a=list(dict(self).keys())
        i=0
        while(i<len(a)):
            result[a[i]-1]=self[a[i]]*a[i]
            i+=1
        return result
