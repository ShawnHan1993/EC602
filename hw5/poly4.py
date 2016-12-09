                                 
                             
                                    
                                 
class Polynomial():

    def __init__(self, poly=[]):
        self.polynomial = poly

    def __add__(self,addend):
        resultList = otherList = []
        if len(self.polynomial) > len(addend.polynomial):
            resultList = self.polynomial
            otherList = addend.polynomial
        else:
            resultList = addend.polynomial
            otherList = self.polynomial
        for i in range(len(otherList)):
            resultList[-1-i] += otherList[-1-i]
        return Polynomial(resultList)

    def __sub__(self, subtrahend):
        resultList = []
        selfLength = len(self.polynomial)
        subLength = len(subtrahend.polynomial)
        if selfLength >= subLength:
            resultList = self.polynomial
            for i in range(subLength):
                resultList[-1-i] = self.polynomial[-1-i] - subtrahend.polynomial[-1-i]
        else:
            resultList = subtrahend.polynomial
            for i in range(selfLength):
                resultList[-1-i] = self.polynomial[-1-i] - subtrahend.polynomial[-1-i]
            for j in range(0,subLength-selfLength):
                resultList[j] = -subtrahend.polynomial[j]
        return Polynomial(resultList)

    def __mul__(self, multiplier):
        resultList = []
        left = self.polynomial
        right = multiplier.polynomial
        for ii in range(len(left)+len(right)-1):
            resultList.append(0)
        for i in range(len(left)):
            for j in range(len(right)):
                resultList[i+j] += left[i] * right[j]
        return Polynomial(resultList)

    def __eq__(self, another):
        eq1 = self.polynomial
        eq2 = another.polynomial
        equal = True
        if len(eq1) == len(eq2):
            for i in range(len(eq1)):
                if eq1[i] != eq2[i]:
                    equal = False
                    break
        else:
            equal = False
        return equal

    def eval(self, value):
        result = 0
        polyList = self.polynomial
        length = len(polyList)
        for i in range(length):
            result += polyList[i] * (value ** (length-1-i))
        return result

    def __str__(self):
        length = len(self.polynomial)
        returnString = ""
        if length == 0:
            returnString = "0"
        else:
            for i in range(length):
                if isinstance(self.polynomial[i], complex):
                    if self.polynomial[i].real >= 0:
                                                                                                              
                        returnString = returnString + str(self.polynomial[i]) + ' '
                    else:
                                                                                                               
                        returnString = returnString + '-' + str(-self.polynomial[i]) + ' '
                else:
                    if self.polynomial[i] >= 0:
                                                                                                              
                        returnString = returnString + str(self.polynomial[i]) + ' '
                    else:
                                                                                                               
                        returnString = returnString + '-' + str(-self.polynomial[i]) + ' '
            if returnString[0] == '+':
                returnString = returnString[1::]
        return returnString

    def __repr__(self):
        return str(self)

def main():
    pp = Polynomial([1, -3.5, 1+2.5j, 2-3j])
    qq = Polynomial([2.5, -1.5, 1+2.2j])
    rr = Polynomial([2.5, -1.5, 1+2.2j])
    print(qq.eval(2))


if __name__ == '__main__':
    main()
