from PIL import Image
import  pytesseract
import argparse
import cv2
import  os

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path To Image File")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
text = pytesseract.image_to_string(image)

print(text)
