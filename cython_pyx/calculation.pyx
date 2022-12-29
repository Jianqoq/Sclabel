from random import *
from numpy import *
from os import *
from math import *


cpdef tuple label2_event_pos(int x, int y, double factor):
    cdef double x2, y2
    x2 = x // factor
    y2 = y // factor
    return int(x2), int(y2)


cpdef double new_width(double angle, int height, int width):
    cdef double x, q

    if 0 <= angle <= 90 or 180 <= angle <= 270:
        x = cos(radians(angle1))
        q = cos(radians(90 - angle1))
    elif 90 < angle < 180 or 270 < angle <= 360:
        angle = 180 - angle
        x = cos(radians(angle))
        q = cos(radians(90 - angle))
    if isclose(x, 0):
        x = 0
    if isclose(q, 0):
        q = 0
    return format(abs(height * x + width * q), '.1f')


cdef double new_height(double angle, int height, int width):
    cdef double x, q
    if 0 <= angle <= 90 or 180 <= angle <= 270:
        x = cos(radians(angle))
        q = cos(radians(90 - angle))
    elif 90 < angle < 180 or 270 < angle <= 360:
        angle = 180 - angle
        x = cos(radians(angle))
        q = cos(radians(90 - angle))
    if isclose(x, 0):
        x = 0
    if isclose(q, 0):
        q = 0
    return format(abs(height * q + width * x), '.1f')


cpdef double compare(int num1, int num2, int height, int width):
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


def generate(int rows, int cols):

    cdef list choose = [0, 1]
    cdef int choice = random.choice(choose)
    cdef float y1, x2, x3, y2
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


def get_validname(savefiledir, name, count, form):
    save = f'{savefiledir}/{name}{str(count)}{form[1]}'
    while path.exists(save):
        count += 1
        save = f'{savefiledir}/{name}{str(count)}{form[1]}'
    return save


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