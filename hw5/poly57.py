                                   


class Polynomial:
 
	def __init__(self,a=None):
		self.d ={}
		self.a = a
		if( a != None):
			self.d = dict([len(self.a)-i-1,a[i]] for i in range (0,len(self.a)))
 



	def __str__(self):
		s = ""
		j=0
		for k1,v1 in reversed(sorted(self.d.items())):
			if (v1 != 0):
    
    
				if(v1 < 0):
					s += str(v1) + "X" + "^" + str(k1) 
				else:
					if(j == 0):
     
						s +=  str(v1) + "X" + "^" + str(k1)
						j = 1
					else:
						if(k1 == 0):
							s += "+" + str(v1) 
						else:
							s += "+" + str(v1) + "X" + "^" + str(k1)
		return s

 

	def __setitem__(self,key,value):
		self.d[key] = value

	def __getitem__(self,key):
		list1 = list(self.d.keys())
		if key in list1:
				return self.d[key]
		else:
				return 0
     
 

	def __add__(self,other):
		add=Polynomial([])
		for k1,v1 in self.d.items():
            		if(not(k1 in add.d.keys())):
                		add.d[k1]=v1
		for k2,v2 in other.d.items():
			if(not(k2 in add.d.keys())):
               			add.d[k2]=v2
			else:
                		add.d[k2]=add.d[k2]+v2
		return add
  
	def __sub__(self,other):
		sub=Polynomial([])
		for k1,v1 in self.d.items():
            		if(not(k1 in sub.d.keys())):
                		sub.d[k1]=v1
		for k2,v2 in other.d.items():
			if(k2 in sub.d.keys()):
               			sub.d[k2]=sub.d[k2]-v2 
   
		return sub


	def __mul__(self,other):
       
        	mul=Polynomial([])
        	for k4,v4 in self.d.items():
            		for k5,v5 in other.d.items():
                		if(not((k4+k5) in mul.d.keys())):
                    			mul[k4+k5]=v4*v5
                		else:
                    			mul[k4+k5]=mul[k4+k5]+(v4*v5)
        	return mul

	def deriv(self):

        	deriv=Polynomial([])
        	for key,value in self.d.items():
            		if(key!=0):
                		deriv.d[key-1]=key*value
        
        	return deriv

	def __eq__(self,other):
        	if((len(self.d.items()^other.d.items()))==0):
            		return True
        	else:
            		return False 

	def eval(self,number):
		result=0.0
		list1 = list(self.d.keys())
		list2 = list(self.d.values())
		for i in range(0, len(list1)):
			result += list2[i] * number**list1[i]
   
		return result

  
  
def main():
	x = Polynomial([4,-5,2,1,0])
	print(x)
	q = Polynomial([1,2,1])
	y= Polynomial()
	y[2] = 5
 
 
 
	print( y[5])

 
 
 

if __name__ == '__main__':
    main()
