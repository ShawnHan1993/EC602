                                   
                                 
                               
                         
                                  

class Polynomial():
    def __init__(self, poly):
        self.poly = {};
        poly_reversed = poly[::-1]
        for i in range(len(poly)):
            self.poly[i] = poly_reversed[i]
   
    def __repr__(self):
        expression = ''
        count = 0
        for exponent in self.poly:
            expression += str(self.poly[exponent]) + "x^" + str(exponent)
            if count + 1 <  len(self.poly):
                expression += " + "
                count += 1
        return expression

    def __setitem__(self, exponent, value):
        self.poly[exponent] = value

    def __getitem__(self, exponent):
        return self.poly[exponent]
       
    def __add__(self, poly):
         result_dict = {}
         result = Polynomial([])
         for exponent_self in self.poly:
             if exponent_self in poly.poly:
                 result_dict[exponent_self] = self.poly[exponent_self] + poly.poly[exponent_self]
             else:
                 result_dict[exponent_self] = self.poly[exponent_self]
         for exponent_add in poly.poly:
             if exponent_add not in self.poly:
                 result_dict[exponent_add] = poly.poly[exponent_add]
         for exponent in result_dict:
             result[exponent] = result_dict[exponent]
         return result

    def __sub__(self, poly):
         result_dict = {}
         result = Polynomial([])
         for exponent_self in self.poly:
             if exponent_self in poly.poly:
                 result_dict[exponent_self] = self.poly[exponent_self] - poly.poly[exponent_self]
             else:
                 result_dict[exponent_self] = self.poly[exponent_self]
         for exponent_sub in poly.poly:
             if exponent_sub not in self.poly:
                 result_dict[exponent_sub] = -poly.poly[exponent_sub]
         for exponent in result_dict:
             result[exponent] = result_dict[exponent]
         return result

    def __mul__(self, poly):
        result_dict = {}
        result = Polynomial([])
        for exponent_self in self.poly:
            for exponent_mul in poly.poly:
                if exponent_self + exponent_mul not in result_dict:
                    result_dict[exponent_self + exponent_mul] = self.poly[exponent_self]\
                                                                * poly.poly[exponent_mul]
                else:
                    result_dict[exponent_self + exponent_mul] += self.poly[exponent_self]\
                                                                * poly.poly[exponent_mul]
        for exponent in result_dict:
            result[exponent] = result_dict[exponent]
        return result

    def __eq__(self, poly):
        return isinstance(poly, Polynomial) and self.poly == poly.poly

    def eval(self, val):
        result = 0
        for exponent in self.poly:
            result += self.poly[exponent]*pow(val, exponent)
        return result

    def deriv(self):
        result_dict = {}
        result = Polynomial([])
        for exponent in self.poly:
            if exponent != 0:
                result_dict[exponent - 1] = exponent*self.poly[exponent]
            else:
                result_dict[exponent] = 0
        for exponent in result_dict:
            result[exponent] = result_dict[exponent]
        return result

def main():
    print("Please enter the Polynomial and implement calculations as you want, e.g: a=Polynomial([1,2,3])")
    pass

if __name__=="__main__":
    main()
