import cv2
import numpy as np
from pyzbar.pyzbar import decode
#import sys
#import time

#img = cv2.imread('Image/1.png')
cap = cv2.VideoCapture(1)
cap.set(3,200)
cap.set(4,200)

with open('myDatafile.text') as f:
    myDatalist = f.read().splitlines()


while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDatalist:
            myOutput = 'Authorized'
            myColor = (0,255,0)

        else:
            myOutput = 'Un-Authorized'
            myColor = (0,0,255)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 2)
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (0, 255, 0), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(1)