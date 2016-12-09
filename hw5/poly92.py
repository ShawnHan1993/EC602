                                 
                             
                                    
                                 
class Polynomial():

    def __init__(self, poly=[]):
        self.polynomial = poly
        self.negPolynomial = []

    def __add__(self, addend):
        posResultList = posOtherList = []
                                                  
        if len(self.polynomial) >= len(addend.polynomial):
            posResultList = self.polynomial[:]
            posOtherList = addend.polynomial[:]
        else:
            posResultList = addend.polynomial[:]
            posOtherList = self.polynomial[:]
        for i in range(len(posOtherList)):
            if posOtherList[-1-i] == 0:
                continue
            posResultList[-1-i] += posOtherList[-1-i]

        negResultList = negOtherList = []
        if len(self.negPolynomial) >= len(addend.negPolynomial):
            negResultList = self.negPolynomial[:]
            negOtherList = addend.negPolynomial[:]
        else:
            negResultList = addend.negPolynomial[:]
            negOtherList = self.negPolynomial[:]
        for i in range(len(negOtherList)):
            if negOtherList[i] == 0:
                continue
            negResultList[i] += negOtherList[i]

        returnResult = Polynomial(posResultList)
        returnResult.negPolynomial = negResultList
        return returnResult

    def __sub__(self, subtrahend):
        posResultList = []
        posSelfLength = len(self.polynomial)
        posSubLength = len(subtrahend.polynomial)
                                         
        if posSelfLength >= posSubLength:
            posResultList = self.polynomial[:]
            for i in range(posSubLength):
                if subtrahend.polynomial[-1-i] == 0:
                    continue
                posResultList[-1-i] = self.polynomial[-1-i] - subtrahend.polynomial[-1-i]
                                          
        else:
            posResultList = subtrahend.polynomial[:]
            for i in range(posSelfLength):
                posResultList[-1-i] = self.polynomial[-1-i] - subtrahend.polynomial[-1-i]
            for j in range(0,posSubLength-posSelfLength):
                if subtrahend.polynomial[j] == 0:
                    continue
                posResultList[j] = -subtrahend.polynomial[j]

        negResultList = []
        negSelfLength = len(self.negPolynomial)
        negSubLength = len(subtrahend.negPolynomial)
                                         
        if negSelfLength >= negSubLength:
            negResultList = self.negPolynomial[:]
            for i in range(negSubLength):
                if subtrahend.negPolynomial[i] == 0:
                    continue
                negResultList[i] = self.negPolynomial[i] - subtrahend.negPolynomial[i]
                                          
        else:
            negResultList = subtrahend.negPolynomial[:]
            for i in range(negSelfLength):
                negResultList[i] = self.negPolynomial[i] - subtrahend.negPolynomial[i]
            for j in range(negSelfLength,negSubLength):
                if subtrahend.negPolynomial[j] == 0:
                    continue
                negResultList[j] = -subtrahend.negPolynomial[j]

        returnResult = Polynomial(posResultList)
        returnResult.negPolynomial = negResultList
        return returnResult

    def __mul__(self, multiplier):
        posLeft = self.polynomial[:]
        posRight = multiplier.polynomial[:]
        negLeft = self.negPolynomial[:]
        negRight = multiplier.negPolynomial[:]
        left = posLeft + negLeft
        right = posRight + negRight
        resultList = [0] * (len(left)+len(right)-1)

        nzLeft = []
        nzRight = []
        for i in range(len(left)):
            if left[i] != 0:
                nzLeft.append(i)
        for j in range(len(right)):
            if right[j] != 0:
                nzRight.append(j)
        for ii in range(len(nzLeft)):
            for jj in range(len(nzRight)):
                resultList[nzLeft[ii]+nzRight[jj]] += left[nzLeft[ii]] * right[nzRight[jj]]

                                    
                              
                          
                                         
                                   
                              
                                                       

        posResult = resultList[0:(len(posLeft)+len(posRight)-1)]
        negResult = resultList[(len(posLeft)+len(posRight)-1):]
        result = Polynomial(posResult)
        result.negPolynomial = negResult
        return result

    def __eq__(self, another):
        pos1 = self.polynomial[:]
        pos2 = another.polynomial[:]
        neg1 = self.negPolynomial[:]
        neg2 = another.negPolynomial[:]
                                              
        pi1 = 0
        while pi1 < len(pos1):
            if pos1[pi1] == 0:
                pos1.pop(pi1)
                pi1 = 0
            else:
                break
        pi2 = 0
        while pi2 < len(pos2):
            if pos2[pi2] == 0:
                pos2.pop(pi2)
                pi2 = 0
            else:
                break
                                                 
        while len(neg1) != 0:
            if neg1[-1] == 0:
                neg1.pop()
            else:
                break
        while len(neg2) != 0:
            if neg2[-1] == 0:
                neg2.pop
            else:
                break
        equal = True
        if len(pos1) == len(pos2) and len(neg1) == len(neg2):
            for i in range(len(pos1)):
                if pos1[i] != pos2[i]:
                    equal = False
                    break
            if equal == True:
                for j in range(len(neg1)):
                    if neg1[j] != neg2[j]:
                        equal = False
                        break
        else:
            equal = False
        return equal

    def eval(self, value):
        result = 0
        posList = self.polynomial[:]
        negList = self.negPolynomial[:]
        posLength = len(posList)
        negLength = len(negList)
        for i in range(posLength):
            if posList[i] == 0:
                continue
            result += posList[i] * (value ** (posLength-1-i))
        for j in range(negLength):
            if negList[j] == 0:
                continue
            result += negList[j] * (value ** (-1-j))
        return result

    def __getitem__(self, index):
        if index >= 0:
            if index >= len(self.polynomial):
                return 0
            else:
                realIndex = len(self.polynomial)-1-index
                return self.polynomial[realIndex]
        else:
            if -index > len(self.negPolynomial):
                return 0
            else:
                realIndex = -index-1
                return self.negPolynomial[realIndex]

    def __setitem__(self, index, value):
        if index >= 0:
            if index > len(self.polynomial)-1:
                for i in range(index+1-len(self.polynomial)):
                    self.polynomial.insert(i,0)
            realIndex = len(self.polynomial)-1-index
            self.polynomial[realIndex] = value
        else:
            if len(self.negPolynomial) < -index:
                for i in range(-index-len(self.negPolynomial)):
                    self.negPolynomial.append(0)
            self.negPolynomial[-index-1] = value

    def deriv(self):
        posList = self.polynomial[:]
        negList = self.negPolynomial[:]
        posResult = []
        negResult = []
        for i in range(len(posList)-1):
            if posList[i] == 0:
                posResult.append(0)
            else:
                posResult.append(posList[i] * (len(posList)-1-i))
        for j in range(len(negList)):
            if negList[j] == 0:
                negResult.append(0)
            else:
                negResult.append(negList[j] * (-1-j))
        if len(negResult) != 0:
            negResult.insert(0,0)

        returnResult = Polynomial(posResult)
        returnResult.negPolynomial = negResult
        return returnResult

    def __str__(self):
        length = len(self.polynomial)
        negLength = len(self.negPolynomial)
        returnString = ""
        if (length == 0) and (negLength == 0):
            returnString = "0"
        else:
            for i in range(length):
                if isinstance(self.polynomial[i], complex):
                    if self.polynomial[i].real > 0:
                        returnString = returnString + '+' + str(self.polynomial[i]) + 'X^' + str(length-1-i)
                                                                                     
                    elif self.polynomial[i].real < 0:
                        returnString = returnString + '-' + str(-self.polynomial[i]) + 'X^' + str(length-1-i)
                                                                                            
                    else:
                        if self.polynomial[i].imag > 0:
                            returnString = returnString + '+' + str(self.polynomial[i].imag) + 'jX^' + str(length-1-i)
                        else:
                            returnString = returnString + '-' + str(-self.polynomial[i].imag) + 'jX^' + str(length-1-i)
                else:
                    if self.polynomial[i] > 0:
                        returnString = returnString + '+' + str(self.polynomial[i]) + 'X^' + str(length-1-i)
                                                                                     
                    elif self.polynomial[i] < 0:
                        returnString = returnString + '-' + str(-self.polynomial[i]) + 'X^' + str(length-1-i)
                                                                                            
            for j in range(negLength):
                if isinstance(self.negPolynomial[j], complex):
                    if self.negPolynomial[j].real > 0:
                        returnString = returnString + '+' + str(self.negPolynomial[j]) + 'X^' + str(-1-j)
                                                                                     
                    elif self.negPolynomial[j].real < 0:
                        returnString = returnString + '-' + str(-self.negPolynomial[j]) + 'X^' + str(-1-j)
                                                                                            
                    else:
                        if self.negPolynomial[j].imag > 0:
                            returnString = returnString + '+' + str(self.negPolynomial[j].imag) + 'jX^' + str(-1-j)
                        else:
                            returnString = returnString + '-' + str(-self.negPolynomial[j].imag) + 'jX^' + str(-1-j)
                else:
                    if self.negPolynomial[j] > 0:
                        returnString = returnString + '+' + str(self.negPolynomial[j]) + 'X^' + str(-1-j)
                                                                                        
                    elif self.negPolynomial[j] < 0:
                        returnString = returnString + '-' + str(-self.negPolynomial[j]) + 'X^' + str(-1-j)
                                                                                               
            if returnString[0] == '+':
                returnString = returnString[1::]
        return returnString

    def __repr__(self):
        return str(self)

def main():
    aa = Polynomial([])
    bb = Polynomial([])
    aa[20000] = 2
    aa[100000] =10
    bb[180000] = 15
    bb[3000] = 12
    aa*bb
               
               
                  

                                                                  
                                                
                                           
                                           
                                                             
                                                             
                                                             
                                                               
                                                                                              
                                                                                              
                                        
                                       
                                                  
                           
                
                                                    
                                     
                                                              
     
                                                               
                                                
                                           
                                           
                
                   
                                                                        
                                                                        
                                                                         
                                                                           
                                                                                                                                      
                                                                                                                                      
                                        
                                        
                                                 
                            
                 
                                                               
                                       
                                                                          

if __name__ == '__main__':
    main()
