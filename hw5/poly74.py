                                  


class Element():
        
        def __init__(self, coefficient=complex(0,0), index=0):        
            self.coefficient = coefficient;
            self.index = index
            
            
class Polynomial():

                                                                                              
                                                                                              
    
        
    def __init__(self,sequence=[complex(0,0)]):
        count = 0
        position = 0
        sequenceLength = len(sequence)
        elementList = []
        while count < sequenceLength:
            
            index = sequenceLength - (count + 1)
            
            if complex(sequence[count]) != complex(0,0):
                elementList.append(Element(complex(sequence[count]), index))
                position += 1
                
            count += 1
            
        self.elementList = elementList


    def __setitem__(self, key, value): 
        keyFound = False
        for selfElement in self.elementList:
            if selfElement.index == key: 
                selfElement.coefficient = complex(value)
                keyFound = True
                break
        
        if keyFound == False:
            self.elementList.append(Element(complex(value), key))


    def __getitem__(self, key):
        for selfElement in self.elementList:
            if selfElement.index == key: 
                return selfElement.coefficient
        
        return "Element not found"

    def copy(value):
        poly = Polynomial()
        for valueElement in value.elementList:
            poly.elementList.append(Element(valueElement.coefficient,valueElement.index))
            
        return poly
        
    def complementCopy(value):
        poly = Polynomial()
        for valueElement in value.elementList:
            poly.elementList.append(Element(complex(-1,0) * complex(valueElement.coefficient),valueElement.index))
            
        return poly
        
        
    def __add__(self,value):
        sumPoly = Polynomial.copy(self)
            
        for valueElement in value.elementList:
            indexAvailableInBoth = False
            for sumPolyElement in sumPoly.elementList:
                
                if sumPolyElement.index == valueElement.index:
                    sumPolyElement.coefficient += valueElement.coefficient
                    indexAvailableInBoth = True
                    break
            
            if indexAvailableInBoth == False: 
                sumPoly.elementList.append(valueElement)
            
        return sumPoly
        
        
    def __radd__(self,value):
        sumPoly = Polynomial.copy(self)
            
        for valueElement in value.elementList:
            indexAvailableInBoth = False
            for sumPolyElement in sumPoly.elementList:
                
                if sumPolyElement.index == valueElement.index:
                    sumPolyElement.coefficient += complex(valueElement.coefficient)
                    indexAvailableInBoth = True
                    break
            
            if indexAvailableInBoth == False: 
                sumPoly.elementList.append(valueElement)
            
        return sumPoly
        
        
    def __sub__(self,value):
        return (self + Polynomial.complementCopy(value))
        
        
    def __rsub__(self,value):
        return (self + Polynomial.complementCopy(value))
        
        
                             
        
        
    def __eq__(self, other):
        for selfElement in self.elementList:
            equal = False
            for otherElement in other.elementList:
                if selfElement.index == otherElement.index:
                    if selfElement.coefficient == otherElement.coefficient:
                        equal = True
                        break
            
            if equal == False:
                return False
        
        return True


    def eval(self, value):
        result = complex(0,0)
        for selfElement in self.elementList:
            result += selfElement.coefficient*pow(complex(value), selfElement.index)
        return result
        
        
    def deriv(self):
        poly = Polynomial()
        for selfElement in self.elementList:
            if selfElement.index != 0: 
                poly.elementList.append(Element(complex(selfElement.index,0) * complex(selfElement.coefficient),(selfElement.index - 1)))

        return poly
        
        
    def __str__(self):
        
        polyString = "Poly="
        for selfElement in self.elementList:
            polyString += "(Co-efficient=" + str(selfElement.coefficient) + ", Index=" + str(selfElement.index) + "), "
            
        if(len(polyString) > 7):
            return polyString[:len(polyString) - 2]
            
        return polyString
            

    def __repr__(self):
        return str(self)
                    
                

def readInput(s):
    num = s.split()
    numList = []
    for n in num:
        numList.append(complex(n))
        
    return Polynomial(numList)
    
    
def main():
                              
                                     
    
                                    
                                     
    
    polynomial1 = Polynomial([4,3.5,6])
    polynomial2 = Polynomial([2.2,1.8,5.9])
    
    polynomial1[3] = 6.1
    polynomial2[3] = 8.2
    
    polynomial1[-1] = -4.5
    polynomial2[-1] = 0.7
    
    polynomial3 = polynomial1 + polynomial2
    print(polynomial3)
    
    polynomial4 = polynomial2 - polynomial1
    print(polynomial4)
    
    print(polynomial1 == polynomial2)
    polynomial5 = Polynomial([6.1,4,3.5,6])
    polynomial5[-1] = -4.5
    print(polynomial5 == polynomial1)
    
    polynomial6 = Polynomial([1.2,3.2,5.6])
    print(polynomial6.eval(1.1))
    
    polynomial7 = Polynomial.deriv(polynomial6)
    print(polynomial7)
    

if __name__=="__main__":
	main()