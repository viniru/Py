import cv2
im = cv2.imread("smallgray.png",1)
print(im)

cv2.imwrite("newsmallgrey.png",im)
