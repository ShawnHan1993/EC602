                                 
class Polynomial():

 def __init__(self,poly=[0]):
  self.dict = {}
  for i in range (0, len(poly)):
   self.dict[(len(poly)-1-i)] = poly[i]

 def __getitem__(self, index):
  if index in (self.dict):
   return(self.dict[index])
  else:
   return(0)

 def __setitem__(self, index, value):
  self.dict[index] = value

 def __add__(self, value):
  temp = Polynomial([])
  for i in (self.dict):
   temp.dict[i] = self.dict[i]
  for i in (value.dict):
   try:
    temp[i] += value.dict[i]
   except:
    temp[i] = value.dict[i]
  return(temp) 

 def __radd__(self, value):
  temp = Polynomial([])
  for i in (self.dict):
   temp.dict[i] = self.dict[i]
  for i in (value.dict):
   try:
    temp[i] += value.dict[i]
   except:
    temp[i] = value.dict[i]
  return(temp) 

 def __sub__(self, value):
  temp = Polynomial([])
  for i in (self.dict):
   temp.dict[i] = self.dict[i]
  for i in (value.dict):
   try:
    temp[i] -= value.dict[i]
   except:
    temp[i] = -1*value.dict[i]
  return(temp)
 
 def __rsub__(self, value):
  temp = Polynomial([])
  for i in (self.dict):
   temp.dict[i] = self.dict[i]
  for i in (value.dict):
   try:
    temp[i] -= value.dict[i]
   except:
    temp[i] = -1*value.dict[i]
  return(temp)

 def __mul__(self, value):
  temp = Polynomial([])
  for i in (self.dict):
   for j in (value.dict):
    try:
     temp[i+j] += self.dict[i] * value.dict[j]
    except:
     temp[i+j] = self.dict[i] * value.dict[j]
  return(temp)

 def __rmul__(self, value):
  temp = Polynomial([])
  for i in (self.dict):
   for j in (value.dict):
    try:
     temp[i+j] += self.dict[i] * value.dict[j]
    except:
     temp[i+j] = self.dict[i] * value.dict[j]
  return(temp)

 def eval(self, value):
  temp = 0
  for i in (self.dict):
   temp += self.dict[i]*value**i
  return(temp)
 
 def deriv(self):
  temp = Polynomial([])
  for i in (self.dict):
   temp[i-1] = self.dict[i]*i
  return(temp)
  
 def __eq__(self, value):
  if (len(self.dict) > len(value.dict)):
   for i in (self.dict):
    if (self.dict[i] != 0):
     if (i in (value.dict)):
      if (value.dict[i] != self.dict[i]):
       return 0   
    else:
     return 0
  else:          
   for i in (value.dict):
    if (value.dict[i] != 0):
     if (i in (self.dict)):
      if (self.dict[i] != value.dict[i]):
       return 0
     else:
      return 0      
  return 1
    

def main():
  pass

if __name__=="__main__":
  main()



