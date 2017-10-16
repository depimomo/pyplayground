from PIL import Image, ImageChops
from resizeimage import resizeimage

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

#im = Image.open("/media/monica/DATA/GoogleDrive/KULIAH/materi kuliah/smt7/SKRIPSI/DATASET/1_1017_crop_clean/0001/aa.jpg")
im = Image.open("gg.jpg")
im = trim(im)
im = resizeimage.resize_width(im, 400)
#im = resizeimage.resize_contain(im, [400, 100])
im.save('oo.jpg', im.format)
im.close()