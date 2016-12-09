                                     

def check_expect(a,b):
	if str(a) == str(b):
		print("Test passed.")
	else:
		print("Test failed: " + str(a) + " != " + str(b))
	return

class Polynomial():
	"Polynomial([c1, c2,...,cn]) -> c1*x**(n-1) + c2*x**(n-2) + ... + cn"
                                                                         
	def __init__(self, coeffs = [0]):
		self.coeffs = []
		for i in range(0,len(coeffs)):
			if coeffs[i] != 0:
				self.coeffs.append(([coeffs[i],len(coeffs) - i - 1]))

	def __add__(self,other):
		"return self + other"
		ret = Polynomial()
		for term in self.coeffs:
			ret.coeffs.append([term[0],term[1]])

                    
		if(isinstance(other,complex)):
			ret[0] += other

                    
		elif(isinstance(other,int)):
			ret[0] += other

                  
		elif(isinstance(other,float)):
			ret[0] += other

                       
		if (isinstance(other,Polynomial)):
			for t in other.coeffs:
				ret[t[1]] = ret[t[1]] + t[0]
		return ret

                            
                         
                    

	def __sub__(self,other):
		"Return self - other"
                                            
		ret = Polynomial()
		for term in other.coeffs:
			ret.coeffs.append([term[0],term[1]])

		for term in ret.coeffs:
			term[0] = -1 * term[0]

		return self + ret

                            
                         
                    

	def __mul__(self,other):
		"Return self * other"
		ret = Polynomial()
  
		for term in self.coeffs:
			for t in other.coeffs:
				new_coeff = term[0] * t[0]
				new_power = term[1] + t[1]
				ret[new_power] = ret[new_power] + new_coeff
		return ret 
  

                            
                         
                    

	def __eq__(self,other):
		"Return self == other"
		return sorted(self.coeffs) == sorted(other.coeffs)

	def __getitem__(self, index):
		"p[n] accesses the coefficient for x^n"
                   
		for term in self.coeffs:
			if term[1] == index:
				return term[0]
                         
		return 0

	def __setitem__(self, index, value):
		"p[n] accesses the coefficient for x^n"
                   
		for term in self.coeffs:
			if term[1] == index:
				term[0] = value
				return
                                      
		self.coeffs.append([value,index])
		return 

	def __str__(self):
                     
		self.coeffs = self.coeffs
		ret = ""
		for term in self.coeffs:
			if term[0] != 0:
				if term[1] == 0:
					ret += str(term[0]) + " "
				elif term[1] == 1:
					ret += str(term[0]) + "x" + " "
				else:
					ret += str(term[0]) + "x^" + str(term[1]) + " "
		return ret

	def eval(self,value):
		"evaluate the polynomial with x=value"
		ret = 0
		for term in self.coeffs:
			ret += term[0] * value ** term[1]
		return ret

	def deriv(self):
		"return the derivative of self"
                                  
		ret = Polynomial()
		for term in self.coeffs:
			ret.coeffs.append([term[0],term[1]])

		for term in ret.coeffs:
			term[0]*=term[1]
			term[1]-= 1

		print(ret.coeffs)
		return ret

def main():
                
	a = Polynomial([0,1,2,3])
	floata = Polynomial([0.0,1.1,2.2,3.3])
	complexa = Polynomial([complex(1,1),complex(2,2),complex(3,3)])

                                              
	print("==================================================")
               
	print("TESTING __str__ and __init__")
	print(Polynomial([0,1,2,3]), end="")
	print(" should be 1x^2 2x 3")
	print(str(floata), end="")
	print(" should be 1.1x^2 2.2x 3.3")
	print(str(complexa), end="")
	print(" should be (1+1j)x^2 (2+2j)x (3+3j)")
	print("==================================================")

              
	print("TESTING __eq__")
	print(Polynomial([0,1,2,3]) == a, end="")
	print(" should be True")
	print(Polynomial([2,3]) == a, end="")
	print(" should be False")
	a = Polynomial([4,0,0])
	check_expect(a.deriv() == Polynomial([8,0]), "True")
	print("==================================================")

                   
	print("TESTING __getitem__")
	print(str(a[1]) + " should be 2")
	print("==================================================")

                   
	print("TESTING __setitem__")
	a[10] = 5
	print(str(a[10]) + " should be 5")
	print("==================================================")

               
	a = Polynomial([1])
	print("TESTING __add__")
	check_expect(a + a,2)
	a = Polynomial([1,1])
	check_expect(a + a,"2x 2 ")
	a = Polynomial([1,2,3,4])
	print(a + a, end="")
	print(" should be 2x^3 4x^2 6x 8 ")
	print(a + a, end="")
	print(" should be 2x^3 4x^2 6x 8 ")
	a = Polynomial([1,2,3,4])
	print(a + 1, end="")
	print(" should be 1x^3 2x^2 3x 5 ")
	print(a + 1.0, end="")
	print(" should be 1x^3 2x^2 3x 5.0 ")
	print(a + complex(1,1), end="")
	print(" should be 1x^3 2x^2 3x (5+j) ")
	print("==================================================")

               
	print("TESTING __sub__")
	check_expect(Polynomial([1]) - Polynomial([1]),"")
	check_expect(Polynomial([2]) - Polynomial([1]),"1 ")
	check_expect(Polynomial([1,1]) - Polynomial([1]),"1x ")
	check_expect(Polynomial([3,1]) - Polynomial([1,1]),"2x ")
	a = Polynomial()
	b = Polynomial()
	a[-1] = 1
	b[-2] = 1
	print(a)
	print(b)
	check_expect(a - b, "x^-1 -1x^-2")
	check_expect(a + b, "x^-1 x^-2")
	print("==================================================")
 
               
	print("Testing __mul__")
	check_expect(Polynomial([1]) * Polynomial([1]),"1 ")
	check_expect(Polynomial([1,0]) * Polynomial([1,0]),"1x^2 ")
	check_expect(Polynomial([1,2,3]) * Polynomial([1,2,3]),"1x^4 4x^3 10x^2 12x 9 ")
	print("==================================================")
                
	print("TESTING __eval__")
	check_expect(Polynomial([1]).eval(1),1)
	check_expect(Polynomial([2,1]).eval(1),2*1**1 + 1)
	check_expect(Polynomial([2,2,0]).eval(3),2*3**2 + 2*3**1)
	print("==================================================")

                 
	print("TESTING __deriv__")
	check_expect(Polynomial([1]).deriv(),"")
	check_expect(Polynomial([2,1]).deriv(),"2")
	a = Polynomial([4,0,0])
	check_expect(Polynomial([4,0,0]).deriv(),"8x ")
	print("==================================================")

                     
	foo = Polynomial([3.2,-7.1,1])
	foo[-2] = 4
	print(foo)

	derivative = foo.deriv()
	print(derivative)


if __name__=="__main__":
	main()
