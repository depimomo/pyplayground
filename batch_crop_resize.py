import os
import os.path
from PIL import Image, ImageChops
from resizeimage import resizeimage

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

for dirpath, dirnames, filenames in os.walk("/media/monica/DATA/GoogleDrive/KULIAH/materi kuliah/smt7/SKRIPSI/DATASET/1_475_latin"):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
    	name = os.path.join(dirpath, filename)
    	print(name)
    	im = Image.open(name)
    	im = trim(im)
    	im = resizeimage.resize_width(im, 500)
    	im.save(name)
    	im.close()