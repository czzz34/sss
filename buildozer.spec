[app]
title = CameraApp
package.name = cameraapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,kv

version = 0.1

# Keep requirements minimal
requirements = python3,kivy,opencv,cv2,app,

orientation = portrait

# Android permissions (read/write for gallery + camera)
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

fullscreen = 0
