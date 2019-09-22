import numpy as np
import cv2

def order_pts(pts):
    #This function  order_pts takes a single argument, pts , which is a list of four points specifying the (x, y) coordinates of each point of the rectangle.
    rect=np.zeros((4,2),dtype="float32")
    sum_pts=pts.sum(axis=1)
    diff_pts=np.diff(pts,axis=1)
    #we’ll find the top-left point, which will have the smallest x + y sum, and the bottom-right point, which will have the largest x + y sum
    rect[0]=pts[np.argmin(sum_pts)]
    rect[2] = pts[np.argmax(sum_pts)]

    #now we’ll have to find the top-right and bottom-left points. Here we’ll take the difference (i.e. x – y) between the points
    #The coordinates associated with the smallest difference will be the top-right points, whereas the coordinates with the largest difference will be the bottom-left points
    rect[1] = pts[np.argmin(diff_pts)]
    rect[3] = pts[np.argmax(diff_pts)]

    return rect



