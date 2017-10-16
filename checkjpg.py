# import glob, os
# os.chdir("/media/monica/DATA/GoogleDrive/KULIAH/materi kuliah/smt7/SKRIPSI/DATASET/1_1017_crop_clean/0001")
# for file in glob.glob("*.jpg"):
#     print(file)

import os
import os.path

for dirpath, dirnames, filenames in os.walk("/media/monica/DATA/GoogleDrive/KULIAH/materi kuliah/smt7/SKRIPSI/DATASET/1_1017_crop_clean/0002"):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
    	print(os.path.join(dirpath, filename))