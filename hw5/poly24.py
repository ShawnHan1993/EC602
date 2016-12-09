                                 
                                   



class Polynomial(object):
    def __init__(self,numbers=[None]):
        self.coeff = numbers
        self.zero= 0

    def __getitem__(self,index):
           return self.coeff[index]
    
    def __setitem__(self,index,value):
        if (len(self.coeff)>index>=0):
            self.coeff[index] = value
        if (index<0):
            i=0
            j=0
            for i in range (index*-1):
                self.coeff[:i]=self.coeff[:i+1]
            self.coeff[0] = 0
            self.coeff[0] = value
            for i in range ((index*-1)-1):
                self.coeff[i+1]=0
            self.zero=index*-1
        if(index>len(self.coeff)):
            l=len(self.coeff)
            for i in range (index):
                self.coeff[:i]=self.coeff[:i+1]
            for i in range(l):
                self.coeff[i]=self.coeff[len(self.coeff)-l+i]
            for i in range(len(self.coeff)-l):
                self.coeff[l+i]=0
            self.coeff[index+self.zero]=value


    def __add__(self, p2):
        if (len(self.coeff) > len(p2.coeff)):
            res = self.coeff 
            for i in range(len(p2.coeff)):
                res[i+self.zero] += p2.coeff[i+p2.zero]
        else:
            res = other.coeff
            for i in range(len(self.coeff)):
                res[i+p2.zero] += self.coeff[i+self.zero]
        return Polynomial(res)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = numpy.zeros(M+N+1)
        for i in range(0, M+1):
            for j in range(0, N+1):
                result_coeff[i+j] += c[i]*d[j]
        return Polynomial(result_coeff)

    def __eq__(self,other):
        c = self.coeff
        d = other.coeff
        if (c==d):
            return 1
        else:
            return 0


    def __repr__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
                    
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        if s[0:3] == ' + ':                    
            s = s[3:]
        if s[0:3] == ' - ':                            
            s = '-' + s[3:]
        return s

    def __str__(self):
        s = ''
        for i in range(self.zero, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], len(self.coeff)-self.zero-i)
        for i in range(self.zero, 0):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], -i)
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        if s[0:3] == ' + ':
            s = s[3:]
        if s[0:3] == ' - ':
            s = '-' + s[3:]
        return s


if __name__ == '__main__':
    main()