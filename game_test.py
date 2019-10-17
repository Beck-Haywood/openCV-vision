import numpy as np
import time
from cv2 import cv2

class Game:

    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller
    def can_see_object(self, template, threshold=0.9):
        matches = self.vision.find_template(template, threshold=threshold)
        return np.shape(matches)[1] >= 1

    def click_object(self, template):#offset=(0, 0)
        matches = self.vision.find_template(template)

        x = matches[1]#[0] #+ offset[0]
        y = matches[0]#[0] #+ offset[1]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)
    def run(self):
        bot_run = True
        while bot_run:
            if cv2.waitKey(33) == ord('a'):
                bot_run == False
            if self.can_see_object('play-game'):
                self.click_object('play-game')

            



