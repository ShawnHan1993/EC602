                             


class Polynomial():
    pass

    def __init__(self, data={}):
        self.raw_data = data
        self.data = dict()
        for index, element in enumerate(data):
            self.data[(len(data) - index - 1)] = element

    def __setitem__(self, index, value):
        self.data[index] = value

    def __eq__(self, other):
        return (self.data == other.data)

    def __sub__(self, other):
        result_dict = {}
        keys_tested = []

        for key in other.data:
            if key in self.data:
                result_dict[key] = self.data[key] - other.data[key]
            else:
                result_dict[key] = 0 - other.data[key]
            keys_tested.append(key)

        for key in self.data:
            if key not in keys_tested:
                if key in other.data:
                    result_dict[key] = self.data[key] - other.data[key]
                else:
                    result_dict[key] = self.data[key]

        answer_poly = Polynomial()
        answer_poly.data = result_dict
        return answer_poly

    def __add__(self, other):
        result_dict = {}
        keys_tested = []

        for key in other.data:
            if key in self.data:
                result_dict[key] = self.data[key] + other.data[key]
            else:
                result_dict[key] = 0 + other.data[key]
            keys_tested.append(key)

        for key in self.data:
            if key not in keys_tested:
                if key in other.data:
                    result_dict[key] = self.data[key] + other.data[key]
                else:
                    result_dict[key] = 0 + self.data[key]

        answer_poly = Polynomial()
        answer_poly.data = result_dict
        return answer_poly

    def __mul__(self, other):
        answer_poly = Polynomial([0])

        for b_key in other.data:
            temp_dict = {}
            for a_key in self.data:
                exponent = a_key + b_key
                temp_dict[exponent] = self.data[a_key] * other.data[b_key]
            temp1_poly = Polynomial()
            temp1_poly.data = temp_dict
            temp2_poly = Polynomial()
            temp2_poly.data = answer_poly.data
                            
                                    
                                    
                            
            (answer_poly).data = (temp1_poly + temp2_poly).data

                                     
                                      
                                 
        return answer_poly

    def eval(self, base):
        total = 0

        for key in self.data:
            total += (base**key) * self.data[key]
        return total

    def deriv(self):
        a = self.data
        result_dict = {}

        for key in a:
            result_dict[key-1] = a[key] * key

        answer_poly = Polynomial()
        answer_poly.data = result_dict
        return answer_poly


def main():
    pass
    foo = Polynomial([5, 2, 3, 0, 4])
    bar = Polynomial([3, 0, 4])
    mult_foobar = foo * bar
    sub_foobar = foo - bar
    add_foobar = foo + bar
    evaluation1 = foo.eval(3)
    evaluation2 = bar.eval(3)
    derivative = foo.deriv()
    print(add_foobar.data)
    print(sub_foobar.data)
    print(mult_foobar.data)
    print(evaluation1)
    print(evaluation2)
    print(derivative.data)

if __name__ == "__main__":
    main()
