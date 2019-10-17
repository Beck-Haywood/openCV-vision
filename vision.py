from cv2 import cv2
from matplotlib import pyplot as plt
from mss import mss
from PIL import Image
import numpy

class Vision:
    def __init__(self):
        #Dictionary of images for tests
        self.static_templates = {
            'play-game': 'static/images/play_game_full.png',
            'co-op-vs-ai': 'static/images/CO-OP-VS-AI.png',
            'beginner-bots': 'static/images/beginner-bots.png',
            'confirm' : 'static/images/confirm.png',
            'find-game' : 'static/images/find-game.png'
        }

        self.templates = { k: cv2.imread(v, 0) for (k, v) in self.static_templates.items() }

        self.monitor = {'top': 0, 'left': 0, 'width': 1600, 'height': 920} #was 900
        self.screen = mss()

        self.frame = None
    def convert_rgb_to_bgr(self, img):
        return img[:, :, ::-1]
    def take_screenshot(self):
        screen_shot = self.screen.grab(self.monitor)
        print(type(screen_shot))
        img = Image.frombytes('RGB', screen_shot.size, screen_shot.rgb)
        #img = Image.open('static/images/leagueclient1.png') #was 'static/images/clientshot2.jpeg'
        img = numpy.array(img, dtype='f')
        print(img.shape)
        #img = self.convert_rgb_to_bgr(img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(img.shape[::-1])

        return img_gray #was img_gray
    def refresh_frame(self):
        self.frame = self.take_screenshot()
    def match_template(self, img, template, threshold=0.9):
        """
        1. Loads image and puts template in
        2. Performs match template using cv2 
        3. Checks if threshold is met and returns matches
        """
        #img_grayscale.astype(numpy.float32)
        #template.astype(numpy.float32)
        #template.astype(numpy.uint8)
        
        #Image where the search is running. It must be 8-bit or 32-bit floating-point. templ – Searched template. It must be not greater than the source image and have the same data type.


#which function is the template none type, is the template even none type? Where is the error actually happening
#Im passing a string not the actual image, into resize
       # print(self.templates)
       # print(img)
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        w, h = template.shape[::-1]
        method = None
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img,top_left, bottom_right, 255, 2)
        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.show()
        matches = numpy.where(res >= threshold)
        return matches
    def find_template(self, name, image=None, threshold=0.9):
        if image is None:
            #print('Image is None')
            if self.frame is None:
                #print('self.frame is None')
                self.refresh_frame()
                #print('Ran self.refresh_frame')

            image = self.frame
            
            #print(image)
            #image.astype(numpy.uint8)
            #print(image)
            #type(self.frame)
            #print(type(self.scre[name]))
            #cv2.imread(image, 0)
            #cv2.imshow("Screen shot", image)
            #print(self.templates[name].shape)    <<<<<<<<<tests
            #print(image.shape)                   <<<<<<<<<<tests
            self.templates[name] = numpy.array(self.templates[name], dtype='f')
            #template_image = self.convert_rgb_to_bgr(self.templates[name])
            #img_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
            #print(type(self.frame))
            #image1 = cv2.imread(self.teamplates[name])
            
            #image = cv2.imread(image, 0)
            #cv2.imshow("st", image)
            #cv2.imshow("static/images/play_game.png", self.templates[name])
            #cv2.waitKey(50000)
            #cv2.closeAllWindows()
        
       
        return self.match_template(image, self.templates[name], threshold)
        
    '''
    def scaled_find_template(self, name, image=None, threshold=0.9, scales=[1.0, 0.9, 1.1]):
        if image is None:
            if self.frame is None:
                self.refresh_frame()

            image = self.frame
        
        initial_template = self.templates[name]
        for scale in scales:
            scaled_template = cv2.resize(initial_template, (0,0), fx=scale, fy=scale)
            matches = self.match_template(
                image,
                scaled_template,
                threshold
            )
            if np.shape(matches)[1] >= 1:
                return matches
        return matches
        '''
