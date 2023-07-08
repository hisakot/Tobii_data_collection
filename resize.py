import cv2
import os
import glob
from tqdm import tqdm

dirs = ["20170707_main", "20200214_1_main", "20200214_2_main",
        "20220405assistant", "20220422DrHayashida",
        "20220628mainDrIshikawa", "20220715mainDrSeki", "20220823_main"]

for name in dirs:
    img_dir = "E:/" + name + "/org_imgs/*.png"
    img_files = glob.glob(img_dir)
    print(name)
    for img_file in tqdm(img_files):
        img = cv2.imread(img_file)
        img = cv2.resize(img, (480, 270))
        cv2.imwrite(img_file, img)

def change_size(image):
    binary_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image2 = cv2.threshold(binary_image, 15, 255, cv2.THRESH_BINARY)
    binary_image2 = cv2.medianBlur(binary_image2, 19)  # filter the noise, need to adjust the parameter based on the dataset
    x = binary_image2.shape[0]
    y = binary_image2.shape[1]

    edges_x = []
    edges_y = []
    for i in range(x):
        for j in range(10,y-10):
            if binary_image2.item(i, j) != 0:
                edges_x.append(i)
                edges_y.append(j)
    
    if not edges_x:
        return image

    left = min(edges_x)  # left border
    right = max(edges_x)  # right
    width = right - left  
    bottom = min(edges_y)  # bottom
    top = max(edges_y)  # top
    height = top - bottom  
    if width == 0 or height == 0:
        return image

    pre1_picture = image[left:left + width, bottom:bottom + height]  

    #print(pre1_picture.shape) 
    
    return pre1_picture  

dir_names = [7, 37, 40, 54, 56, 70]
for dir_name in dir_names:

    dir_name = str(dir_name)
    image_names = glob.glob("../cholec80/frame/" + dir_name + "/*.jpg")
    image_names.sort()

    for i, image_name in enumerate(image_names):
        image = cv2.imread(image_name)
        dim = (int(image.shape[1]/image.shape[0]*300), 300)
        image = cv2.resize(image, dim)
        image = change_size(image)
        image = cv2.resize(image, (250, 250))
        cv2.imwrite("../cholec80/frame/" + dir_name + "/" + str(i) + ".jpg", image)
        print("save " + dir_name + ": " + str(i))
