import skimage.io
import numpy
import random
import itertools
import json

r=random.choice

rr=random.randrange

N=40
ALL_COLORS="bgry"

def flip(squares):
    for i in range(len(squares)):
        squares[i] = (squares[i][1],squares[i][0])
    

def rotate(squares,fullextent):
    for i in range(len(squares)):
        squares[i] = (fullextent-1-squares[i][1],squares[i][0])

#random parameters
def make_aliens(extent,weight,photosize,copies=1,colors=4):
    """extent     how big the alien is (x,y)
    weight     how many squares the alien has
    copies     how many photos to include of this alien
    colors     how many colors this alien has
    photosize  how big to make the picture (x,y)
    """
    my_colors=random.sample(ALL_COLORS,colors)

    Body =[r(my_colors) for x in range(weight)]
    Squares = random.sample(
        list(itertools.product(range(extent[0]),range(extent[1]))),weight)
    Pictures=[]
    fullextent=max(extent)
    for x in range(copies):
        for y in range(rr(2)):
            flip(Squares)
        for y in range(rr(4)):
            rotate(Squares,fullextent)
        Xoffset = rr(photosize[0]-fullextent)
        Yoffset = rr(photosize[1]-fullextent)
        the_picture=[]
        for (x,y),c in zip(Squares,Body):
            the_picture.append( (Yoffset+y, Xoffset+x, c) )

        Pictures.append(the_picture)
    return Pictures

Colors = {'r':(255,0,0),'b':(0,0,255),'g':(0,255,0),'y':(255,255,0)}
colorlist = list(Colors.keys())

A = []
Answers = []
imsize = (80,60,3)

Files = 1123

count = 0
for i in range(200):
    colors = random.randint(1,4)
    copies = random.randint(1,15)
    extent = ( random.randint(10,40), random.randint(10,40))
    weight = random.randint(99,max(100,extent[1]*extent[0]-50))

    A.extend(make_aliens(extent, weight, imsize[:2], copies, colors))

    Answers.extend ([(i,count + x) for x in range(copies)])
    count += copies
    if count > Files:
        break

random.shuffle(Answers)

Ps = ['cherry','apple','pear','orange','banana','rasberry','grape','kiwi']
def prefix():
    k=random.choice(Ps)
    return k[0:rr(3,9)]

for i, (j,k) in enumerate(Answers[:Files]):
    image = A[k]
    P = 255*numpy.ones ( imsize, dtype="uint8")
    for (x,y,c) in image:
        P[y,x,:] =Colors[c]

    skimage.io.imsave('{}{}.png'.format(prefix(),i),P)


