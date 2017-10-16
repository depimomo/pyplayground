import os
import os.path
from PIL import Image

ma_he = 0
mi_he = 10000

for dirpath, dirnames, filenames in os.walk("/media/monica/DATA/GoogleDrive/KULIAH/materi kuliah/smt7/SKRIPSI/DATASET/1_475_new"):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
    	name = (os.path.join(dirpath, filename))
    	im = Image.open(name)
    	_, height = im.size
    	if ma_he < height:
    		ma_he = height
    		print("ma_he:" + str(ma_he) + " \n")
    		print(name + "\n\n")
    	if mi_he > height:
    		mi_he = height
    		print("mi_he:" + str(mi_he) + "\n")
    		print(name + "\n\n")
