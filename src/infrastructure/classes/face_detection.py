from src.infrastructure.interfaces.iface_detection import IFaceDetection
import cv2

class FaceDetection(IFaceDetection):
    def __init__(self, CascadeClassifier, scaleFactor=1.1, minNeighbors=5):
        # Loading the required haar-cascade xml classifier file 
        self._haar_cascade = cv2.CascadeClassifier('/home/yossef/Documents/PROJECTS/FaceRec/assets/haarcascade_frontalface_default.xml')
        self._scaleFactor = scaleFactor
        self._minNeighbors = minNeighbors

    def Detect(self, gray_img):
        # Applying the face detection method on the grayscale image 
        faces_rect = self._haar_cascade.detectMultiScale(gray_img, self._scaleFactor, self._minNeighbors)
        return faces_rect