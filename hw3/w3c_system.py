# AUTHOR Shen Han shawnhan@bu.edu
# AUTHOR Changlong Jiang cljiang@bu.edu
# AUTHOR Xinyu Li lxinyu@bu.edu

import numpy as np
import sys
h=input()
x=input()
h=h.split()
for i in range(len(h)):
    h[i]=float(h[i])
x=x.split()
for j in range(len(x)):
    x[j]=float(x[j])
result=np.convolve(h,x)
result_list=[]
size_array=result.shape
for i in range(size_array[0]):
    result_list.append(result[i].item())
#result_list = set(result_list)
print(" ".join(str(xx) for xx in result_list))

