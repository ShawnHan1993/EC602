                                  
                            

\
\
\
\
   

class Polynomial():




    def __init__(self,seq=[0]):
        
        lg=len(seq)
        self.dict={0:0}
        self.dict[0]=0
        
        for a in range(lg):
            self.dict[a]=seq[lg-a-1]
        
        
        
        
        
    def __setitem__(self,key,value):
        self.dict[key]=value
        
           
      
      
    def __add__(self,value):
        dictadd={}
        for a in self.dict:
            try:
                dictadd[a]=self.dict[a]+value.dict[a]
            except:
                dictadd[a]=self.dict[a]
        
        for b in value.dict:
            try:
                dictadd[b]=value.dict[b]+self.dict[b]
            except:
                dictadd[b]=value.dict[b]
        
        
        res=Polynomial([])
        for c in dictadd:
            res[c]=dictadd[c]
  
    
        killlist=[]
        for d in res.dict:
            if res.dict[d]==0:
               killlist.append(d) 
        
        for e in killlist:
            del res.dict[e]
            
            
            
            
        return res
                
 

      
    def __sub__(self,value):
        dictsub={}
        for a in self.dict:
            try:
                dictsub[a]=self.dict[a]-value.dict[a]
            except:
                dictsub[a]=self.dict[a]
        
        for b in value.dict:
            try:
                dictsub[b]=value.dict[b]-self.dict[b]
            except:
                dictsub[b]=-(value.dict[b])
        
        
        res=Polynomial([])
        for c in dictsub:
            res[c]=dictsub[c]
            
            
            
            
        killlist=[]
        for d in res.dict:
            if res.dict[d]==0:
               killlist.append(d) 
        
        for e in killlist:
            del res.dict[e]
            
        return res        
        

    def __mul__(self,value):
        
        
        res=Polynomial([])
        for a in self.dict:
            
            tem1=Polynomial([])
            for b in value.dict:
                tem1[b+a]=value.dict[b]*self.dict[a]
            res=tem1+res
        
        
        
        
        
        
        
            
        killlist=[]
        for d in res.dict:
            if res.dict[d]==0:
               killlist.append(d) 
        
        for e in killlist:
            del res.dict[e]
        
        return res
        
    def __eq__(self,other):
        res=True
        ret=True
        
            
            
            
        for a in self.dict:
                
            try:
                res=(other.dict[a]==self.dict[a])
            except:

                res=False
                if self.dict[a]==0:
                    res=True
                    
                    
            if (not res):
                    ret=False
                    
        for b in other.dict:
                
            try:
                res=(other.dict[b]==self.dict[b])
            except:
                res=False
                if other.dict[b]==0:
                    res=True
        
        if (not res):
            ret=False
        
        
        return ret
        
    def deriv(self):
        ghost=self.dict[0]
        del self.dict[0]
        dictderiv=Polynomial([])
        for a in self.dict:
            dictderiv[a-1]=a*(self.dict[a])
            
        self.dict[0]=ghost
        return dictderiv



    def eval(self,value):
        res=0
        
        for a in self.dict:
            res=res+self.dict[a]*(value**a)
        try:
            
            res=res
        except:
            res=res
            
        return res
                    
            
    def __str__(self):
        sss=' '
        for a in self.dict:
            sss=sss+'+{}X**{}'.format(self.dict[a],a)
        
        
        return sss
        
    def __repr__(self):
        return str(self)
            
                
                
        
        

        
        
        
    
        
        


































def main():
    pass

if __name__=="__main__":
    main()