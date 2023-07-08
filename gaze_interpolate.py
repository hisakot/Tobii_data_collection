import csv
import cv2
import glob
import numpy as np
import os
import statistics
from tqdm import tqdm

DIR_PATH = "E:/2022-04-22DrHayashida/"

gazes = np.loadtxt(DIR_PATH + "gaze.csv", delimiter=",", skiprows=1, usecols=(1, 2))

itp_gaze = list()
before_zero = False
start_frame = 1
for i, gaze in enumerate(gazes):
    if before_zero == True:
        if gaze[0] == 0 and gaze[1] == 0:
            continue
        else:
            if len(itp_gaze) == 0:
                post_x = 0
                post_y = 0
            else:
                post_x = itp_gaze[-1]["x"]
                post_y = itp_gaze[-1]["y"]
            current_frame = i + 1
            dx = (gaze[0] - post_x) / (current_frame - start_frame + 1)
            dy = (gaze[1] - post_y) / (current_frame - start_frame + 1)
            for j in range(current_frame - start_frame + 1):
                x = post_x + dx * (j + 1)
                y = post_y + dy * (j + 1)
                itp_gaze.append({"frame" : start_frame + j, "x" : x, "y" : y})
            before_zero = False
    else:
        if gaze[0] == 0 and gaze[1] == 0:
            before_zero = True
            start_frame = i + 1
        else:
            itp_gaze.append({"frame" : i+1, "x" : gaze[0], "y" : gaze[1]})
        
field_names = ["frame", "x", "y"]
with open(DIR_PATH + "gaze_interpolate.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(itp_gaze)
