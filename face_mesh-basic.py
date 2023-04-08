import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)
cTime=0
pTime=0

mpDraw=mp.solutions.drawing_utils
mpFaceMesh=mp.solutions.face_mesh
faceMesh=mpFaceMesh.FaceMesh(max_num_faces=2)


while True:
    success, frame=cap.read()
    if not success:
        break
    resized_frame=cv2.resize(frame,(0,0),fx=0.75,fy=0.75)
    resized_frameRGB=cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    results=faceMesh.process(resized_frameRGB)
    print(results)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(resized_frame,faceLms, mpDraw.FACEMESH_TESSELATION)
            
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime 
    cv2.putText(resized_frame,f"FPS:{int(fps)}",(20,70),cv2.FONT_HERSHEY_PLAIN,
    3,(0,255,0),3)
    cv2.imshow("image",resized_frame)
    cv2.waitKey(1)

