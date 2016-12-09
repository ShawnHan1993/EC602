                                  

class Polynomial():
    def __init__(self, arr=[]):
        self.dic = {}

        if len(arr) != 0:
            for i in range(0, len(arr)):
                self.dic[len(arr) - 1 - i] = arr[i]


    def __add__(self, other):
        result = Polynomial([])

        range = set(list(self.dic.keys()) + list(other.dic.keys()))

        for key in range:
            if not (key in self.dic):
                self.dic[key] = 0

            if not(key in other.dic):
                other.dic[key] = 0

            result.dic[key] = self.dic[key] + other.dic[key]

        return result


    def __sub__(self, other):
        result = Polynomial([])

        range = set(list(self.dic.keys()) + list(other.dic.keys()))

        for key in range:
            if not (key in self.dic):
                self.dic[key] = 0

            if not (key in other.dic):
                other.dic[key] = 0

            result.dic[key] = self.dic[key] - other.dic[key]

        return result


    def __eq__(self, other):
        dic1 = {}
        dic2 = {}

        for key1 in self.dic.keys():
            if self.dic[key1] != 0:
                dic1[key1] = self.dic[key1]

        for key2 in other.dic.keys():
            if other.dic[key2] != 0:
                dic2[key2] = other.dic[key2]

        if dic1 == dic2:
            return True
        else:
            return False


    def __mul__(self, other):
        result1 = Polynomial([])
        result2 = Polynomial([])
        index = 0

        for key1 in self.dic.keys():

            result1.dic={}
            for key2 in other.dic.keys():
                result1.dic[key1+key2] = self.dic[key1] * other.dic[key2]

            if index == 0:
                result2.dic = result1.dic
            else:
                result2 = result2 + result1

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
        result = Polynomial([])

        for key in self.dic.keys():
            if key != 0:
                result.dic[key - 1] = key * self.dic[key]

        return result


    def eval(self, base):
        result = 0

        for key in self.dic.keys():
            result += (base ** key) * self.dic[key]

        return result





