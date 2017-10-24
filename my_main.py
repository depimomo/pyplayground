import tensorflow as tf
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numba import cuda

plt.style.use('ggplot')

#hide warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

#list images
def get_handwriting_list():
	files = [os.path.join("1_475_new", file_i)for file_i in os.listdir("1_475_new")if ".jpg" in file_i]
	# print(files)
	return files

#load images
def get_handwriting_files():
	 return [plt.imread(f_i) for f_i in get_handwriting_list()]

#build gabor filters
def build_filters():
	filters = []
	ksize = 31

	for theta in np.arange(0, np.pi, np.pi / 16):
		kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
		kern /= 1.5*kern.sum()
		filters.append(kern)
		return filters

#process
@cuda.jit
def process(img, filters):
	accum = np.zeros_like(img)
	for kern in filters:
		fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
		np.maximum(accum, fimg, accum)
		return accum

#read the file
imgs = get_handwriting_files()

#'flatten' images into one array
data = np.array(imgs)
print(data.shape)

#TODO: kelompokin imagenya berdasar gender (dicek dari label.csv) baru digabungin jadi satu array