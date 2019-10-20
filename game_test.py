import numpy as np
import time
from controller import Controller
from vision import Vision
from cv2 import cv2

class Game:

    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller
    def run(self):
        '''
        bot_run = True
        while bot_run:
            if cv2.waitKey(33) == ord('a'):
                bot_run == False
                '''
        
        self.vision.refresh_frame()
        matches = self.vision.find_template('play')
        x = matches[1][0] -65 #60
        y = matches[0][0] -40 #50
        print(matches)
        #self.controller.smooth_move_mouse(x, y)
        self.controller.mouse_move(x, y)
        self.controller.left_mouse_click()
        self.controller.left_mouse_click()


        time.sleep(3)
        self.vision.refresh_frame()
        #self.controller.smooth_move_mouse(10, 10)
        time.sleep(1)
        matches = self.vision.find_template('co-op-vs-ai')
        x = matches[1][0] -80 #60
        y = matches[0][0] -125 #50
        print(matches)
        self.controller.mouse_move(x, y)
        self.controller.left_mouse_click()

    
        time.sleep(0.5)
        self.vision.refresh_frame()
        #self.controller.smooth_move_mouse(10, 10)
        time.sleep(1)
        matches = self.vision.find_template('beginner-bots')
        x = matches[1][0]  -280#60
        y = matches[0][0] - 660
        print(matches)
        self.controller.mouse_move(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)
        self.vision.refresh_frame()
        #self.controller.smooth_move_mouse(10, 10)
        time.sleep(1)
        matches = self.vision.find_template('confirm')
        x = matches[1][0]  -480#60
        y = matches[0][0] - 830
        print(matches)
        self.controller.mouse_move(x, y)
        self.controller.left_mouse_click()
        # #find match
        # time.sleep(2)
        # self.controller.left_mouse_click()


        #time.sleep(0.5)
        #self.vision.refresh_frame()
        #matches = self.vision.find_template('accept', threshold = 0.95)
        #while matches == False:
        #    self.vision.refresh_frame()
        #    matches = self.vision.find_template('accept')
        #    time.sleep(2)
        #print('exited loop?')
        #x = matches[1][0]  -490
        #y = matches[0][0] - 830
        #print(matches)
       # self.controller.mouse_move(x, y)
       # self.controller.left_mouse_click()
        
       