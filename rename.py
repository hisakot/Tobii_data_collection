import glob
import os

import cv2

img_paths = glob.glob("../MaskRCNN_semi_supervised/output/blend_img/*.png")
for i, img_path in enumerate(img_paths):
    img = cv2.imread(img_path)
    cv2.imwrite("../MaskRCNN_semi_supervised/output/blend_img_rename/" + str(i) + ".png", img)
