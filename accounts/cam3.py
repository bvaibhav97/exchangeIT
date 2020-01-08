import numpy as np
import cv2

webcam = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
ret,frame = webcam.read() # return a single frame in variable `frame`

while(True):
	cv2.imshow("cap",frame) #display the captured image
	key = cv2.waitKey(114)
	
	if key == ord('s'):
		cv2.imwrite(filename='saved_img.jpg', img=frame)
		print("Processing image...")
		img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
		
		img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
		print("Image saved!")
		break

	elif key == ord('q'):
		webcam.release()
		cv2.destroyAllWindows()
		break

webcam.release()