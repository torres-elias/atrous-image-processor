import numpy as np

import image_io
import atrous as at
img = image_io.load("atrous-image-processor\\images\\Shapes.png")

kernel = np.array([[1/25,1/25,1/25,1/25,1/25],
                   [1/25,1/25,1/25,1/25,1/25],
                   [1/25,1/25,1/25,1/25,1/25], 
                   [1/25,1/25,1/25,1/25,1/25],
                   [1/25,1/25,1/25,1/25,1/25]])
img_out = at.atrous(img, kernel, 2, 1, 1)

print(img_out.shape)

image_io.save(img_out, path)