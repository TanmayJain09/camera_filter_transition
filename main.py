from core.camera import Camera
from core.engine import Engine
from addons.face_filter_addon import FaceFilterAddon

def main():
    camera = Camera(0)
    addon = FaceFilterAddon()

    engine = Engine(camera, addon)
    engine.run()

if __name__ == "__main__":
    main()