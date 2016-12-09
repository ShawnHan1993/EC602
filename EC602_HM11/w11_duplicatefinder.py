from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib
def searchKey(name):
    number = int(re.search(r'[0-9]{1,10}',name).group(0))
    return number
    
def searchKeyM(line):
    number = int(re.search(r'[0-9]{1,10}',line[0]).group(0))
    return number
    
foldername = './test_b'
filenames = listdir(foldername)
bigDict = {}
for name in filenames:
    if name[len(name) - 3:len(name)] == 'png':
        histogram = [0] * 3 * 256
        im = imread(foldername+'/'+name)
        for i in range(im.shape[0]):
            for j in range(im.shape[1]):
                if (im[i,j] != np.array([255,255,255], dtype = np.uint8)).any():
                    histogram[int(im[i,j,0])] = histogram[int(im[i,j,0])] + 1
                    histogram[int(im[i,j,1]) + 256] = histogram[int(im[i,j,1]) + 256] + 1
                    histogram[int(im[i,j,2]) + 512] = histogram[int(im[i,j,2]) + 512] + 1
        keyTmp = ''.join(str(e) for e in histogram)
        bigDict.setdefault(keyTmp,[]).append(name)
        
result = []
tmp = list(bigDict.values())
for i in range(len(tmp)):
    result.append(sorted(tmp[i],key = searchKey))
result = sorted(result,key = searchKeyM)
for i in range(len(result)):
    result[i] = ' '.join(e for e in result[i])
result = '\n'.join(e for e in result)
result = result + '\n'
m = hashlib.sha256()
m.update(result.encode('utf-8'))
res = m.hexdigest()
print(res)
