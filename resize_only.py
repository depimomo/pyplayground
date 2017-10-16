import os
import os.path
from PIL import Image, ImageChops
from resizeimage import resizeimage

for dirpath, dirnames, filenames in os.walk("/media/monica/DATA/GoogleDrive/KULIAH/materi kuliah/smt7/SKRIPSI/DATASET/sisa"):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
    	name = os.path.join(dirpath, filename)
    	print(name)
    	im = Image.open(name)
    	im.resize([500, 670])
    	im.save(name)
    	im.close()