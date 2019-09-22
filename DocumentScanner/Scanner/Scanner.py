from Transform.FourPointTransform import *
from skimage.filters import threshold_local
import numpy as np
import cv2
import  argparse
import imutils

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path To Image File")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
ratio=image.shape[0]/500
orig=image.copy()
image=imutils.resize(image,height=500)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(image,(5,5),0)
edged=cv2.Canny(gray,75,100)
# cv2.imshow("orginal",orig)
# cv2.imshow("gray",gray)
# cv2.imshow("edge",edged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cnts=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:5]
screencnts=None
approxlist=[]
approxlenlist=[]
for c in cnts:
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*peri,True)
    approxlist.append(approx)
    approxlenlist.append(len(approx))

    print("approx==>",approx)
    if len(approx)==2:
        screencnts=approx
        break
index=approxlenlist.index(max(approxlenlist))
screencnts=approxlist[index]
print("max of screen===>",index)
print("screen counts==>",screencnts)
#cv2.drawContours(image,[screencnts],-1,(0,255,0),2)
cv2.imshow("outline",image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

print(screencnts.shape)
warped=four_pont_transform(orig,screencnts.reshape(10,2)*ratio)
warped=cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
T=threshold_local(warped,13,"gaussian",8)
warped=(warped>T).astype("uint8")*255
cv2.imshow("warped",warped)
cv2.waitKey(0)
cv2.destroyAllWindows()