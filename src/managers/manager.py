from src.infrastructure.classes.face_detection import FaceDetection
from src.infrastructure.classes.postprocess import PostProcess
from src.infrastructure.classes.preprocess import PreProcess
from src.infrastructure.classes.video_handler import VideoHandler
from src.managers.config_manager import ConfigManager

import cv2
import time

class Manager():
    def __init__(self, configPath="config/config.json"):
        self._config_manager = ConfigManager(configPath)
        config_data = self._config_manager.read_config()
        self._preprocess = PreProcess()
        self._postprocess = PostProcess()
        self._video_handler = VideoHandler(config_data["VideoHandler"]["videoSource"]) 
        self._face_detection = FaceDetection(config_data["FaceDetection"]["CascadeClassifier"], scaleFactor=1.2, minNeighbors=9)

    def detect_frame(self):
        start = time.time()
        ret, frame = self._video_handler.read_frame()

        if not ret:
            print("ret is false")
            return

        # Preprocess
        gray = self._preprocess.preprocess(frame)

        # Detect
        faces = self._face_detection.Detect(gray)

        # Postprocess
        self._postprocess.postprocess(faces, gray)

        self._video_handler.show_video(gray)

        end = time.time()
        time_difference = end - start
        fps = 1 / time_difference

        # Display the FPS along with the time taken
        print("Time:", round(time_difference * 1000, 2), "milliseconds")
        print("FPS:", round(fps, 2))


    def detect_video(self):
        while True:
            self.detect_frame()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self._video_handler.__del__()

