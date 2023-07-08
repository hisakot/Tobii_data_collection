import cv2
import glob
import os

# org_img_paths = glob.glob("../Dataset/surgery/org_imgs/7/*.png")
org_img_paths = "../Dataset/surgery/org_imgs/7/"
tool_paths = glob.glob("../ViT_MRCNN/output/tmp/color_mask/*.png")

for i, tool_path in enumerate(tool_paths):
    tool_img = cv2.imread(tool_path)
    png_name = os.path.basename(tool_path)
    org_img = cv2.imread(org_img_paths + png_name)
    print(org_img_paths + png_name)
    print(tool_path)

    org_img = cv2.resize(org_img, (480, 270))
    tool_img = cv2.resize(tool_img, (480, 270))

    blend_img = cv2.addWeighted(org_img, 1, tool_img, 0.4, 0)
    cv2.imwrite("../ViT_MRCNN/output/tmp/blend_img/" + str(i).zfill(6) + ".png", blend_img)
