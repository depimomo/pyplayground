import os
import pandas as pd
import numpy as np
from PIL import Image
import glob
import tensorflow as tf
import pickle
from scipy.misc import toimage

### 1-1 Save 200 Gabor masks of panda data frame ( Panda is the fastest one ) & convert it as tf objects
# -> Output: array of tf objects


def gabor(gaborfiles):

    w = np.array([np.array(pd.read_csv(file, index_col=None, header=-1)) for file in gaborfiles])

    wlist = [] # 200 gabor wavelet
    for i in range(len(w)):
        chwi = np.reshape(np.array(w[i], dtype='f'), (w[i].shape[0], w[i].shape[1], 1, 1))
        wlist.append( tf.Variable(np.array(chwi)) )

    wlist2 = np.array(wlist)

    return wlist2


### 1-2 Import & resize image  (convert into array and change data type as float32)
def image_resize(allimage, shape):

    badlist = []; refined = []
    for i in range(len(allimage)):
        badlist.append(Image.open(allimage[i]))
        refined.append(badlist[i].resize(shape, Image.ANTIALIAS))

    refinedarr = np.array([np.array((fname), dtype='float32') for fname in refined])

    imgreshape = refinedarr.reshape(-1,refinedarr.shape[1],refinedarr.shape[2],1)

    return imgreshape


### 1-3 Convolution b/w allimages and 200 gabor masks

def conv_model(imgresize, wlist, stride):
    imgresize3 = []
    for i in range(len(wlist)):
        imgresize3.append(tf.nn.conv2d(imgresize, wlist[i],
                                       strides=[1, stride, stride, 1], padding='SAME'))

    imgresize5 = tf.transpose(imgresize3, perm=[0, 1, 2, 3, 4])

    return imgresize5