import cv2
from glob import glob
import numpy as np
import os

n = 2

for i in range(40):
	img = cv2.imread("E:/2022-04-05MrHayashida/org_imgs/" + str(n + 3000 * i).zfill(6) + ".png")
	cv2.imwrite("./scene/" + str(n + 3000 * i).zfill(6) + ".png", img)
