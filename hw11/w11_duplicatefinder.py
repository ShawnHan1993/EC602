from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib

filenames=listdir('.\example1')
cc=0