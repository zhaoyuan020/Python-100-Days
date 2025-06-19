# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os.path
# 读取图片
img_path = "D:\\shipinchouzhen\\1.png"           #  D:\shipinchouzhen
img = Image.open(img_path)

# 图像转化为numpy数组
img = np.asarray(img)
flat = img.flatten()

# 创建函数
def get_histogram(image, bins):
    # array with size of bins, set to zeros
    histogram = np.zeros(bins)
    # loop through pixels and sum up counts of pixels
    for pixel in image:
        histogram[pixel] += 1
    # return our final result
    return histogram

# execute our histogram function
hist = get_histogram(flat, 256)

# execute the fn
cs = np.cumsum(hist)

# numerator & denomenator
nj = (cs - cs.min()) * 255
N = cs.max() - cs.min()

# re-normalize the cumsum
cs = nj / N

# cast it back to uint8 since we can't use floating point values in images
cs = cs.astype('uint8')

# get the value from cumulative sum for every index in flat, and set that as img_new
img_new = cs[flat]

# put array back into original shape since we flattened it
img_new = np.reshape(img_new, img.shape)

# set up side-by-side image display
fig = plt.figure()
fig.set_figheight(15)
fig.set_figwidth(15)

# display the real image
fig.add_subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Image 'Before' Contrast Adjustment")

# display the new image
fig.add_subplot(1, 2, 2)
plt.imshow(img_new, cmap='gray')
plt.title("Image 'After' Contrast Adjustment")
filename = os.path.basename(img_path)

# plt.savefig("D:\\" + filename)
plt.show()