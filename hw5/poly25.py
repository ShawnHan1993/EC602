                                         
                                      
                                        
                                     

class Polynomial():
	def __init__(self,ipoly=[]):
		self.poly = dict((len(ipoly) - key - 1,ipoly[key]) for key in range(len(ipoly)))
	def generic_sum(self,rpoly_obj,sub_flag):
		res = Polynomial()
		res.poly = self.poly.copy()
		rpoly_obj.poly.update({key : ((-1)**sub_flag * rpoly_obj.poly[key]) for key in rpoly_obj.poly})
		for key in rpoly_obj.poly:
			if key not in self.poly:
				res.poly[key] = rpoly_obj.poly[key]
				continue
			res.poly[key] += rpoly_obj.poly[key]
		return res
	def __add__(self,rpoly_obj):
		return self.generic_sum(rpoly_obj,0)
	def __sub__(self,rpoly_obj):
		return self.generic_sum(rpoly_obj,1)
	def __mul__(self,rpoly_obj):
		res = Polynomial()
		temp = Polynomial()
		for key1 in self.poly:
			temp.poly = dict()
			for key2 in rpoly_obj.poly:
				temp.poly[key1 + key2] = self.poly[key1] * rpoly_obj.poly[key2]
			res += temp
		return res
	def __eq__(self,rpoly_obj):
		if len(self.poly) != len(rpoly_obj.poly):
			return False
		for key in self.poly:
			if (key not in rpoly_obj.poly) or (self.poly[key] != rpoly_obj.poly[key]):
				return False
		return True
	def eval(self,val):
		res = 0
		for key in self.poly:
			res += self.poly[key] * val**key
		return res
	def __setitem__(self,key,item):
		self.poly[key] = item
	def __getitem__(self,key):
		return self.poly[key]
	def deriv(self):
		for key in self.poly:
			res[key - 1] = key * self.poly[key]
		return res
	def disp(self):
		print(self.poly)
