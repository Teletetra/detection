import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)
cTime=0
pTime=0 

mpFaceDetection=mp.solutions.face_detection
mpDraw=mp.solutions.drawing_utils
faceDetection=mpFaceDetection.FaceDetection()
while True:
    success, frame =cap.read()
    if not success:
        break
    
    resized_frame=cv2.resize(frame,(0,0),fx=0.75,fy=0.75)
    resized_frameRGB=cv2.cvtColor(resized_frame,cv2.COLOR_BGR2RGB)
    results =faceDetection.process(resized_frameRGB)
    print(results)

    if results.detections:
        for id,detection in enumerate(results.detections):
            mpDraw.draw_detection(resized_frame,detection)
            #print(id,detection)
            #print(detection.score)
            print(detection.location_data.relative_bounding_box)
            bboxC= detection.location_data.relative_bounding_box
            ih ,iw ,ic = resized_frame.shape
            bbox =int(bboxC.xmin*iw),int(bboxC.ymin*ih), \
            int(bboxC.width*iw), int(bboxC.height*ih)
            cv2.rectangle(resized_frame,bbox,(255,0,0),2)
            cv2.putText(resized_frame, f"{int(detection.score[0]*100)}%",(bbox[0],bbox[1]-20),cv2.FONT_HERSHEY_PLAIN,
    2,(255,0,255),2)
 


    cTime=time.time()
    fps=1/(cTime-pTime) 
    pTime=cTime
    cv2.putText(resized_frame,f"FPS:{int(fps)}",(20,70),cv2.FONT_HERSHEY_PLAIN,
    3,(0,255,0),2)
    cv2.imshow("image",resized_frame)   
    cv2.waitKey(20)

cap.release()
cv2.destroyAllWindows()