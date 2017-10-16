import os
import os.path
from PIL import Image

for dirpath, dirnames, filenames in os.walk("/media/monica/DATA/GoogleDrive/KULIAH/materi kuliah/smt7/SKRIPSI/DATASET/1_1017_full"):
    for x in range(501,751):
    	for filename in [f for f in filenames if f.startswith("0" + str(x)) and f.endswith("_4.jpg")]:
    		name = os.path.join(dirpath, filename)
    		print(name)
    		im = Image.open(name)
    		w, h = im.size
    		im = im.crop((0, 2400, w, h))
    		im.save(name, im.format)
    		im.close()