from src.infrastructure.interfaces.ivideo_handler import IVideoHandler
import cv2

class VideoHandler(IVideoHandler):
    def __init__(self, videoSource=0):
        self._videoSource = videoSource
        self._cap = self.get_video()

    def get_video(self):
        # Open a video capture object (0 for default camera)
        cap = cv2.VideoCapture(self._videoSource)
        return cap

    def read_frame(self):
        # Read a frame from the camera
        ret, frame = self._cap.read()
        if not ret:
            return ret, None
        
        return ret, frame

    def get_video_properties(self):
        # Get video properties
        width = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = self._cap.get(cv2.CAP_PROP_FPS)

        return width, height, fps

    def show_video(self, frame, title="Video"):
        # Display the frame
        cv2.imshow(title, frame)        

    def __del__(self):
        # Release the video capture object and close the window
        self._cap.release()
        cv2.destroyAllWindows()
