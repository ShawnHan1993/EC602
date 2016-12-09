                              

class Polynomial():
    def __init__(self, coeff=[]):
        self.coeff = coeff
        self.expo = []
        for i in range(len(self.coeff)):
            self.expo.insert(i,-i)

    def __setitem__(self, expo, coeff):
        if expo in self.expo:
            n = self.expo.index(expo)
            self.coeff[n] = coeff
        else:
            self.expo.append(expo)
            self.coeff.append(coeff)

    def __getitem__(self, expo):
        n = self.expo.index[expo]
        return (self.coeff[n])

    def __add__(self, other):
        result = Polynomial([])
        for i in self.expo:
            n = self.expo.index(i)
            m = other.expo.index(i)
            if i in other.expo:
                result.expo.append(i)
                result.coeff.append(self.coeff[n] + other.coeff[m])
            else:
                result.expo.append(i)
                result.coeff.append(self.coeff[n])
        for i in other.expo:
            m = other.expo.index(i)
            if i in result.expo:
                break
            else:
                result.expo.append(i)
                result.coeff.append(other.coeff[m])
        return Polynomial(result)

    def __sub__(self, other):
        result = Polynomial([])
        for i in self.expo:
            n = self.expo.index(i)
            if i in other.expo:
                m = other.expo.index(i)
                result.expo.append(i)
                result.coeff.append(self.coeff[n] - other.coeff[m])
            else:
                result.expo.append(i)
                result.coeff.append(self.coeff[n])
        for i in other.expo:
            m = other.expo.index(i)
            if i in result.expo:
                break
            else:
                result.expo.append(i)
                result.coeff.append(0 - other.coeff[m])
        return Polynomial(result)

    def __mul__(self, other):
        result = Polynomial([])
        for i in self.expo:
            n = self.expo.index(i)
            for j in self.expo:
                m = other.expo.index(j)
                if (i + j) in result.expo:
                    result_coeff[n + m] += (self.coeff[n] + other.coeff[m])
                else:
                    result.expo.append(i + j)
                    result.coeff.append(self.coeff[n] + other.coeff[m])
        return Polynomial(result)

    def __eq__(self, other):
        result = 0
        for i in self.expo:
            n = self.expo.index(i)
            if i in other.expo:
                m = other.expo.index(i)
                if self.coeff[n] == other.coeff[m]:
                    result = 1
        if result ==1:
            return True
        else:
            return False

    def eval(self, value):
        result = 0
        total = 0
        for i in self.expo:
            n = self.expo.index(i)
            total = self.coeff[n] * (value ** i)
            result += total
        return result

    def deriv(self):
        j = 0
        for i in self.expo:
            n = self.expo.index(i)
            if self.coeff[n] != 0:
                i = i - 1
                self.coeff[n] = i * self.coeff[n]
            else:
                del self.coeff[n]
                del self.expo[j]
            j = j + 1
        return Polynomial(self.coeff)

if __name__=="__main__":
    main()
