#import astropy
#astropy.test()

# from astropy.visualization import SqrtStretch
# stretch = SqrtStretch()
# print(stretch([0., 0.25, 0.5, 0.75, 1.]))

import numpy as np
import matplotlib.pyplot as plt

from astropy.visualization import (MinMaxInterval, SqrtStretch, ImageNormalize)

# Generate a test image
image = np.arange(65536).reshape((256, 256))

# Create an ImageNormalize object
norm = ImageNormalize(image, interval=MinMaxInterval(), stretch=SqrtStretch())

# or equivalently using positional arguments
# norm = ImageNormalize(image, MinMaxInterval(), SqrtStretch())

# Display the image
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
im = ax.imshow(image, origin='lower', norm=norm)
fig.colorbar(im)