                                      


class Polynomial:
                                                           

                                                                                        
                                                   

    def __init__(self, l):
        self.terms = {}

                                                                                  
        for i in range(len(l)):
            self[len(l) - i - 1] = l[i]

    def __add__(self, other):
                                             
        poly_sum = Polynomial([])

                                                                         
        poly_sum.terms = dict(self.terms)
        for exp, coeff in other.terms.items():
            if exp in poly_sum.terms:
                poly_sum[exp] += coeff
            else:
                poly_sum[exp] = coeff

        return poly_sum

    def __sub__(self, other):
                                             
        poly_difference = Polynomial([])

                                                                                       
        poly_difference.terms = dict(self.terms)
        for exp, coeff in other.terms.items():
            if exp in poly_difference.terms:
                poly_difference[exp] -= coeff
            else:
                poly_difference[exp] = -coeff

        return poly_difference

    def __mul__(self, other):
                                             
        poly_product = Polynomial([])

        for exp, coeff in self.terms.items():                             
            partial_product = Polynomial([])
            for other_exp, other_coeff in other.terms.items():                                  
                partial_product[exp + other_exp] = coeff * other_coeff

            poly_product += partial_product                                                 

        return poly_product

    def __eq__(self, other):
                                                                     
        equal = True

                                                                                                
        for exp, coeff in self.terms.items():
            if exp in other.terms and self[exp] != other[exp]:
                                                                                 
                equal = False

                                                                                                        
                                                                               
        if len(self.terms) != len(other.terms):
            equal = False

        return equal

    def eval(self, val):
                                                                     
        eval_sum = 0
        for exp, coeff in self.terms.items():                                                                     
            eval_sum += coeff * val**exp

        return eval_sum

    def deriv(self):
                                                                             
        poly_deriv = Polynomial([])

                                                                                               
                                                                                
        for exp, coeff in self.terms.items():
            new_coeff = coeff * exp
            if new_coeff != 0:
                poly_deriv[exp - 1] = new_coeff

        return poly_deriv

    def __getitem__(self, item):
        return self.terms[item]

    def __setitem__(self, key, value):
        self.terms[key] = value


def main():
    pass
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
       

if __name__ == '__main__':
    main()