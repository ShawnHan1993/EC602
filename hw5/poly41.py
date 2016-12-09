                                        
 
                  
 
 
                                                                                  
                                                                            
                  
                                                                     
                                                     
                                                            
                                                                       
                                                                                             
                                                                                        
                                                                                              
                                                                 
                                                                                            



class Polynomial():

                                                             
	def __init__ (self,coef=[]):
		self.poly = {}                                                   
		expon = len(coef)-1                                                 
		for i in coef:
			if i != 0:                                                
				self.poly[expon] = i
			expon -= 1
   
	def __str__(self):
                                  
		"Prints nice version of Polynomial"
		ans = ""
		for expon, coef in self.poly.items():
                                                                         
				ans += str(coef) + "x^" + str(expon) + " + "
          
              
		return ans[0:len(ans)-3]                                                        
                                                    

	def __repr__(self):
		"Prints dictionary of poly"
		return str(self.poly)


	def __setitem__(self, expon, coef):
                                                          
		"Used to set a[i] = v, Assign new coef, v, to exponent, i"
                            
		if coef != 0:
			self.poly[expon] = coef

		else:
                                               
			del self[expon] 

	def __getitem__(self, expon):
                                                                 
		"Used to get a[i] and return 0 if expon is not present"
		if expon in self.poly:
			return self.poly[expon]
		else:
			return 0

	def __delitem__(self, expon):
                                            
		"Delete exponent"
		if expon in self.poly:
			self.poly.pop[expon] 

	def __len__(self):
                                                  
		"Give length of polynomial"
		return len(self.poly)


	def __add__ (self, add):
                                 
		"Return self+add"
		ans = Polynomial([])
		ans.poly = self.poly.copy()

		for expon, coef in add.poly.items():
			if expon in ans.poly: 
				ans[expon] += coef                                
				if ans.poly[expon] == 0:
					del expon                           
				else:
					pass
			else:
				ans[expon] = coef                               
		return ans

	def __sub__(self, sub):
                                      
		"Return self-sub"
		ans = Polynomial([])
		ans.poly = self.poly.copy()

		for expon, coef in sub.poly.items():
			if expon in ans.poly:
				ans[expon] -= coef                                
				if ans.poly[expon] == 0:
					del ans[expon]
				else:
					pass
			else:
				ans[expon] = coef                               
		return ans

	def __mul__(self,mult):
                                      
		"Retun self*mult"
		ans = Polynomial([])
		ans.poly = self.poly.copy()

		for exponA, coefA in mult.poly.items():
			for exponB, coefB in ans.poly.items():  
				if (exponA+exponB) in ans.poly:
					ans.poly[exponA+exponB] += coefA*coefB
				else:
					ans.poly[exponA+exponB] = coefA*coefB
		return ans
     

	def __eq__(self,eq):
                                          
		"Return value is 'True' or 'False'"
                       
                              
                         
                                              

		if len(self.poly) > len(eq.poly):
			return False
		else:
			for exponA, coefA in self.poly.items():
				for exponB, coefB in eq.poly.items(): 
					if (exponA == exponB and coefA == coefB):
						return True
					else:
						return False
  

	def eval(self, value):
                                                                   
		number = 0

		for expon, coef in self.poly.items():
			number += coef * value**expon
		return number

	def deriv(self):
		ans = Polynomial([])
		for expon, coef in self.poly.items():
			ans[expon-1] += coef*expon 
		return ans
 
