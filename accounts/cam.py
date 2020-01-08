import cv2
import tkinter as tk

cap = cv2.VideoCapture(0)

while(True):

    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    ret,frame = cap.read() # return a single frame in variable `frame`
    key = cv2.waitKey(1)

    
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 