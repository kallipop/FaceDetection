import cv2

camera = cv2.VideoCapture(0)

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
    
    face = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=8)
    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(127,0,255),2)
    
    cv2.putText(frame,f"Faces detected: {len(face)}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(127,0,255),2)
    
    if len(face) >0:
           cv2.putText(frame,"Status: Face detected",(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(127,0,255),2)
    else:
        cv2.putText(frame,"Status: No Face detected",(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(127,0,255),2)
    
    cv2.imshow("My camera", frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("screenshot.png",frame)
    
camera.release()
cv2.destroyAllWindows()