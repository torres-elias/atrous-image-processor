from PIL import Image
import numpy as np

def load(path):
    img = Image.open(path)
    return np.array(img)

def save(image, path):
    img = Image.fromarray(image)
    img.save(path)