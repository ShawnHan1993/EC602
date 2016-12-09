
                                       

class Polynomial():

                                                      
 
	def __init__(self,values = [] ):
                                                    
		values.reverse()
		self.co = values
		self.d = {}
		for i in range(0,len(self.co)) :
			if self.co[i] != 0 :
				self.d[str(i)] = self.co[i]
 

	def __eq__(self,other):
		if self.eval() == other.eval():
			return True
		else:
			 return False
    
	def __str__(self):
		out = self.co
		out.reverse()
                     
  
		outstr = ""
		count = 1
		for key in reversed(sorted(self.d.keys())):
			if count == 1:
				if self.d[key] < 0 :
					outstr += "-"
			if (self.d[key] < 0) & (count != 1) :
				outstr += "- "
			if (self.d[key] >= 0) & (count != 1) :
				outstr += "+ "
			outstr += (str(abs(self.d[key])) + "X^" + key + " ")
			count += 1
   
			if key == "0" :
				outstr = outstr[:-4]
				outstr += " "
		return outstr 
   
 
	def __setitem__(self,key,val):
                
                                   
		self.d[str(key)] = val 
 
	def __getitem__(self,key):
		return self.d[str(key)] 

	def __add__(self,other):
		l1 = len(self.co)
		l2 = len(other.co)
		addition ={}
                                    
                                
              

                          
                                      
                          
                                    

                          

		for key1, val1 in self.d.items():
			addition[key1] = val1
			for key2, val2 in other.d.items():
				if key1 != key2 :
					addition[key2] = val2
				if key1 == key2 :
					addition[key1] += val2
   
  
		out = Polynomial([])
		out.d = addition
		return out

	def __sub__(self,other):
                    
                     
                                     
                                  
               

                         
                           
                         
                            

                           
  
		garb = {}

		for key1, val1 in self.d.items():
			garb[key1] = val1
			for key2, val2 in other.d.items():
				if key1 != key2:
					garb[key2] = -1 * val2
				if key1 == key2:
					garb[key1] -= val2  


		out=Polynomial([])
		out.d = garb
		return out

                          
                    
                     
  
                               
               
                           
                            
                                          
               
                          
                           
                                          

                
                         
                           
                                          
    
                              
 
	def __mul__(self,other) :
		a = max(map(int,self.d))
		b = max(map(int,other.d))

		stupid = {}

		store=list(range(0,a+b+1))

		for i in range (0,len(store)):
			store[i]=0

		for key, value in self.d.items():
			for key2,val2 in other.d.items():
                                                    
				newkey = str(int(key) + int(key2))
                                                      

				stupid[(newkey)] = (value * val2)
		returner = Polynomial([])
		returner.d = stupid
		return returner   

	def eval(self):
		thing = 0
		other = 0
                                  
                                 
                  
  
		for key,val in self.d.items():
                     
			thing = val * 10 ** int(key)
                
			other += thing
                    
                                     
		return other 
  

	def deriv(self):
                                            
                              
            
             
                               
                                   
   
                
                         
		bleh = {}

		for key,val in self.d.items():
			if key != "0":
				bleh[str(int(key)-1)]=int(key)*val 
		deriva = Polynomial([])
		deriva.d = bleh 
		return deriva
    


def main():
	pass

if __name__ == "__main__":
	main()

