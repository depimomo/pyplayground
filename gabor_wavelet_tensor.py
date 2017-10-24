import glob
import tensorflow as tf
import gabor_wavelet as gb


# gabor mask
gabor1 = glob.glob('gabor_wavelet_filter_bank/*.csv')
mask = gb.gabor(gabor1)

gaborname = [s.strip('gabor_wavelet_filter_bank\\') for s in gabor1 ]
gaborname = [s.strip('.csv') for s in gaborname ]

# Image
imglist = glob.glob('*.jpg') # Images as many as you want 
imgresize = gb.image_resize(imglist, (128, 128)) /255. # imgresize.shape # (N,256,256)
imglistfin = [s.strip('.jpg') for s in imglist]


imglistfin = [s.strip('.jpg') for s in imglist]
imgname = [s.strip('ROItest\\') for s in imglistfin]


# convolution
X = tf.placeholder("float", [None, 128, 128, 1])
train = gb.conv_model(X, mask, 1) # Stride = 1 generates (128, 128) size image. If Stride = 4, then (32, 32) size image 

batch_size = 20 # # of Batch 

# Tensorflow Sessioin

init_op = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init_op)

    convresult = []
    training_batch = zip(range(0, len(imgresize), batch_size), range(batch_size, len(imgresize) + 1, batch_size))
    for start, end in training_batch:
        convresult.append( sess.run(train, feed_dict={X:imgresize[start:end] }) )

convresult # (200, # of image, convolved_size, convolved_size, 1 ) 
# if stride =1, convolved_size = 128 ; if stride = 4 , convolved_size = 32