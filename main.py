from core.camera import Camera
from core.engine import Engine
from addons.glasses_filter_addon import GlassesFilterAddon

def main():
    camera = Camera(0)
    addon = GlassesFilterAddon()

    engine = Engine(camera, addon)
    engine.run()

if __name__ == "__main__":
    main()