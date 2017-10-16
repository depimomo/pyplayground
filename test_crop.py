import os
import os.path
from PIL import Image
from resizeimage import resizeimage

im = Image.open("2.jpg")
#w, h = im.size
#im = im.crop((0, 2400, w, h))
#im = resizeimage.resize_crop(im, [4940, 6700])
im.thumbnail([500, 670], Image.ANTIALIAS)
im.save("2_b.jpg", im.format)
im.close()