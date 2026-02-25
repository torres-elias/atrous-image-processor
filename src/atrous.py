import numpy as np

def atrous(img, kernel, rate, stride_h, stride_w):
    h, w = img.shape[0], img.shape[1]
    kh, kw = kernel.shape[0], kernel.shape[1]
    
    offset_h = rate * (kh // 2)
    offset_w = rate * (kw // 2)

    out_h = len(range(offset_h, h - offset_h, stride_h))
    out_w = len(range(offset_w, w - offset_w, stride_w))
    img_out = np.zeros([out_h, out_w, 3])

    y, x = 0, 0
    for i in range(offset_h, h - offset_h, stride_h):
        x = 0
        for j in range(offset_w, w - offset_w, stride_w):
            for c in range(3):
                img_out[y, x, c] = 255 # TODO: implementar correlação atrous
            
            x += 1
        y += 1