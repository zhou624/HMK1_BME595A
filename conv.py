# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 19:55:01 2017

@author: Yifeng Zhou, zhou624@purdue.edu
"""

import numpy as np
class Conv2D:
    def __init__(self,in_channel, o_channel, kernel_size, stride, mode):
        self.in_channel=in_channel
        self.o_channel=o_channel
        self.kernel_size=kernel_size
        self.stride=stride
        self.mode=mode
    def forward(self,input_image):
        K1 = np.array([[-1,-1,-1],
                    [0,0,0],
                    [1,1,1]])
        k2 = np.array([[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]])
        k3 = np.array([[1,1,1],
                    [1,1,1],
                    [1,1,1]])
        k_3=np.stack((K1,k2,k3),axis=0)
        k4 = np.array([[-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1],
                    [0,0,0,0,0],
                    [1,1,1,1,1],
                    [1,1,1,1,1]])
        k5 = np.array([[-1,-1,0,1,1],
                    [-1,-1,0,1,1],
                    [-1,-1,0,1,1],
                    [-1,-1,0,1,1],
                    [-1,-1,0,1,1]])
        k_5=np.stack((k4,k5),axis=0)
        mode=self.mode
        kernel_size=self.kernel_size
        stride=self.stride
        o_channel=self.o_channel
        in_channel=self.in_channel
        xdim=input_image.shape[0]
        ydim=input_image.shape[1]
        outputX=len(list(range(kernel_size,xdim+1,stride)))
        outputY=len(list(range(kernel_size,ydim+1,stride)))
        OutputImage=np.zeros((outputX,outputY,o_channel),dtype=np.int)
        num_operation=0
        if mode=='known':
            if (kernel_size==3)&(o_channel==1):
                kernel=K1        
            elif kernel_size==3:
                kernel=k_3
            elif kernel_size==5:
                kernel=k_5
        elif mode=='rand':
            kernel=np.random.rand(kernel_size,kernel_size,o_channel)
        if in_channel==3:
            input_image= np.average(input_image, weights=[0.299, 0.587, 0.114], axis=2)
        for outchannel in range (0,o_channel):  
            for i1 in range(0,outputX):
                for j1 in range(0,outputY):
                    if o_channel==1:
                        kernelMulti=kernel
                    else:
                        #kernelMulti=kernel[:,:,outchannel]
                        kernelMulti=kernel[outchannel,:,:]
                    kernelMulti=np.transpose(kernelMulti)
                    tempmat=np.multiply(kernelMulti,  input_image[ stride*i1 : stride*i1+kernel_size, stride*j1 : stride*j1+kernel_size ])
                    OutputImage[i1,j1,outchannel]=np.sum(tempmat)
                    num_operation=num_operation+1
        return num_operation,OutputImage