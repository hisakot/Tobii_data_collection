import csv
import cv2
import glob
import numpy as np
import os
import statistics
from tqdm import tqdm

TOBII = 2
DIR_PATH = "../20220823_main/"

org_imgs = DIR_PATH +  "org_imgs/*.png"
img_paths = glob.glob(org_imgs)
img_paths.sort()

gazes = np.loadtxt(DIR_PATH + "gaze.csv", delimiter=",", skiprows=1, usecols=(1, 2))
gazes *= np.array((960, 540))

# CSV = "E:/2022-06-28assistantMrHayashida/gaze_med.csv"
label = ["frame", "x", "y"]
data = list()

def median(gazes, i):
	count = 0
	x_list = list()
	y_list = list()
	while count < 4:
		gaze_x = int(gazes[i * 4 + count][0])
		gaze_y = int(gazes[i * 4 + count][1])
		count += 1
		if gaze_x != 0 and gaze_y != 0:
			x_list.append(gaze_x)
			y_list.append(gaze_y)

	if len(x_list) == 0 and len(y_list) == 0:
		return (0, 0)
	med_x = statistics.median(x_list)
	med_y = statistics.median(y_list)
	med_gaze = (int(med_x), int(med_y))

	return med_gaze

i = 0
for img_path in tqdm(img_paths):
	img = cv2.imread(img_path)
	org_img = cv2.resize(img, (960, 540))
	
# gaze = (int(gazes[i * 4][0]), int(gazes[i * 4][1]))
	if TOBII == 3:
		gaze = median(gazes, i)
	elif TOBII == 2:
		gaze = (int(gazes[i][0]), int(gazes[i][1]))
	gaze_data = {"frame" : i+1, "x" : gaze[0], "y" : gaze[1]}
	data.append(gaze_data)

# 	cv2.drawMarker(blend_img, gaze, (0, 0, 255),
# 		       markerType=cv2.MARKER_CROSS, markerSize=50,
# 		       thickness=5, line_type=cv2.LINE_8)
	# blend transparent red circle
	if gaze[0] == 0 and gaze[1] == 0:
		blend_img = org_img
	else:
		circle_img = np.zeros((540, 960, 3), np.uint8)
		cv2.circle(circle_img, gaze, radius=30, color=(0, 255, 0), thickness=3)
		blend_img = cv2.addWeighted(org_img, 1, circle_img, 0.85, 0)

	cv2.imwrite(DIR_PATH + "gaze_blend/" + os.path.basename(img_path), blend_img)
	i += 1

if TOBII == 3:
	with open(CSV, "w", newlinr="") as f:
		writer = csv.DictWriter(f, fieldnames=label)
		writer.writeheader()
		write.writerows(data)

