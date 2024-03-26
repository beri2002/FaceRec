from abc import ABC, abstractmethod

class IFaceDetection(ABC):

    @abstractmethod
    def Detect(self, gray_img):
        pass
