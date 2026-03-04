import numpy as np

def atrous(img, kernel, rate, stride_h, stride_w, activation):
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
                img_out[y, x, c] = activation(np.sum(img[i - offset_h:i - offset_h + ((kh - 1) * rate) + 1:rate, 
                                              j - offset_w:j - offset_w + ((kw - 1) * rate) + 1:rate, 
                                              c] 
                                              * kernel))
            x += 1
        y += 1
    return img_out