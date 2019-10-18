from cv2 import cv2
import numpy
from vision import Vision
from controller import Controller
from game_test import Game
import time
import os
from PIL import ImageTk, Image

vision = Vision()
controller = Controller()
game = Game(vision, controller)

game.run()
