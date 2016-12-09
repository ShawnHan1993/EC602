                                  

class Polynomial():
    def __init__(self, arr=[]):
        self.dic = {}

        if len(arr) != 0:
            for i in range(0, len(arr)):
                self.dic[len(arr) - 1 - i] = arr[i]


    def __add__(self, other):
        for key in other.dic.keys():
            if key in self.dic:
                self.dic[key] += other.dic[key]
            else:
                self.dic[key] = other.dic[key]

        return self


    def __sub__(self, other):
        for key in other.dic.keys():
            if key in self.dic:
                self.dic[key] -= other.dic[key]
            else:
                self.dic[key] = 0 - other.dic[key]

        return self


    def __eq__(self, other):
        if self.dic == other.dic:
            return True
        else:
            return False


    def __mul__(self, other):
        result1 = Polynomial([])
        result2 = Polynomial([])
        index = 0

        for key1 in self.dic:

            result1.dic={}
            for key2 in other.dic:
                result1.dic[key1+key2] = self.dic[key1] * other.dic[key2]

            if index == 0:
                result2.dic = result1.dic
            else:
                result2 += result1

            index += 1

        return result2


    def __setitem__(self, key, value):
        self.dic[key] = value

        return self


    def __getitem__(self, key):
        if key in self.dic:
            return self.dic[key]
        else:
            return 0


    def deriv(self):
        for key in self.dic:
            self.dic[key - 1] = key * self.dic[key]

        return self


    def eval(self, base):
        result = 0

        for key in self.dic:
            result += (base ** key) * self.dic[key]

        return result





