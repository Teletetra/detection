import sys
import cv2
import time 
import mediapipe as mp

class handDetector():
    def __init__(self,mode=False, maxHands=2 , detectionCon=8.5, trackCon=8.5 ):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mphand=mp.solutions.hands
        self.hands=self.mphand.Hands( self.trackCon,self.mode, self.maxHands,self.detectionCon,)
        self.mpDraw = mp.solutions.drawing_utils
    
    
    def findHands(self,img,draw=True):
    # Convert the color space of the image from BGR to RGB, which is required by the mediapipe library
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Use the Hands.process() method to detect and track hands in the image
        self.results= self.hands.process(imgRGB)

    #print(results.multi_hand_landmarks)
    # If at least one hand is detected in the image    
        if self.results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlms , self.mphand.HAND_CONNECTIONS )
        return img         
    

    def findPostion(self,img,handNo=0, draw=_True_):
        lmList =[]
        if results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
               #  print(id,lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
        #    if id ==0:
                cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)

        
    # Display the image with landmarks and connections drawn on it   
''' cTime= time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(10,70,),cv2.FONT_HERSHEY_PLAIN,3,
                     (255,0,255),3  )
    cv2.imshow("image", img)
    # Wait for a key event for 1 millisecond before continuing the loop
    cv2.waitKey(1)
'''


def main():
    pTime=0
    cTime=0
    #loopover frames from the webcane video stream
    cap=cv2.VideoCapture(0)
    while True:
      #read the next frame from the webcame
        success, img = cap.read()
        img = detector.findHands(img)
        cTime= time.time()
        fps=1/(cTime-pTime)
        pTime=cTime

        cv2.putText(img,str(int(fps)),(10,70,),cv2.FONT_HERSHEY_PLAIN,3,
                     (255,0,255),3  )
    cv2.imshow("image", img)
    # Wait for a key event for 1 millisecond before continuing the loop
    cv2.waitKey(1)  
    

