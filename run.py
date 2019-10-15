from cv2 import cv2
import numpy
from vision import Vision
import time
import os
from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Computer Vision")
title1 = Label(window,text="Image matching", font=("arial",20,"bold")).pack()
window.mainloop()
vision = Vision()

#def find_playbutton():
#    matches = vision.find_template('play-game',vision.frame, threshold=0.75)
#    print(numpy.shape(matches)[1] >= 1)

#find_playbutton()
wat = cv2.imread(os.path.expanduser('~/dev/repos/openCV_vision/static/images/play_game.png'), 0)
cv2.imshow('play_game.png', wat)
cv2.waitKey(5000)
cv2.destroyAllWindows()
print(wat)
