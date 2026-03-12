# main.py
import os
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.clock import Clock

# Determine external storage on Android, fallback to local folder on PC
try:
    from android.storage import primary_external_storage_path
    base = primary_external_storage_path()
    SAVE_FOLDER = os.path.join(base, "pic")
except Exception:
    SAVE_FOLDER = "pic"

class CameraApp(App):
    def build(self):
        self.root = BoxLayout(orientation="vertical")
        self.status = Label(text="Opening Camera...")
        # create camera widget (uses Android camera via Camera API)
        self.cam = Camera(resolution=(1280, 720), play=True)
        self.root.add_widget(self.status)
        self.root.add_widget(self.cam)
        # schedule single capture 2 seconds after start
        Clock.schedule_once(self.capture_image, 2)
        return self.root

    def capture_image(self, dt):
        try:
            if not os.path.exists(SAVE_FOLDER):
                os.makedirs(SAVE_FOLDER, exist_ok=True)

            timestamp = int(time.time())
            filename = os.path.join(SAVE_FOLDER, f"img_{timestamp}.png")

            # export current camera widget to PNG file
            # (Camera is a widget — export_to_png saves the current frame)
            self.cam.export_to_png(filename)

            self.status.text = f"Saved: {filename}"
            print("Saved:", filename)

        except Exception as e:
            self.status.text = "Camera Failed"
            print("Capture error:", e)

        finally:
            # stop camera to release resources
            try:
                self.cam.play = False
            except Exception:
                pass

if __name__ == "__main__":
    CameraApp().run()
