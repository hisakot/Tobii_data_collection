import cv2
import numpy as np
import os
from scipy import ndimage
import glob

GAZE_CSV = "main20170707/gaze_interpolation.csv"

gaze_points = np.loadtxt(GAZE_CSV, delimiter=",", skiprows=1, usecols=(1, 2))

for i, gaze_point in enumerate(gaze_points):
	gaze_point *= np.array([320, 180])
	if gaze_point[0] == 0 and gaze_point[1] == 0:
		gaze_point = np.array([1, 1]) + gaze_point
	gaze_x = gaze_point[0]
	gaze_y = gaze_point[1]
	gazemap = np.zeros((180, 320))
	gazemap[int(round(gaze_y)) - 1][int(round(gaze_x)) - 1] = 1
	gazemap = ndimage.filters.gaussian_filter(gazemap, 15)
	gazemap -= np.min(gazemap)
	gazemap /= np.max(gazemap)
	gazemap *= 255
	gazeim = cv2.resize(gazemap, (224,224), interpolation=cv2.INTER_AREA)
	cv2.imwrite("main20170707/gaze_range/" + str(i+1).zfill(6) + ".png", gazeim)
