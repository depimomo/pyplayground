from PIL import Image
from resizeimage import resizeimage

fd_img = open("/media/monica/DATA/GoogleDrive/KULIAH/materi kuliah/smt7/SKRIPSI/DATASET/1_1017_crop_clean/0001/aa.jpg", "r")
img = Image.open(fd_img)
#img = resizeimage.resize_width(img, 400)
img = resizeimage.resize_contain(img, [400, 100])
img.save('oo.jpg', img.format)
fd_img.close()
