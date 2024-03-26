from abc import ABC, abstractmethod

class IPreProcess(ABC):

    @abstractmethod
    def canny_edge_detect(self, image):
        pass

    @abstractmethod
    def gray_scale(self, image):
        pass

    @abstractmethod
    def resize(self, image):
        pass

    @abstractmethod
    def blur(self, image):
        pass