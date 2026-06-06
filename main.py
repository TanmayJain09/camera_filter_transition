from core.camera import Camera
from core.engine import Engine
from addons.grayscale_addon import GrayScaleAddon

def main():
    camera = Camera(0)          # webcam
    addon = GrayScaleAddon()    # plugin

    engine = Engine(camera, addon)
    engine.run()

if __name__ == "__main__":
    main()