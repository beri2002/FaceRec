from src.infrastructure.interfaces.ipreprocess import IPreProcess
import cv2

class PreProcess(IPreProcess):

    def __init__(self):
        pass

    def canny_edge_detect(self, image, lower_threshold=50, upper_threshold=150):
        # Perform Canny edge detection
        edges = cv2.Canny(image, lower_threshold, upper_threshold)
        return edges

    def gray_scale(self, image):
            # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_frame

    def resize(self, image, size=(640, 480)):
        # Resize the image
        resized_image = cv2.resize(image, size)
        return resized_image

    def blur(self, image, kernel_size=(5, 5), standard_deviation=0):
        # Apply Gaussian blur with a specified kernel size
        blurred_image = cv2.GaussianBlur(image, kernel_size, standard_deviation)
        return blurred_image
    
    def preprocess(self, image):
        image = self.gray_scale(image)
        image = self.resize(image)
        # image = self.canny_edge_detect(image)
        return image
