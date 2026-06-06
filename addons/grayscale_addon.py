import cv2
from core.plugin_base import PluginBase

class GrayScaleAddon(PluginBase):
    def process(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)