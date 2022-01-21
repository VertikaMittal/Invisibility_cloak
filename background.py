#opencv for image processing
import cv2

#creating a videocapture object

cap = cv2.VideoCapture(0) #this is my webcam

#getting the background image
while cap.isOpened():
    ret, background = cap.read() #simply reading from the web cam
    if ret:
        cv2.imshow("Capture", background)
        if cv2.waitKey(5) == ord('q'):
            #save the background image
            cv2.imwrite("image.jpg",background)
            break
cap.release()
cv2.destroyAllWindows()

