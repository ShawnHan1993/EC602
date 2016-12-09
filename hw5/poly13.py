                                  
                                   
                                  
class Polynomial():
    def __init__(self,List):
        self.coeffs = List
        self.variable = 'x'
        self.negcoeffs = []
        
    def __str__(self):
        thestr = "0"
        the1str = ""
        var = self.variable
        coeffs = self.coeffs
        negcoeffs = self.negcoeffs
        n = len(coeffs) - 1
        for k in range(len(coeffs)):
            if type(coeffs[k]) != complex:
                coefstr = str(coeffs[k])
            elif coeffs[k].real == 0:
                coefstr = '%sj' % coeffs[k].imag
            else:
                coefstr = '(%s + %sj)' % (coeffs[k].real,coeffs[k].imag)                                  
            power = (n-k)
            if power == 0:
                if coefstr != '0':
                    newstr = '%s' % coefstr
                else:
                    if k == 0:
                        newstr = '0'
                    else:
                        newstr = ''
            elif power == 1:
                if coefstr == '0':
                    newstr = ''
                elif coefstr == 'b':
                    newstr = var
                else:
                    newstr = '%s %s' % (coefstr, var)
            else:
                if coefstr == '0':
                    newstr = ''
                elif coefstr == 'b':
                    newstr = '%s**%d' % (var, power,)
                else:
                    newstr = '%s %s**%d' % (coefstr, var, power)

            if k > 0:
                if newstr != '':
                    if newstr.startswith('-'):
                        thestr = "%s - %s" % (thestr, newstr[1:])
                    else:
                        thestr = "%s + %s" % (thestr, newstr)
            else:
                thestr = newstr
                
        for k in range(len(negcoeffs)):
            if type(negcoeffs[k]) != complex:
                coefstr = str(negcoeffs[k])
            elif negcoeffs[k].real == 0:
                coefstr = '%sj' % negcoeffs[k].imag
            else:
                coefstr = '(%s + %sj)' % (negcoeffs[k].real,negcoeffs[k].imag)                                  
            power = - k - 1
            if coefstr == '0':
                continue
            else:
                newstr = '%s %s**%d' % (coefstr, var, power)
            if newstr.startswith('-'):
                the1str = "%s - %s" % (the1str, newstr[1:])
            else:
                the1str = "%s + %s" % (the1str, newstr)

        if len(self.coeffs) > 0:    
            thestr = thestr + the1str
        else:
            thestr = the1str[3:]
        return thestr
        
    def __add__(self,poly):
        diff = len(poly.coeffs) - len(self.coeffs)
        if diff == 0:
            val = [x+y for x, y in zip(poly.coeffs, self.coeffs)]
        elif diff > 0:
            val = poly.coeffs[0:diff] + [x+y for x,y in zip(poly.coeffs[diff:],self.coeffs)]
        else:
            val = self.coeffs[0:diff] + [x+y for x,y in zip(self.coeffs[diff:],poly.coeffs)]
        return Polynomial(val)
        
    def __sub__(self,poly):
        diff = len(poly.coeffs) - len(self.coeffs)
        if diff == 0:
            val = [x-y for x, y in zip(poly.coeffs, self.coeffs)]
        elif diff > 0:
            val = poly.coeffs[0:diff] + [y-x for x,y in zip(poly.coeffs[diff:],self.coeffs)]
        else:
            val = self.coeffs[0:abs(diff)] + [y-x for y,x in zip(self.coeffs[abs(diff):],poly.coeffs)]
        return Polynomial(val)
        
    def __mul__(self,poly):
        list1 = poly.coeffs
        list2 = self.coeffs
        list3 = []
        j = 0
        n = len(list1) + len(list2) - 1
        for i in range(n):
            list3.append(0)
        while j < len(list1):
            k = 0
            while k < len(list2):
                a = n-(len(list1)-j-1)-(len(list2)-k-1)-1
                list3[a] = list3[a] + list1[j] * list2[k]
                k = k + 1
            j = j + 1
        return Polynomial(list3)
        
    def __eq__(self, poly):
        if self.coeffs != poly.coeffs:
            return False
        return True
        
    def __getitem__(self,val):
        n = len(self.coeffs)
        if val >= 0:
            return self.coeffs[n-val-1]
        else:
            return self.negcoeffs[abs(val) - 1]
    def __setitem__(self,key,val):
        if key < 0:
            n = len(self.negcoeffs)
            if n >= abs(key):
                self.negcoeffs[abs(key) - 1] = val
            else:
                for i in range(abs(key) - n - 1):
                    self.negcoeffs.append(0)
                self.negcoeffs.append(val)
        else:
            n = len(self.coeffs)
            if n - 1 >= key:
                self.coeffs[n-key-1] = val
            else:
                new_list = [val]
                for i in range(key - n):
                    new_list.append(0)
                self.coeffs = new_list + self.coeffs
        print(self.negcoeffs)
            
    def eval(self,val):
        a = 0
        i = 0
        n = len(self.coeffs)
        while i < n:
            b = self.coeffs[i] * (val ** (n - i - 1))
            i = i + 1
            a = a + b
        return a
        
    def deriv(self):
        list1 = self.coeffs[:-1]
        list2 = []
        n = len(list1)
        i = 0
        while i < n:
            a = list1[i] * (n-i)
            list2.append(a)
            i = i + 1
        return Polynomial(list2)
    
def main():
    p = Polynomial([])
    q = Polynomial([])
    q [-2] = 100
    print(q[-2])
    print(q)
    p [5] = 100
    print(p.eval(-23))
    print(p)
    print(Polynomial([1,-2,3]))
    print(Polynomial([4,-9+1j,-5.6,10,10]) * Polynomial([4,-9+1j,5.6,10]))
    print(Polynomial([4,-9+1j,5.6,10,10]) == Polynomial([4,-9+1j,5.6,10,10]))
    print(Polynomial([1,3,4,2,1]))
    print(Polynomial([1,3,4,2,1]).deriv())

if __name__=="__main__":
    main()