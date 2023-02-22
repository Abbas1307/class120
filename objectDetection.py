import cv2
import time
import math

video =cv2.VideoCapture("bb3.mp4")

# 1. loading tracker
tracker=cv2.TrackerCSRT_create()

# 2. read the first frame of the video
returned,img= video.read()

# 3. select the bounding box on the image(roi region of interset) 
bbox=cv2.selectROI("tracker",img,False)

# 4. Intilize the tracker on the image and the bbox
tracker.init(img,bbox)

print("what is bbox: ",bbox)

pt1=527
pt2=300

xps=[]
yps=[]

# tracker for goal
def trackingPosition(img,bbox):
# cv2 circle method used to make goal point
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.circle(img,(pt1,pt2),3,(0,0,255),4)
    
    c1=x+int(w/2)
    c2=y+int(h/2)

    cv2.circle(img,(c1,c2),3,(0,255,0),4)

    #distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    #x2=c1,x1=pt1,y2=c2,y1=pt2
    distance=math.sqrt((c1-pt1)**2+(c2-pt2)**2)
    print(distance)
    if distance<=30:
        cv2.putText(img,"goal has been reached",(500,400),cv2.FONT_HERSHEY_COMPLEX,0.7,(20,44,67),4)

    xps.append(c1)
    yps.append(c2)
    for i in range(len(xps)-1):
        if distance>=30:

            cv2.circle(img,(xps[i],yps[i]),2,(35,0,69),4)
        

def drawBox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,255,0),3,1)

while True:
    dummy,img= video.read()

    # 5. update the tracker on the image and bbox
    success,bbox=tracker.update(img)
    
    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img,"Lost the tracker",(200,200),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)
    trackingPosition(img,bbox)
    cv2.imshow("result",img)

    key=cv2.waitKey(25)

    if key ==32:
        print("stopped")
        break 

video.release()
cv2.destroyAllWindows()

 
 


