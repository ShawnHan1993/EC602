                           
class Polynomial():


	def __init__(self,s):
		self.d = { }
		for i in range(len(s)):
			if s[i] != 0:
				self.d[len(s)-i-1] = s[i]
        



	def __str__(self):
		s = ""
		for i in self.d:
			if self.d[i] != 0:
				s = s + "+" + str(self.d[i]) + "x^" + str(i)
   
		s = s[1:]
		return s 
	def __setitem__(self, key, item):
  
        	self.d[key] = item   
  


	def __getitem__(self,key):
		if key in self.d:
			return self.d[value]
		else:
			return 0 
 
	def __add__(self,value):
		for i in value.d:
			if i in self.d: 
            			self.d[i] += value.d[i]
			else:
				self.d[i] = value.d[i]
		return self
 
	def __sub__(self,value):
		for i in value.d:
			if i in self.d: 
            			self.d[i] = self.d[i] - value.d[i]
			else:
				self.d[i] = -value.d[i]
		return self
 
	def __mul__(self,value):
		for i in value.d:
			if i in self.d:  
            			self.d[i] = self.d[i]*value.d[i]
			else:
				self.d[i] = 0
   
		return self
 
	def __radd__(self,value):
		for i in self.d:
			if i in value.d: 
            			value.d[i] += self.d[i]
			else:
				value.d[i] = self.d[i]
		return self
 
	def __rmul__(self,value):
		for i in self.d:
			if i in value.d: 
            			value.d[i] = value.d[i]*self.d[i]
			else:
				value.d[i] = self.d[i]
		return self
 
 
	def deriv(self):
		s = ""
		for i in self.d:
			if self.d[i] != 0:
				s = s + "+" + str(self.d[i]*(i-1)) + "x^" + str(i-1)

   
		s = s[2:]
		return s  

	def __eq__(self,value):
		for i in value.d:
			if i in self.d: 
            			self.d[i] == value.d[i]
		for i in self.d:
			if i in value.d: 
            			value.d[i] == self.d[i] 
def main():

	x = Polynomial([2,3,4])
	x[20] = 10
	print(x)    
	y = Polynomial([3,5,6])
	print(y)
	print(x+y)
	print(x-y)
	print(x*y)
	print(x.deriv())
if __name__ == '__main__':
    main()