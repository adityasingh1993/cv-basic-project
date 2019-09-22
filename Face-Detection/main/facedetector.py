import numpy as np
import argparse
import cv2
import imutils
from imutils.video import VideoStream
import argparse
import time

ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
ap.add_argument("-p", "--prototxt", required=True,
	 help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
 	help="path to Caffe pre-trained model")
# ap.add_argument("-c", "--confidence", type=float, default=0.5,
# 	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

net=cv2.dnn.readNetFromCaffe(args["prototxt"],args["model"])
vs=VideoStream(src=0).start()
time.sleep(1.0)
while True:
    image=vs.read()
    image=imutils.resize(image,width=400)
    #image=cv2.imread(args["image"])
    (h,w)=image.shape[:2]
    blob=cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),1.0,(300,300),(104.0,177.0,123.0))
    net.setInput(blob)
    detections=net.forward()
    for i in range(0,detections.shape[2]):
        confidence=detections[0,0,i,2]
        print(confidence)

        #if confidence >args["confidence"]:
        if confidence > 0.5:
            print("Detections",detections)
            box=detections[0,0,i,3:7]*np.array([w,h,w,h])
            (startX,startY,endX,endY)=box.astype(int)
            text = "{:.2f}%".format(confidence * 100)
            if startY-10>10:
                y=startY-10
            else:
                y=startY+10
            cv2.rectangle(image,(startX,startY),(endX,endY),(0,0,255),2)
            cv2.putText(image,text,(startX,y),cv2.FONT_HERSHEY_COMPLEX,0.45,(0,0,255),2)
    cv2.imshow("output",image)
    key = cv2.waitKey(1) & 0xFF


        # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    # if we are using a webcam, release the pointer
if not args.get("video", False):
    vs.stop()

    # otherwise, release the file pointer
else:
    vs.release()

    # close all windows
cv2.destroyAllWindows()

