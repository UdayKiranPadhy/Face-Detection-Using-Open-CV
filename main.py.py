import cv2 
import warnings
warnings.filterwarnings("ignore")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('lena.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret , frame = cap.read()
    frame=cv2.flip(frame, 1)
    faces = face_cascade.detectMultiScale(frame,1.1,4)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()