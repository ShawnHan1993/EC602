                                

class Polynomial():
 
	def __init__(self,coef):
		self.coef = coef
		CoefCnt = len(self.coef)
		self.expo = {}
		for i in range(CoefCnt):
			self.expo[i] = self.coef[CoefCnt - i - 1]

	def __getitem__(self,expo):
		return self.expo[expo]

                                           
	def __setitem__(self,expo,coef):
		if expo in self.expo:
			self.expo[expo] = coef
		else:
			self.expo.update({expo:coef})

                                                      
	def __add__(poly1,poly2):                                       
		p1 = poly1.expo
		p2 = poly2.expo
		return { k : p1.get(k,0) + p2.get(k,0) for k in set(p1) | set(p2)}
                          
                          
                        
                        
                                                                  
                   
           

	def __radd__(poly1,poly2):                                          
		p1 = poly1.expo
		p2 = poly2.expo
		return { k : p1.get(k,0) + p2.get(k,0) for k in set(p1) | set(p2)}

	def __sub__(poly1,poly2):
		p1 = poly1.expo
		p2 = poly2.expo
		return { k : p1.get(k,0) - p2.get(k,0) for k in set(p1) | set(p2)}

                             

                                              
	def __mul__(poly1,poly2):
		p1 = poly1.expo
		p2 = poly2.expo
		prod = {}
		for k1 in set(p1):
			for k2 in set(p2):
				if k1+k2 in prod:
					prod[k1+k2] += p1.get(k1) * p2.get(k2)
				else:
					prod[k1+k2] = p1.get(k1) * p2.get(k2)
		return prod

                            

                                              
	def __eq__(poly1,poly2):
		p1 = poly1.expo
		p2 = poly2.expo
		if len(p1) != len(p2):
			return False
		else:
			for key in p1:
				if p1[key] != p2[key]:
					diff = False
				else:
					diff = True
			return diff

	def eval(self,base):
		val = 0
		for expo,coef in self.expo.items():
			val += coef * base ** expo
		return val

                                              
                                              
	def deriv(self):
		deri = {}
		for expo,coef in self.expo.items():
			deri.update({expo-1,coef*expo})
		return deri

def main():
    q = Polynomial([4.4, -5.1, 1.4])
    p = Polynomial([1, 5, 2])
    r = Polynomial([3,-2,4])
                
                   
    print(r*p)


if __name__=="__main__":
	main()