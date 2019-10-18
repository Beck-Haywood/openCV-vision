#My motivation behind this project V
My motivation behind this has come from robotics in highschool I utilized tensorflow to track objects that the robot was moving. I always wanted to make an advanced videogame bot even though it wont be that useful. This is the first step to creating a bot. For my computer vision software im using openCV, MSS, Pillow, Numpy, and pyMouse. These allow me to take screen shots of the monitor and compare a template to each screenshot, the template matching method returns the x and y corrdinates of the matched image, allowing me to draw a box around the match using openCV commands, and teleport my mouse to the location to navigate websites, game clients or anything the computer can access.
#How to run V
How to run: insert images into the dictonary template in start of vision.py. Example: 'image-name': 'path to image.png'
Then on run: matches = vision.find_template('templatename', image=None) This will find the match and # print(np.shape(matches)[1] >= 1) will return true or false depending on if it finds it.
#Using matches to direct mouse V
Using pyMouse is as simple as setting  #x = matches[1][0]  #y = matches[0][0]  Then calling a move_mouse function will teleport your mouse close to the target and using offsets it can be accurate.
#Testing if matches are not being found V
Testing what openCV is acutually seeing as a match: in Vision.py uncommenting lines 70-74 will make a window pop up and it will draw a box around any object it finds. Keep in mind this for testing purposes and wont work well, while your navigating clients with pymouse.
                                      