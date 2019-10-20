import time
from pynput.mouse import Button, Controller as MouseController

class Controller:
    def __init__(self):
        self.mouse = MouseController()
    # def move_mouse(self, x, y):
    #         def set_mouse_position(x, y):
    #             self.mouse.position = (int(x), int(y))
    #         def smooth_move_mouse(from_x, from_y, to_x, to_y, speed=0.3):
    #             steps = 40
    #             sleep_per_step = speed // steps
    #             x_delta = (to_x - from_x) / steps
    #             y_delta = (to_y - from_y) / steps
    #             for step in range(steps):
    #                 new_x = x_delta * (step + 1) + from_x
    #                 new_y = y_delta * (step + 1) + from_y
    #                 set_mouse_position(new_x, new_y)
    #                 time.sleep(sleep_per_step)
    #         return smooth_move_mouse(self.mouse.position[0], self.mouse.position[1], x, y)
    #def mouse_move(self, x, y):
     #   pass
       # def set_mouse_position(x, y):
        #    self.mouse.position(int(x), int(y))
    #def smooth_move_mouse(self, x, y, speed=3):
    #    current_x = self.mouse.position[0]
    #    current_y = self.mouse.position[1]
    #    steps = 400
    #    sleep_per_step = speed / steps
    #    total_y_delta = y - self.mouse.position[1]
    #    total_x_delta = x - self.mouse.position[0]
    #    
    #    y_delta = total_y_delta // steps
    #    x_delta = total_x_delta // steps
    #    while current_y > y:
    #        time.sleep(sleep_per_step)
    #        self.mouse.position = current_x, current_y    
    #        current_x += x_delta
    #        current_y += y_delta
    def set_mouse_position(self, x, y):
        self.mouse.position = (int(x), int(y))
    def mouse_move(self, x, y): 
        #current_x = self.mouse.position[0]
        #current_y = self.mouse.position[1]
        #self.mouse.position = current_x, current_y
        self.mouse.position = x, y



            



    def left_mouse_click(self):
        self.mouse.click(Button.left)