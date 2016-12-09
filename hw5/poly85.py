                             
                                  

class Polynomial(object):

      def __init__(self, coefficients):
         self.co=coefficients
         self.degree=len(coefficients) - 1

      def __str__(self):
         x = ''
         d = len(self.co)    
         for i in range(d):      
             if self.co[i] != 0:
                x += ' + %g*x^%d' % (self.co[i],d-i-1)  
         x = x.replace('+ -', '- ')
         x = x.replace('x^0', '1')
         x = x.replace(' *1', ' ')
         x = x.replace('x^1 ', 'x ')
         return x
        
      def __add__(self,other):
          co1 = self.co
          co2 = other.co
          if len(co1) > len(co2):
              co2 = co2 + [0]*(len(co1)-len(co2))
              y=[co1[i] + co2[i] for i in range(len(co2))]
          if len(co2) > len(co1):
              co1 = co1 + [0]*(len(co2)-len(co1))
              y=[co1[i] + co2[i] for i in range(len(co1))]
          if len(co1) == len(co2):
              y=[co1[i] + co2[i] for i in range(len(co1))]
          return Polynomial(y)

      def __sub__(self,other):
          cof1 = self.co
          cof2 = other.co
          if len(cof1) > len(cof2):
             cof2 = cof2 + [0]*(len(cof2)-len(cof1))
             z=[cof1[i] - cof2[i] for i in range(len(cof1))]
          if len(cof2) > len(cof1):
              cof1 = cof1 + [0]*(len(cof2)-len(cof1))
              z=[cof2[i] - cof1[i] for i in range(len(cof2))]
          if len(cof1) == len(cof2):
              z=[cof1[i] - cof2[i] for i in range(len(cof1))]
          return Polynomial(z)
      
      def __mul__(self, other):
         
        n = self.degree + other.degree + 1     
        prod = [0]*(n+1) 
        for i in range(0, self.degree + 1):
            for j in range(0, other.degree + 1):
                prod[i+j] = prod[i+j] + self.co[i] * other.co[j]
        return Polynomial(prod)
      def eval(self: list,e: float) -> float:
          coef = self.co
          deg = len(coef)
          sum = 0.0
          for i in range(len(coef)):
            sum = sum + (coef[i]*(e**(deg-1-i)))          
          return sum
  
      def __eq__(self,other):
          coef1 = self.co
          coef2 = other.co
          if len(coef1) == len(coef2):
             for i in range(len(coef1)):
                 if coef1[i] == coef2[i]:
                    return 1
                 else:
                    return 0
          else:
              return 0
      


                          

                             
              

                             
                              
               
              
               
                
                   
                
                 
                     
           
                    
    
 
    
    
    
    
