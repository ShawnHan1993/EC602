                                 
class Polynomial():
 pass

 def __init__(self,poly=[0]):
  self.poly = poly 
  self.coefficient = self.poly[:]
  self.power = [0]*len(self.poly)
  for i in range(0, len(self.poly)):
   self.power[i] = i
  self.power = list(reversed(self.power))
  self.coefficient = list((self.coefficient))

 def __str__(self):
  self.poly=[]
  for i in range(min(self.power),max(self.power)+1):
   success = 0
   for j in range(0, len(self.power)):
    if(i == self.power[j]):
     self.poly.append(self.coefficient[j])
     success=1
   if(success==0):
     self.poly.append(0)
  temp = list(reversed(self.poly[:]))
  return temp.__str__()

 def __add__(self, value):
  addA = self.__class__()
  if(max(self.power) > max(value.power)):
   maxP = max(self.power)
  else:
   maxP = max(value.power)
  if(min(self.power) < min(value.power)):
   minP = min(self.power)
  else:
   minP = min(value.power)
  result = [0]*(-minP+maxP+1)
  for i in range(minP, maxP+1):
   for j in range(0, len(self.power)):
    if( i==self.power[j]):
     result[i-minP] = result[i-minP] + self.coefficient[j]
   for k in range(0, len(value.power)):
    if( i==value.power[k]):
     result[i-minP] = result[i-minP] + value.coefficient[k]
  addA =list(reversed(result))
  return addA

 def __radd__(self, value):
  addA = self.__class__()
  if(max(self.power) > max(value.power)):
   maxP = max(self.power)
  else:
   maxP = max(value.power)
  if(min(self.power) < min(value.power)):
   minP = min(self.power)
  else:
   minP = min(value.power)
  result = [0]*(-minP+maxP+1)
  for i in range(minP, maxP+1):
   for j in range(0, len(self.power)):
    if( i==self.power[j]):
     result[i-minP] = result[i-minP] + self.coefficient[j]
   for k in range(0, len(value.power)):
    if( i==value.power[k]):
     result[i-minP] = result[i-minP] + value.coefficient[k]
  addA =list(reversed(result))
  return addA


 def __sub__(self, value):
  subA = self.__class__()
  if(max(self.power) > max(value.power)):
   maxP = max(self.power)
  else:
   maxP = max(value.power)
  if(min(self.power) < min(value.power)):
   minP = min(self.power)
  else:
   minP = min(value.power)
  result = [0]*(-minP+maxP+1)
  for i in range(minP, maxP+1):
   for j in range(0, len(self.power)):
    if( i==self.power[j]):
     result[i-minP] = result[i-minP] + self.coefficient[j]
   for k in range(0, len(value.power)):
    if( i==value.power[k]):
     result[i-minP] = result[i-minP] - value.coefficient[k]
  subA =list(reversed(result))
  return subA

 def __rsub__(self, value):
  subA = self.__class__()
  if(max(self.power) > max(value.power)):
   maxP = max(self.power)
  else:
   maxP = max(value.power)
  if(min(self.power) < min(value.power)):
   minP = min(self.power)
  else:
   minP = min(value.power)
  result = [0]*(-minP+maxP+1)
  for i in range(minP, maxP+1):
   for j in range(0, len(self.power)):
    if( i==self.power[j]):
     result[i-minP] = result[i-minP] + self.coefficient[j]
   for k in range(0, len(value.power)):
    if( i==value.power[k]):
     result[i-minP] = result[i-minP] - value.coefficient[k]
  subA =list(reversed(result))
  return subA

 def __mul__(self, value):
  mulA = self.__class__()
  result = [0]*(max(self.power)+max(value.power)-min(self.power)-min(value.power)+1)
  for i in range(0, len(self.power)):
   for j in range(0, len(value.power)):
    result[self.power[i]+value.power[j]] = result[self.power[i]+value.power[j]] + self.coefficient[i] * value.coefficient[j]
  mulA= list(reversed(result))  
  return mulA

 def __rmul__(self, value):
  mulA = self.__class__()
  result = [0]*(max(self.power)+max(value.power)-min(self.power)-min(value.power)+1)
  for i in range(0, len(self.power)):
   for j in range(0, len(value.power)):
    result[self.power[i]+value.power[j]] = result[self.power[i]+value.power[j]] + self.coefficient[i] * value.coefficient[j]
  mulA= list(reversed(result))  
  return mulA

 def __eq__(self, value):
  for i in range(min(self.power), max(self.power)+1):
   success = 0
   for j in range(min(value.power), max(value.power)+1):
    if(i==j):
     for k in range(0, len(self.power)):
      if(self.power[k] == i):
       iSelf = k
     for l in range(0, len(value.power)):
      if(value.power[l] == i):
       iValue = l
     temp = self.coefficient[k] - value.coefficient[l]
     if temp != 0:
      return("False")
     else:
      success = 1
   if(success == 0):
    return("False")
  return("True")

 def eval(self, value):
  evalA = 0
  for i in range(0, len(self.power)):
   evalA = evalA + self.coefficient[i]*value**self.power[i]
  return(evalA)

 def deriv(self):
  derivA = self.__class__()
  derivA = [0]*(max(self.power)-min(self.power)+1)
  for i in range(0, len(self.power)):
   if(self.power[i] != 0):
    derivA[self.power[i]-1-(min(self.power)-1)] = self.coefficient[i]*self.power[i]
  if(min(self.power)>=0):
    derivA.pop(0)
  return(list(reversed(derivA)))

 def __getitem__(self, index):
  for i in range(0,len(self.power)):
   if(self.power[i] == index):
    return(self.coefficient[i]) 

 def __setitem__(self, index, value):
   for j in range(0,len(self.power)):
    if(self.power[j] == index):
     self.coefficient[j] = value
     break
   self.coefficient.append(value)
   self.power.append(index)


 def main():
  pass


 if __name__=="__main__":
  main()


