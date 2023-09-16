import os
import cv2
# importing io from skimage
import skimage
from skimage import io
import matplotlib
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from skimage import data
import numpy as np
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.filters import threshold_otsu
from skimage import data, segmentation, color
from skimage import graph
from matplotlib import pyplot as plt

from math import sqrt
from skimage.feature import canny


file = os.path.join(skimage.data_dir, '/Users/dylanconnolly/Desktop/IMG_6799.jpg')
image = io.imread(file)
image = skimage.color.rgb2gray(image)
thresh = threshold_otsu(image)
binary = image > thresh

# fig, axes = plt.subplots(ncols=4, figsize=(8, 2.5))
# ax = axes.ravel()
# ax[0] = plt.subplot(1, 3, 1)
# ax[1] = plt.subplot(1, 3, 2)
# ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])
#
# ax[0].imshow(image, cmap=plt.cm.gray)
# ax[0].set_title('Original')
# ax[0].axis('off')
#
# # ax[1].hist(image.ravel(), bins=256)
# # ax[1].set_title('Histogram')
# # ax[1].axvline(thresh, color='r')
#
# ax[1].imshow(binary, cmap=plt.cm.gray)
# ax[1].set_title('Thresholded')
# ax[1].axis('off')
#
edges = skimage.filters.sobel(image)
# ax[2].imshow(edges, cmap=plt.cm.gray)
# ax[2].set_title('idk')
# ax[2].axis('off')

plt.show()
skimage.io.imshow(edges)
skimage.io.show()
#
# def to_gray_uint(image):
#     return np.uint8((image) * 255)
#
#
# img = cv2.imread('/Users/dylanconnolly/Desktop/IMG_6799.jpg')
# print(img)

# converting image into grayscale image
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = to_gray_uint(skimage.color.gray2rgb(image))
# gray = cv2.cvtColor(to_gray_uint(skimage.color.gray2rgb(image)), cv2.COLOR_BGR2GRAY)
#
# # setting threshold of gray image
# _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#
# # using a findContours() function
# contours, _ = cv2.findContours(
#     threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# i = 0
#
# # list for storing names of shapes
# for contour in contours:
#
#     # here we are ignoring first counter because
#     # findcontour function detects whole image as shape
#     if i == 0:
#         i = 1
#         continue
#
#     # cv2.approxPloyDP() function to approximate the shape
#     approx = cv2.approxPolyDP(
#         contour, 0.01 * cv2.arcLength(contour, True), True)
#
#     # using drawContours() function
#     cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
#
#     # finding center point of shape
#     M = cv2.moments(contour)
#     if M['m00'] != 0.0:
#         x = int(M['m10'] / M['m00'])
#         y = int(M['m01'] / M['m00'])
#
#     # putting shape name at center of each shape
#     if len(approx) == 3:
#         cv2.putText(img, 'Triangle', (x, y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
#
#     elif len(approx) == 4:
#         cv2.putText(img, 'Quadrilateral', (x, y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
#
#     elif len(approx) == 5:
#         cv2.putText(img, 'Pentagon', (x, y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
#
#     elif len(approx) == 6:
#         cv2.putText(img, 'Hexagon', (x, y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
#
#     else:
#         cv2.putText(img, 'circle', (x, y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
#
# # displaying the image after drawing contours
# cv2.imshow('shapes', img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
