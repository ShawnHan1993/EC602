
class Polynomial():
    def __init__(self,sequence=None):
        if sequence:
            N=len(sequence)
            self.values = [(N-i-1,x) for i,x in enumerate(sequence) if x]
        else:
            self.values = []
        self.values.sort()
    def __contains__(self,expon):
        if len(self.values)==0:
            return False

        l,m,u = 0,len(self.values)//2,len(self.values)
        while l < m <  u:
            if self.values[m][0] > expon:
                u = m
            elif self.values[m][0] == expon:
                break
            else:
                l = m
            m = (l+u)//2 

        return self.values[m][0] == expon
       
    def __add__(self,other):
        Sum = Polynomial()
        Sum.values = self.values + other.values
        Sum.values.sort()
        i = 0
        values = []
        while i < len(Sum.values):
            if i == len(Sum.values)-1:
                values.append(Sum.values[i])
            elif Sum.values[i][0]==Sum.values[i+1][0]: # combine

                values.append((Sum.values[i][0],Sum.values[i][1]+Sum.values[i+1][1]))
                i += 1
            else:
                values.append(Sum.values[i])
            i = i + 1
        Sum.values = values

        return Sum


    def __sub__(self,other):
        Sum = Polynomial()
        Sum.values = self.values[:]+[(x,-v) for (x,v) in other.values]
        Sum.values.sort()
        i = 0
        values = []
        while i < len(Sum.values):
            if i == len(Sum.values)-1:
                values.append(Sum.values[i])
            elif Sum.values[i][0]==Sum.values[i+1][0]: # combine

                values.append((Sum.values[i][0],Sum.values[i][1]+Sum.values[i+1][1]))
                i += 1
            else:
                values.append(Sum.values[i])
            i = i + 1
        Sum.values = values

        return Sum


    
    def __mul__(self,other):
        Prod=Polynomial()
        for (expon1,coeff1)in self.values:
            for (expon2,coeff2) in other.values:
                Prod[expon1+expon2] += coeff1 * coeff2
        return Prod

    def __setitem__(self,expon,value):
        if len(self.values)==0:
            if value:
                self.values = [(expon,value)]
            return

        l,m,u = 0,len(self.values)//2,len(self.values)-1

        while l<m<u:
            if self.values[m][0] > expon:
                u = m
            elif self.values[m][0] == expon:
                break
            else:
                l = m
            m = (l+u)//2 

        if self.values[m][0] == expon:
            if not value:
                del self.values[m]
            else:
                self.values[m] = (expon,value)
        elif value:
            self.values.append((expon,value))
            self.values.sort()

    
    def __getitem__(self,expon):
        if len(self.values)==0:
            return 0
        if self.values[0][0] == expon:
            return self.values[0][1]

        l,m,u = 0,len(self.values)//2,len(self.values)
        while l < m <  u:
            if self.values[m][0] > expon:
                u = m
            elif self.values[m][0] == expon:
                break
            else:
                l = m
            m = (l+u)//2 

        if self.values[m][0] == expon:
            return self.values[m][1]
        else:
            return 0


    def __eq__(self,other):
        return self.values == other.values

    def __str__(self):
        return "Polynomial({})".format(self.values)

    def __repr__(self):
        return str(self)


    def eval(self,x):
        t = 0
        for (expon,coeff) in self.values:
            t += x**expon * coeff
        return t

    def deriv(self):
        P = Polynomial()
        for (expon,coeff) in self.values:
            P[expon-1] = expon * coeff
        return P
