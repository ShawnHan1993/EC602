# AUTHOR Shen Han shawnhan@bu.edu
# AUTHOR Changlong Jiang cljiang@bu.edu
import unittest
import numpy as np
#import w6_dft
import random

class DFTTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def testTypeAndShape(self):
        x=np.array([1,1,1])
        y=DFT(x)
        self.assertEqual(type(x),type(y))
        N=len(y)
        self.assertEqual(3,N)

    def testInput(self):
        try:
            x="asdfasdf"
            y=DFT(x)
            raise TypeError('You dont check the type of input')
        except ValueError:
            pass
  
    def testResult(self):
        for i in range(2,21):
            N=i
            a=[0]*N
            for kk in range(10):
                for k in range(N):
                    a[k]=(2*random.random()-1)*(2*random.random()-1)*1j
                a=np.array(a)
                b=DFT(a)
                c=np.fft.fft(a)
                if numpy.allclose(b,c):
                    pass
                else:
                    raise ValueError                  
    
    def tearDown(self):
        "tear down"  
        
if __name__=='__main__':
    from w6_dft import DFT
    unittest.main()
        
        
             

