                                     
                                  
class Polynomial():
	def __init__(self, p = [0]):
  
            
		exp=[]
		val=[] 
		self.p=list(p)
  
		for i in range(len(self.p)):
			exp.append(i)
			val.append(self.p[len(self.p)-i-1])  
  
		self.p=dict(zip(exp,val))  
		print(self.p)
  
     
	def __add__(self, other):  
		p3=Polynomial()
        
		for i in self.p:
			if i in other.p:
				p3[i]=self.p[i]+other.p[i]
                        
			else:
				p3[i]=self.p[i]
                        
		for i in other.p:
			if i not in self.p:
				p3[i]=other.p[i]
                        
		print(p3)         
                        
		return p3  
  
	def __sub__(self, other):
		p3={}
		for i in self.p:
			if i in other.p:
				p3[i]=self.p[i]-other.p[i]
			else:
				p3[i]=self.p[i]
		for i in other.p:
			if i not in self.p:
				p3[i]=other.p[i]
            
		return Polynomial(p3)
  
	def __mul__():
		pass
  
	def __eq__(self, other):
		if len(self.p) != len(other.p):
			return False
		else:
			for i in range(len(self.p)):
				if(other.p[i] == self.p[i]):
					flag=1
				else:
					flag=0
			if(flag==1):
				return True  
  
	def deriv(self):
		dpdx = Polynomial(self.p[:]) 
		dpdx.differentiate()
		return dpdx
  
	def eval(self, x):
		ans=0
		for i in range(len(self.p)):
			ans +=self.p[i]*(x**(len(self.p)-i-1))
		return ans
 
	def __setitem__(self,key,item):
                                                                   
                                 
		self.p[key]=item

	def __getitem__(self,key):
		if key>len(self.p):
			return "None"
		elif not self.p[len(self.p)-key-1]:
			return "None"
		else:
			return self.p[len(self.p)-key-1] 
  
	def __str__(self):
                
		s = ''
		for i in self.p:
			if self.p[i] != 0:
				s += "+({}*x^{})".format(self.p[i],i)
                           
                                        
		return s
    
	def __repr__(self):
		return self.__str__()

def main():
       
	p1=Polynomial([1.4,2,3.4,4.2])
                                                    
                            
          
                    
 
       
	p2=Polynomial([5,6.4,7.2])
                                        
                            
          
                    
            
           
 
	p3=p1 + p2
	print(p3)
 
  
if __name__ == '__main__':
    main()
