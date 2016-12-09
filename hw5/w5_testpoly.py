# AUTHOR Shen Han shawnhan@bu.edu
# AUTHOR Changlong Jiang cljiang@bu.edu
import unittest
import sys
authors=['shawnhan@bu.edu','cljiang@bu.edu']
#from poly42 import *
#from w4_polynomial import *

class PolynomialTestCase(unittest.TestCase):
    #unit testing for polynomial

    def setUp(self):
        pass
    
    def test_init(self):
        z=Polynomial([])
        self.assertIsInstance(z,Polynomial)

    def test_eq(self):
        a=Polynomial([1,2,43+1j,0])
        b=Polynomial([1,2,43+1j,0])
        self.assertEqual(a,b)

    def test_noteq(self):
        a=Polynomial([0,1,2,43])
        b=Polynomial([1,2,43])
        self.assertNotEqual(a,b)
        a=Polynomial([10,2,43])
        b=Polynomial([1,2,43])
        self.assertNotEqual(a,b)
        a=Polynomial([10,2,43])
        b=Polynomial([1,2+1j,43])
        self.assertNotEqual(a,b)
    
    def test_getitem(self):
        a=Polynomial([1,2,43,0])
        self.assertEqual(a[1],43)
        self.assertEqual(a[100],0)
        self.assertEqual(a[-10],0)
    
    def test_setitem(self):
        a=Polynomial([1,2,43,3,8])
        a[1]=5
        self.assertEqual(a,Polynomial([1,2,43,5,8]))
        Size =sum(sys.getsizeof(getattr(a,x)) for x in vars(a))
        a=Polynomial(1000*[0]+[1,2,43,3,8]+1000*[0])
        Size2 =sum(sys.getsizeof(getattr(a,x)) for x in vars(a))
        self.assertEqual(Size2,Size)
        


    def test_descend(self):
        a=Polynomial([1,2,43,0])
        self.assertEqual(a[3],1)
        self.assertEqual(a[2],2)
        self.assertEqual(a[1],43)
        self.assertEqual(a[0],0)

    def test_add(self):
        a=Polynomial([1,2,43,0])
        b=Polynomial([-1,2,1,2])
        c=a+b
        self.assertEqual(c,Polynomial([4,44,2]))
        a=Polynomial([2,43,0])
        b=Polynomial([-1,2,1,2])
        c=a+b
        self.assertEqual(c,Polynomial([-1,4,44,2]))

    def test_sub(self):
        a=Polynomial([1,2,43,0])
        b=Polynomial([1,2])
        c=a-b
        self.assertEqual(c,Polynomial([1,2,42,-2]))

    def test_mul(self):
        a=Polynomial([2,43])
        b=Polynomial([1,2])
        c=a*b
        self.assertEqual(c,Polynomial([2,47,86]))
    
    def test_eval(self):
        a=Polynomial([1,2,43,0])
        c=a.eval(5)
        self.assertEqual(c,390)

    def test_negative(self):
        a=Polynomial([])
        a[-1]=5
        c=a.eval(5)
        self.assertEqual(c,1)

    def test_deriv(self):
        a=Polynomial([2,3,5])
        c=a.deriv()
        self.assertEqual(c,Polynomial([4,3]))

    def test_sparse_zeros(self):
        n = 10000
        p = Polynomial([0]*n)
        q = Polynomial()
        p_size =sum(sys.getsizeof(getattr(p,x)) for x in vars(p))
        q_size =sum(sys.getsizeof(getattr(q,x)) for x in vars(q))        
        factor_increase = p_size/q_size
        self.assertEqual(p,q)
        self.assertLess(factor_increase,2,msg='Implementation not sparse, init with {} zeros'.format(n))

    def tearDown(self):
        "tear down"

if __name__=='__main__':
    unittest.main()