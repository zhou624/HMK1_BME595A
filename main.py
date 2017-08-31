# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Yifeng Zhou, zhou624@purdue.edu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from conv import Conv2D
import time
#%%
# Part A
ImageTitle='rock' # summer or rock or bob
loadimage=misc.imread(ImageTitle+'.jpg')
in_channel=3
o_channel=1
kernel_size=3
stride=1
mode='known'
conv2d = Conv2D(in_channel, o_channel, kernel_size, stride,mode)
[IteNumber, ConvImage] = conv2d.forward(loadimage)
ConvImageShape=ConvImage.shape
for ImNum in range(0, ConvImageShape[2]):
    misc.imsave(ImageTitle+'_ochannel_'+str(o_channel)+'_ksize_'+str(kernel_size)+'_stride_'+str(stride)+'_'+str(ImNum)+'_'+'.jpg',ConvImage[:,:,ImNum])

#%%
# Part B
ImageTitle='bob'
loadimage=misc.imread(ImageTitle+'.jpg')
in_channel=3
kernel_size=3
stride=1
mode='rand'
timeconsumption=np.zeros(11,dtype=np.int)
cnt=0
for o_channel in np.power(2,range(0,11)):
    conv2d = Conv2D(in_channel, o_channel, kernel_size, stride,mode)
    tic1=time.clock()
    [IteNumber, ConvImage] = conv2d.forward(loadimage)
    toc1=time.clock()
    timeconsumption[cnt]=toc1-tic1
    cnt=cnt+1
    print(cnt)
plt.plot(range(0,11),timeconsumption)
plt.ylabel('time consumption / second')
plt.xlabel('2^i (i = 0, 1, …, 10)')
#%%
## part C
ImageTitle='summer'
loadimage=misc.imread(ImageTitle+'.jpg')
in_channel=3
o_channel=2
stride=1
mode='rand'
conv2d = Conv2D(in_channel, o_channel, kernel_size, stride,mode)
cnt=0
operations=np.zeros(5,dtype=np.int)
for kernel_size in [3,5,7,9,11]:
    conv2d = Conv2D(in_channel, o_channel, kernel_size, stride,mode)
    [IteNumber, ConvImage] = conv2d.forward(loadimage)
    operations[cnt]=IteNumber
    cnt=cnt+1
    print(cnt)
plt.plot([3,5,7,9,11],operations)
plt.ylabel('number of operations')
plt.xlabel('kernel_size=3, 5, …, 11')



