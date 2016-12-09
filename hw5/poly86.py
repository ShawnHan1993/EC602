                                

class Polynomial():
  
  def __init__(self, a=[]):
  
    self.pdict = {}
    for i in range (len(a)):
      self.pdict[len(a)-1-i] = a[i]
      

  def __getitem__(self,key):
   if (key in self.pdict):
      return self.pdict[key]
   else:
      return 0

  def __setitem__(self,key,value):
    self.pdict[key] = value

  
  def __add__(self, value):

    out = Polynomial([])
    for i in (self.pdict):
      out.pdict[i] = self.pdict[i]

    for i in (value.pdict):
      try:
        out.pdict[i] += value.pdict[i]
      except:
        out.pdict[i] = value.pdict[i]

    return out

  def __sub__(self, value):
   
    out = Polynomial([])

    for i in (self.pdict):
      out.pdict[i] = self.pdict[i]

    for i in (value.pdict):
      try:
        out.pdict[i] -= value.pdict[i]
      except:
        out.pdict[i] = (-1)*(value.pdict[i])


    return out


  def __mul__(self,value):
    out = Polynomial([])

    for i in (self.pdict):
      for j in (value.pdict):
        try:
          out.pdict[i+j] += self.pdict[i] * value.pdict[j]
        except:
          out.pdict[i+j] = self.pdict[i] * value.pdict[j]

    return out

  def __eq__(self,value):

    if (len(self.pdict) > len(value.pdict)):
      for i in (self.pdict):
        if (self.pdict[i] != 0):
          if (i in (value.pdict)):
            if (value.pdict[i] != self.pdict[i]):
              return 0
          else:
           return 0
    else:          
      for i in (value.pdict):
        if (value.pdict[i] != 0):
          if (i in (self.pdict)):
            if (self.pdict[i] != value.pdict[i]):
              return 0
          else:
           return 0
          
    return 1

  
  def eval(self, value):
      
    x=0

    for i in (self.pdict):
      x += value**i*self.pdict[i]

    return x

  
  def deriv(self):
    
    out = Polynomial([])

    for i in (self.pdict):
      if (i!=0):
        out[i-1] = i*self.pdict[i]

    return out


def main():
      pass

if __name__=="__main__":
  main()
