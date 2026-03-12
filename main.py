import os
import cv2
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

# Android storage
try:
    from android.storage import primary_external_storage_path
    path = primary_external_storage_path()
    SAVE_FOLDER = os.path.join(path, "pic")
except:
    SAVE_FOLDER = "pic"

class CameraApp(App):

    def build(self):
        label = Label(text="Opening Camera...")
        Clock.schedule_once(self.capture_image, 2)
        return label

    def capture_image(self, dt):

        if not os.path.exists(SAVE_FOLDER):
            os.makedirs(SAVE_FOLDER)

        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()

        if ret:
            filename = os.path.join(
                SAVE_FOLDER,
                f"img_{int(time.time())}.jpg"
            )
            cv2.imwrite(filename, frame)

            print("Saved:", filename)
            App.get_running_app().root.text = "Image Captured"

        else:
            App.get_running_app().root.text = "Camera Failed"

        cap.release()

CameraApp().run()