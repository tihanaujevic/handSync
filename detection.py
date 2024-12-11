import cvzone
import cv2
import math

cap = cv2.VideoCapture(0)
detector = cvzone.HandDetector(maxHands=1, detectionCon=1)
mySerial= cvzone.SerialObject("COM3", 9600, 1)

def Distance(p1,p2, lmList):
    x1, y1 = lmList[p1][1], lmList[p1][2]
    x2, y2 = lmList[p2][1], lmList[p2][2]
    length = math.hypot(x2 - x1, y2 - y1)
    return length


while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmList, bbox = detector.findPosition(img) 

    start_point = (150, 80)
    end_point = (500, 400)
    color = (255, 0, 0)
    thickness = 2

    cv2.rectangle(img, start_point, end_point, color, thickness)
    fingers = []

    if lmList:
        
        #thumb 120-215
        lengthThumb = Distance(0,4,lmList)
        if lengthThumb < 150:
            fingers.append(0)
        else:
            fingers.append(2)

        #index 70-150-280
        lengthIndex = Distance(0,8,lmList)
        if lengthIndex > 260:
            fingers.append(2)
        elif lengthIndex > 130:
            fingers.append(1)
        else:
            fingers.append(0)
        
        #middle
        lengthMiddle = Distance(0,12,lmList)
        if lengthMiddle > 260:
            fingers.append(2)
        elif lengthMiddle > 140:
            fingers.append(1)
        else:
            fingers.append(0)

        #ring 60-140-250
        lengthRing = Distance(0,16,lmList)
        if lengthRing > 240:
            fingers.append(2)
        elif lengthRing > 140:
            fingers.append(1)
        else:
            fingers.append(0)

        #pinky
        lengthPinky = Distance(0,20,lmList)
        if lengthPinky > 230:
            fingers.append(2)
        elif lengthRing > 130:
            fingers.append(1)
        else:
            fingers.append(0)
        
        print(fingers)


        mySerial.sendData(fingers)
    cv2.imshow("image", img)
    cv2.waitKey(1)