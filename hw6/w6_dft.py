# AUTHOR Shen Han shawnhan@bu.edu
# AUTHOR Changlong Jiang cljiang@bu.edu
from numpy import zeros,exp,array,pi

def DFT(value): 
    a=array([1])
    if type(a)==type(value):
        tmp=value.shape
        if len(tmp)!=1:
            raise ValueError('please input a 1 dimentional sequence')
            return 
    #if type(value)==type(range(0,2)) or type(a)==type(value) or type(value)==type([1,2]) or type(value)==type((1,2)):
    if hasattr(value,'__getitem__') and (type(value)!=type({1:2})):
        N=len(value)
        result=zeros((N,),dtype=complex)
        for k in range(N):
            for n in range(N):
                tmp=value[n]
                if type(tmp)==type('a'):
                    raise ValueError('please input a sequence of number')
                    return
                tmp=tmp*exp((-1)*1j*2*pi*k*n/N)
                result[k]=result[k]+tmp
        return result         
    else:
        raise ValueError('please input a sequence of number')
        
