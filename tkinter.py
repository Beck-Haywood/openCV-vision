'''from cv2 import cv2
import numpy
import os
#from tkinter import *
from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import ttk

root = tk.Tk()

def display_example():
    img1.place(x=0,y=0)
    img1.pack()
def display_answer():
    img1.pack_forget()
    load = Image.open('found_waldo.png')
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=0,y=0)
    img.pack()
#wat = cv2.imread(os.path.expanduser('~/dev/repos/openCV_vision/static/images/play_game.png'), 0)
#Tkinter setup
#window = tk.Tk()
window.geometry("300x300")
window.title("Computer Vision")
menu = Menu(window)
window.config(menu=menu)
example = Menu(menu)
menu.add_cascade(label='Example', menu=example)
#Variables for showing example setup
load1 = Image.open('find_waldo.jpg')
render1 = ImageTk.PhotoImage(load1)#image=Image.fromarray(find_waldo)
img1 = Label(image=render1)
img1.image = render1
#Drop down that shows examples
example.add_command(label="Wheres Waldo?", command=lambda : display_example())
example.add_command(label="Find Waldo", command=lambda : display_answer())
#Buttons and title
title1 = Label(window,text="Image matching", font=("arial",20,"bold")).pack()
button1 = Button(window,text="Show Picture", width = 9, command=lambda : cv2.imshow('play_game.png', wat))
button2 = Button(window,text="Quit", width = 5, command=lambda : exit())
button2.place(x=120,y=35)
button1.place(x=5,y=35)
window.mainloop()
'''