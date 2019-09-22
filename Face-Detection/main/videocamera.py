import cv2
import time
from imutils.video  import VideoStream
vs=VideoStream(src=0).start()
time.sleep(1.0)
while True:
    image = vs.read()
    image = imutils.resize(image, width=400)

