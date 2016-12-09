                                  
                                   
class Polynomial():

	def __init__(self,value=[0]):
		self.d=value                 
		self.dict={}                       
		x=len(value)-1                 
		for i in self.d:
			if i!=0:
				self.dict[x]=i
			x-=1                                                             
   

	def __setitem__(self,key,value):
		self.dict[key]=value
  
	def __add__(self,value):
		sum={}
		sum=self.dict.copy()
		for n in sum:
			if n in value.dict:
				sum[n]=self.dict[n]+value.dict[n]
			else:
				sum[n]=self.dict[n]
		for m in value.dict:
			if m in self.dict:
				sum[m]=self.dict[m]+value.dict[m]
			else:
				sum[m]=value.dict[m]
		p=Polynomial()                               
		for i in sum:
			p[i]=sum[i]
		return p

	def __sub__(self,value):
		sub={}
		for n in self.dict:
			if n in value.dict:
				sub[n]=self.dict[n]-value.dict[n]
			else:
				sub[n]=self.dict[n]
		for m in value.dict:
			if m in self.dict:
				sub[m]=self.dict[m]-value.dict[m]
			else:
				sub[m]=-value.dict[m]
		p=Polynomial()
		for i in sub:
			p[i]=sub[i]
		return p

	def __mul__(self,value):     
		prod={}
		for n in self.dict:
			for m in value.dict:
				if m+n in prod:
					prod[m+n]=prod[m+n]+self.dict[n]*value.dict[m]
				else:
					prod[m+n]=self.dict[n]*value.dict[m]
		p=Polynomial()
		for i in prod:
			p[i]=prod[i]
		return p

	def deriv(self):
		deriv={}
		for i in self.dict:
			if i!=0:
				deriv[i-1]=i*self.dict[i]
		p=Polynomial()
		for i in deriv:
			p[i]=deriv[i]
		return p

	def eval(self,value):
		result=0
		print(self,value)
		for i in self.dict:
			result+=self.dict[i]*(value**i)
		return result

	def __getitem__(self,key):
		if (key in self.dict) == False:
			return False                                          
		else:
			return self.dict[key]

	def __eq__(self, other):
		return self.dict == other

def main():
	pass

if __name__ == '__main__':
    main()

