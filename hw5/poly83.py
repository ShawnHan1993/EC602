                                         
class Polynomial():
	def __init__(self,poly = [0]):
		self.poly = list(poly)
                                   
		self.poly.reverse()
		self.poly = dict(enumerate(self.poly))
		self.poly = {i:self.poly[i] for i in self.poly if self.poly[i] != 0}

	def __str__(self):
		s = ""
		for i in reversed(sorted(self.poly)):
			s += str(self.poly[i]) + "x^(" + str(i) + ") + "
		return s

	def __repr__(self):
		s = ""
		for i in self.poly:
			s += str(self.poly[i]) + "x^(" + str(i) + ") + "
		return s

	def __add__(self , y):
		sum1 = Polynomial()
		for i in self.poly:
			if(i in y.poly):
				sum1.poly.update({i:self.poly[i] + y.poly[i]})
			else:
				sum1.poly.update({i:self.poly[i]})
		for i in y.poly:
			if not(i in self.poly):
				sum1.poly.update({i:y.poly[i]})
		return sum1 

	def __sub__(self , y):
		sum1 = Polynomial()
		for i in self.poly:
			if(i in y.poly):
				sum1.poly.update({i:self.poly[i] - y.poly[i]})
			else:
				sum1.poly.update({i:self.poly[i]})
		for i in y.poly:
			if not(i in self.poly):
				sum1.poly.update({i:-y.poly[i]})
  
		return sum1

	def __mul__(self, y):
		mul1 = Polynomial()
		if(len(self.poly)>len(y.poly)):
			for i in y.poly:
				for j in self.poly:
					if((i + j) in mul1.poly):
						mul1.poly[i+j] += (self.poly[j] * y.poly[i])
					else:
						mul1.poly[i+j] = (self.poly[j] * y.poly[i])
		else:
			for i in self.poly:
				for j in y.poly:
					if((i + j) in mul1.poly):
						mul1.poly[i+j] += (self.poly[i] * y.poly[j])
					else:
						mul1.poly[i+j] = (self.poly[i] * y.poly[j])

		return mul1

	def deriv(self):
		derivative = Polynomial()
		for i in self.poly:
			if(i!= 0 ):
				derivative.poly.update({i-1:self.poly[i]*i})
		return derivative

	def __setitem__(self, k, v):
		if(v != 0):
			self.poly.update({k:v})

	def __getitem__(self, k):
		if k in self.poly:
			return self.poly[k]
		else:
			return 0

	def __eq__(self, y):
			if(len(self.poly) == len(y.poly)):
				for i in self.poly:
					if (i in y.poly):
						if(self.poly[i] != y.poly[i]):
							return False
					else:
						return False
				return True
			else:
				return False
	def eval(self, value):
		result = 0
		for i in self.poly:
			result += self.poly[i]*(value**i)
		return result
