                                


class Polynomial():
    def __init__(self,List = None):
        self.coeffs = List
        self.variable = 'x'
        
    def __str__(self):
        thestr = "0"
        var = self.variable
        coeffs = self.coeffs
        n = len(coeffs)-1
        for k in range(len(coeffs)):
            if type(coeffs[k]) != complex:
                coefstr = coeffs[k]
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
        c = self.coeffs
        d = poly.coeffs
        M = len(c) -1
        N = len(d) -1
        for i in range(0,M+1):
            for j in range(0,N+1):
                result_coeff[i+j] = c[i]*d[j]
                
        return Polynomial(result_coeff)    
