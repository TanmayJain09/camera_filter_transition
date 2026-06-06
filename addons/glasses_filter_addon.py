import cv2
import numpy as np
from core.plugin_base import PluginBase

class GlassesFilterAddon(PluginBase):
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        # load glasses image (with alpha channel)
        self.glasses = cv2.imread("assets/glasses.png", cv2.IMREAD_UNCHANGED)

    def overlay(self, frame, overlay_img, x, y, w, h):
        overlay_img = cv2.resize(overlay_img, (w, int(h / 2)))

        for i in range(overlay_img.shape[0]):
            for j in range(overlay_img.shape[1]):

                if y + i >= frame.shape[0] or x + j >= frame.shape[1]:
                    continue

                alpha = overlay_img[i, j, 3] / 255.0  # transparency

                for c in range(3):
                    frame[y + i, x + j, c] = (
                        alpha * overlay_img[i, j, c] +
                        (1 - alpha) * frame[y + i, x + j, c]
                    )

        return frame

    def process(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        for (x, y, w, h) in faces:
            # position glasses slightly above center of face
            frame = self.overlay(
                frame,
                self.glasses,
                x,
                y + int(h * 0.25),
                w,
                h
            )

        return frame