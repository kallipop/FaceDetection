import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened:
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
        
    
    cv2.imshow("My camera", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
camera.release()
cv2.destroyAllWindows()