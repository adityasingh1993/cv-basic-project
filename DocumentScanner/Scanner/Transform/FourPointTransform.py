import cv2
import numpy as np
from Transform.ImageTransform import *
def four_pont_transform(image,pts):
    rect=order_pts(pts)
    (tl,tr,br,bl)=rect
    widthA=np.sqrt((br[0]-bl[0])**2+(br[1]-bl[1])**2)
    widthB = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)

    maxWidth=max(int(widthA),int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    print(heightB,"===<Bjj")
    print(heightA, "===<A")
    #maxHeight=max(int(heightA),int(heightB))
    #Here, we define 4 points representing our “top-down” view of the image. The first entry in the list is (0, 0)  indicating the top-left corner.
    # The second entry is (maxWidth - 1, 0)  which corresponds to the top-right corner.
    # Then we have (maxWidth - 1, maxHeight - 1)  which is the bottom-right corner. Finally, we have (0, maxHeight - 1)  which is the bottom-left corner.
    dst=np.array([[0,0],[maxWidth-1,0],[maxWidth-1,maxHeight-1],[0,maxHeight-1]],dtype="float32")
    print("rect===>",rect)
    print("dits===>",dst)
    #To actually obtain the top-down, “birds eye view” of the image we’ll utilize the cv2.getPerspectiveTransform
    #This function requires two arguments, rect , which is the list of 4 ROI points in the original image, and dst ,
    # which is our list of transformed points. The cv2.getPerspectiveTransform  function returns M , which is the actual transformation matrix.
    M=cv2.getPerspectiveTransform(rect,dst)

    #We apply the transformation matrix on Line 61 using the cv2.warpPerspective  function. We pass in the image ,

    # our transform matrix M , along with the width and height of our output image
    #The output of cv2.warpPerspective  is our warped  image, which is our top-down view
    warped=cv2.warpPerspective(image,M,(maxWidth,maxHeight))

    return  warped