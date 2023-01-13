import cv2
import numpy as np
import math

capture = cv2.VideoCapture(0)
while(capture.isOpened()):
    # read image
    ret, img = capture.read()

    # get hand data from the rectangle sub window on the screen
    cv2.rectangle(img, (100,100), (300,300), (0,0,255),0)
    crop_img = img[100:300, 100:300]

    # convert to grayscale
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    # applying gaussian blur
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)

    # thresholdin: Otsu's Binarization method
    _, thresh1 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # check OpenCV version to avoid unpacking error
    (version, _, _) = cv2.__version__.split('.')
 
    contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # find contour with max area
    hand = max(contours, key = lambda x: cv2.contourArea(x))    

    # finding convex hull around the hand
    hull = cv2.convexHull(hand)

    #define areas of hull and hand
    ar_hull = cv2.contourArea(hull)
    ar_hand = cv2.contourArea(hand)

    #ratio of area covered other than hand
    ar_rest = ((ar_hull-ar_hand)/ar_hand)*100

    # finding convexity defects
    hull = cv2.convexHull(hand, returnPoints=False)
    defects = cv2.convexityDefects(hand, hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (255, 0, 0), 3)

    # applying Cosine Rule to find angle for all defects (between fingers)
    # with angle > 90 degrees and ignore defects
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]

        start = tuple(hand[s][0])
        end = tuple(hand[e][0])
        far = tuple(hand[f][0])
        pt = (100,180)

        # find length of all sides of triangle
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))

        #distance between convexHull and the point
        distance = (2*area)/a

        # apply cosine rule
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

        # ignore angles > 90 and highlight rest with red dots
        if angle <= 90 and distance >30:
            count_defects += 1
            cv2.circle(crop_img, far, 1, [0,0,255], -1)
        #dist = cv2.pointPolygonTest(hand,far,True)

        # draw a line from start to end i.e. the convex points (finger tips)
        cv2.line(crop_img,start, end, [0,255,0], 2)
        #cv2.circle(crop_img,far,5,[0,0,255],-1)

    count_defects += 1

    # define actions required
    font = cv2.FONT_HERSHEY_SIMPLEX
    if count_defects==1:
        if ar_rest<12:
                cv2.putText(img,"ZERO", (0,50), font, 2, (255,0,0), 2)
        else:
            cv2.putText(img,"ONE", (0,50), font, 2, (255,0,0), 2)

    elif count_defects==2:
        cv2.putText(img, "TWO", (0, 50), font, 2, (255,0,0), 2)
        
    elif count_defects==3:
        cv2.putText(img,"THREE", (0, 50), font, 2, (255,0,0), 2)
        
    elif count_defects==4:
        cv2.putText(img,"FOUR", (0, 50), font, 2, (255,0,0), 2)

    elif count_defects==5:
        cv2.putText(img,"FIVE", (0,50), font, 2, (255,0,0), 2)
        
    else:
        cv2.putText(img,"Place hand properly inside the box!", (0, 50), font, 2, (0,0,255), 2)

    # show appropriate images in windows
    cv2.imshow('Gesture', img)
    cv2.imshow('Thresholded', thresh1)
    cv2.imshow('Contour', crop_img)

    k = cv2.waitKey(4)
    if k == 27:
        break

cv2.destroyAllWindows()
capture.release()
        
