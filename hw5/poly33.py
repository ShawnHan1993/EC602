                                    




class Polynomial():
	"Polynomial(coeff, key(exp)) -> a polynomial array"

	def __init__(self, coeff=[]):
		exp = len(coeff) - 1 
		poly = []
		expon = []
		self.poly = poly
		self.expon = expon
		i = exp
		while i > -1:
			self.poly += [coeff[exp - i]]
			self.expon += [i]
			i -= 1 
		self.sparse()

	def list_duplicates(self, array,value):
		start_at = -1
		locs = []
		while True:
			try:
				loc = array.index(value,start_at+1) 
			except:
				break
			locs += [loc]
			start_at = loc
		return locs

	def __getitem__(self,key):
		"Get the value from the key"
		try:
			ind_self = self.expon.index(key)
			return self.poly[ind_self]
		except:
			return 0


	def __setitem__(self,key,value):
		"Set the coefficient to a specific key"
		if key in self.expon:
			ind_self = self.expon.index(key)
			self.poly[ind_self] = value
			self.sparse()
		else:
			self.expon += [key]
			self.poly += [value]
			self.sparse()

	def __len__(self):
		try:
			return len(self.poly)
		except:
			return 0


	def __add__(self,value):
		"Return self+coeff"
                                     
		for expo in value.expon:
			ind_value = value.expon.index(expo)
			if expo in self.expon:
				ind_self = self.expon.index(expo)
				self.poly[ind_self] += value.poly[ind_value]
				self.sparse()
			else: 
				self.expon += [expo]
				self.poly += [value.poly[ind_value]]
				self.sparse()
		return self

	def __sub__(self,value):
		"Return self-coeff"
		for expo in value.expon:
			ind_value = value.expon.index(expo)
			if expo in self.expon:
				ind_self = self.expon.index(expo)
				self.poly[ind_self] -= value.poly[ind_value]
			else: 
				self.expon += [expo]
				self.poly += [-(value.poly[ind_value])]
		return self.sparse()


	def __mul__(self,value):
		"return s*v"
		exponents = []
		coefficients = []
		expon = []
		if len(value.poly) == 0:
			return self
		for expon in value.expon:
			exponents += [x+expon for x in self.expon]
		set_exp = set(exponents)
		for coeff in value.poly:
			coefficients += [y*coeff for y in self.poly]
		for exp in set_exp:
			l_of_duplicates = self.list_duplicates(exponents,exp)
			poly = []
			for index in l_of_duplicates:
				poly += [coefficients[index]]

			self[exp] = sum(poly)
		return self
       

	def __eq__(self,value):
		"return if values are equal"
                                           
                                         
		if set(self.expon)== set(value.expon):
			for expon in self.expon:
				self_index = self.expon.index(expon)
				value_index = value.expon.index(expon)
				if self.poly[self_index] != value.poly[value_index]:
					return False 
			return True
		else:
			return False
 

	def eval(self, value):
		"return evalutated polynomial"
		total = 0
		for expon in self.expon:
			ind_self = self.expon.index(expon)
			total += (value**expon)*self.poly[ind_self]
		return total

	def deriv(self):
		"return the derivative of self"
		for expon in self.expon: 
			ind_self = self.expon.index(expon)
			self.poly[ind_self] = self.poly[ind_self]*expon
		self.expon[:] = [expon - 1 for expon in self.expon]
		self.sparse()
		return self


	def sparse(self):
		"return a sparse version of the polynomial"
		for coeff in self.poly:
			if coeff == 0:
				ind_self_c = self.poly.index(coeff)
				len_self = len(self.poly)
				self.poly = self.poly[0:ind_self_c] + self.poly[ind_self_c+1:len_self]
				self.expon = self.expon[0:ind_self_c] + self.expon[ind_self_c+1:len_self]
		return self

def main():
	pass

if __name__=="__main__":
	main()

