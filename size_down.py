import cv2
import glob
import os

img_paths = glob.glob("./2022-04-05assistant/1/imgs/*.png")
img_paths.sort()

for img_path in img_paths:
	img = cv2.imread(img_path)
	img = cv2.resize(img, (960, 540))
	cv2.imwrite(img_path, img)
