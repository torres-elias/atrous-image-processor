import numpy as np

def absolute(img):
    return np.abs(img)

def histogram_expansion(img):
    max_value = img.max()
    min_value = img.min()

    img_out = (img - min_value) / (max_value - min_value) * 255

    return img_out