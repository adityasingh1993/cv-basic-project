from FourPointTransform import *
import numpy as np
import cv2
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="path to image file")
ap.add_argument("-c","--cord",help="four cordinate points of image")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])
coord=np.array(eval(args["cord"]),dtype=float)

wraped=four_pont_transform(image,coord)
cv2.imshow("original",image)
cv2.imshow("wraped",wraped)
cv2.waitKey(0)

#test code ==>python Test.py --image example_02.png --cord "[(73, 239), (356, 117), (475, 265), (187, 443)]"
# Error was coming because dtype of rect and dist was in float , change it to float32