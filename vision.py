from cv2 import cv2
from matplotlib import pyplot as plt
from mss import mss
from PIL import Image
import numpy

class Vision:
    def __init__(self):
        #Dictionary of images for tests
        self.static_templates = {
            'play-game': 'static/play_game.png'
        }

        self.templates = { k: cv2.imread(v, 0) for (k, v) in self.static_templates.items() }

        self.monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
        self.screen = mss()

        self.frame = None
    def convert_rgb_to_bgr(self, img):
        return img[:, :, ::-1]
    def take_screenshot(self):
        screen_shot = self.screen.grab(self.monitor)
        img = Image.frombytes('RGB', screen_shot.size, screen_shot.rgb)
        img = numpy.array(img)
        img = self.convert_rgb_to_bgr(img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img_gray
    def refresh_frame(self):
        self.frame = self.take_screenshot()
    def match_template(self, img_grayscale, template, threshold=0.9):
        """
        1. Loads image and puts template in
        2. Performs match template using cv2 
        3. Checks if threshold is met and returns matches
        """

        res = cv2.matchTemplate(img_grayscale, template, cv2.TM_CCOEFF_NORMED)
        matches = np.where(res >= threshold)
        return matches
    def find_template(self, name, image=None, threshold=0.9):
        if image is None:
            if self.frame is None:
                self.refresh_frame()

            image = self.frame

        return self.match_template(
            image,
            self.templates[name],
            threshold
        )

