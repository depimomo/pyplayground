import tensorflow as tf
import cv2

# Create a 3x3 Gabor filter
params = {'ksize':(3, 3), 'sigma':1.0, 'theta': 0, 'lambd':15.0, 'gamma':0.02}
filter = cv2.getGaborKernel(**params)
# make the filter to have 4 dimensions.
filter = tf.expand_dims(filter, 2)
filter = tf.expand_dims(filter, 3)

# Apply the filter on `image`
answer = tf.conv2d(image, filter, strides=[1, 1, 1, 1], padding='SAME')