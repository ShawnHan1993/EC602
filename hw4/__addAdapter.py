# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:35:55 2016

@author: Shawn Han
"""
# AUTHOR Xinyu Li lxinyu@bu.edu
"""        
    def __addAdapter(self,value,x,y,result):
        if x<0 and y<0:
            return result
        else:
            if x<0 or self.Ord[x]>value.Ord[y]:
                result.Coe.insert(0,value.Coe[y])
                result.Ord.insert(0,value.Ord[y])
                result.n=result.n+1
                return self.__addAdapter(value,x,y-1,result)
            if y<0 or self.Ord[x]<value.Ord[y]:
                result.Coe.insert(0,self.Coe[x])
                result.Ord.insert(0,self.Ord[x])
                result.n=result.n+1
                return self.__addAdapter(self,value,x-1,y,result)
            if self.Ord[x]==value.Ord[y]:
                if (self.Coe[x]+value.Coe[y])!=0:    
                    result.Coe.insert(0,self.Coe[x]+value.Coe[y])
                    result.Ord.insert(0,self.Ord[x])
                    result.n=result.n+1
                return self.__addAdapter(value,x-1,y-1,result)
"""  


        try:
            while True:
                loc=self.Coe.index(0)
                del self.Coe[loc]
                del self.Ord[loc]
                self.n=self.n-1
        except:
            pass
        
