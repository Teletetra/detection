import sys
import cv2
import time 
import mediapipe as mp

# Create a videocapture object to capture video from the deefalt camera
cap=cv2.VideoCapture(0)

#Create instances of the hands and drawin_utils classes from the mediapipe library
mphand=mp.solutions.hands
hands=mphand.Hands(  )
mpDraw = mp.solutions.drawing_utils

pTime=0
cTime=0
#loopover frames from the webcane video stream
while True:
    #read the next frame from the webcame
    success, img = cap.read()
    # Convert the color space of the image from BGR to RGB, which is required by the mediapipe library
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Use the Hands.process() method to detect and track hands in the image
    results= hands.process(imgRGB)

    #print(results.multi_hand_landmarks)
    # If at least one hand is detected in the image    
    if results.multi_hand_landmarks:
        # Loop over the landmarks and connections of each detected hand
        for handlms in results.multi_hand_landmarks:
            # Draw the landmarks and connections on the image using the drawing_utils.draw_landmarks() method
            for id, lm in enumerate(handlms.landmark):
    #            print(id,lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
               # if id ==0:
                cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)


            mpDraw.draw_landmarks(img, handlms , mphand.HAND_CONNECTIONS )
    # Display the image with landmarks and connections drawn on it   
    cTime= time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(10,70,),cv2.FONT_HERSHEY_PLAIN,3,
                     (255,0,255),3  )
    cv2.imshow("image", img)
    # Wait for a key event for 1 millisecond before continuing the loop
    cv2.waitKey(1)  

