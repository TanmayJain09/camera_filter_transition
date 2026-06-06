import cv2

class Engine:
    def __init__(self, camera, addon):
        self.camera = camera
        self.addon = addon

    def run(self):
        while True:
            frame = self.camera.read()

            if frame is None:
                break

            output = self.addon.process(frame)

            cv2.imshow("Addon Output", output)

            # press q to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()