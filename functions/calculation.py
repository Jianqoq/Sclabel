from random import *
from numpy import *
from os import *
from math import *


# calculate real pos based on High DPI scaling factor
def label2_event_pos(x, y, factor):
    x = int(x // factor)
    y = int(y // factor)
    return x, y


# calculate new_width after rotation
def new_width(angle, height, width):
    h = height
    w = width
    angle1 = angle
    x = 0
    q = 0
    if 0 <= angle <= 90 or 180 <= angle <= 270:
        x = cos(radians(angle1))
        q = cos(radians(90 - angle1))
    elif 90 < angle < 180 or 270 < angle <= 360:
        angle1 = 180 - angle1
        x = cos(radians(angle1))
        q = cos(radians(90 - angle1))
    if isclose(x, 0):
        x = 0
    if isclose(q, 0):
        q = 0
    return round(abs(h * x + w * q), 1)


# calculate new_height after rotation
def new_height(angle, height, width):
    h = height
    w = width
    angle1 = angle
    x = 0
    q = 0
    if 0 <= angle <= 90 or 180 <= angle <= 270:
        x = cos(radians(angle1))
        q = cos(radians(90 - angle1))
    elif 90 < angle < 180 or 270 < angle <= 360:
        angle1 = 180 - angle1
        x = cos(radians(angle1))
        q = cos(radians(90 - angle1))
    if isclose(x, 0):
        x = 0
    if isclose(q, 0):
        q = 0
    return round(abs(h * q + w * x), 1)


def compare(num1, num2, height, width):
    if num1 > num2:
        if num2 > width:
            return min(width/num2, height/num1)
        return height/num1
    if num2 > num1:
        if num1 > height:
            return min(height/num1, width/num2)
        return width/num2
    if num1 == num2:
        return height/num1

# this function is calculating new matrix for affine_transformation in the Image_processing file
def generate(rows, cols):
    choose = [0, 1]
    choice = random.choice(choose)
    if choice == 0:
        y1 = random.uniform(0, 1)
        while True:
            x1 = 0
            x2 = round(random.uniform(0, 1), 1)
            x3 = round((1 - x2), 1)
            if x1 < x3 <= x2:
                y2 = round(random.uniform(0, y1), 1)
                y3 = round(random.uniform(y1, 1), 1)
                pts1 = array([[0, 0], [cols - 1, 0], [0, rows - 1]]).astype(np.float32)
                pts2 = array([[x1, rows * y1], [cols * x2, rows * y2],
                                 [cols * x3, rows * y3]]).astype(np.float32)
                return pts1, pts2
    elif choice == 1:
        y2 = random.uniform(0, 1)
        while True:
            x2 = cols - 1
            x1 = round(random.uniform(0, 1), 1)
            x3 = round((1 - x1), 1)
            if x1 > x3 <= 1:
                y1 = round(random.uniform(0, y2), 1)
                y3 = round(random.uniform(y2, 1), 1)
                pts1 = array([[0, 0], [cols - 1, 0], [cols - 1, rows - 1]]).astype(np.float32)
                pts2 = array([[cols * x1, rows * y1], [x2, rows * y2],
                                 [cols * x3, rows * y3]]).astype(np.float32)
                return pts1, pts2


# increase one or append a number after the filename if the filename is already exists
def get_validname(savefiledir, name, count, form):
    save = f'{savefiledir}/{name}{str(count)}{form[1]}'
    while path.exists(save):
        count += 1
        save = f'{savefiledir}/{name}{str(count)}{form[1]}'
    return save

# randomly do image augmentation and display progressbar
def generate_augmentfile(self, *args):
    images, filedir, progress, count, progressbar, savefiledir, name, format, display, quality = args
    if not path.exists(savefiledir):
        makedirs(savefiledir)
    for k in images:
        loc = f'{filedir}/{k.name}'
        progress += 1
        count += 1
        progressbar.setValue(progress)
        save = get_validname(savefiledir, name, count, format)
        foo_list = [self.translation, self.rotation90, self.rotation, self.rotation180]
        random.choice(foo_list)(loc, save, display, format[0], quality)
