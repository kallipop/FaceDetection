import cv2
import time

camera = cv2.VideoCapture(0)

prev_frame_time =time.time()

detect = True

if not camera.isOpened():
    print("Cannot open camera")
    exit()
    
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

while True:
    success , frame = camera.read()
    
    if not success:
        print("Cannot receive frame")
        break
    
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.putText(frame,"D: Toggle Detection | S: Screenshot | Q: Quit",(150,470),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
    
    if detect:
        face = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=8)
        for(x,y,w,h) in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(127,0,255),2)
    
        cv2.putText(frame,f"Faces detected: {len(face)}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    
        if len(face) >0:
               cv2.putText(frame,"Status: Face detected",(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        else:
            cv2.putText(frame,"Status: No Face detected",(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    else: 
        cv2.putText(frame,"Face detection: OFF",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,160,255),2)
        
    
    new_frame_time = time.time()
    
    fps = 1/(new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    
    fps = int(fps)
    cv2.putText(frame,f"FPS: {fps}",(20,450),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),2)


  
    cv2.imshow("My camera", frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("screenshot.png",frame)
    elif key ==ord('d'):
        detect= not detect
    
camera.release()
cv2.destroyAllWindows()