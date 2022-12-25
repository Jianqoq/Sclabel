import cv2
import tempfile
import os
import numpy as np
import random
from cython_libary import calculate


# read full screenshot temp img, then create and write an cropped img to a new temp file.
# Finally return the temp file instance, temp file name and the cropped matrix
def readimage(file, posx: int, posy: int, sizex: int, sizey: int, format: tuple, quality: int):
    image = cv2.imread(file)
    matrix = image[posy: posy + sizey, posx: posx + sizex]
    temp = tempfile.NamedTemporaryFile(suffix=format[1], delete=False)
    name = temp.name
    cv2.imwrite(name, matrix, [format[0], quality])
    return temp, name, matrix

# save full screenshot instead of cropping
def savefullimg(path, save, format: tuple, quality: int):
    image = cv2.imread(path)
    cv2.imwrite(save, image, [format[0], quality])


def dataaugment(filedir: str, savefiledir: str, name: str, display, progressbar, form: tuple, quality: int):
    images = os.scandir(filedir)
    display.setText('Estimating file number...')
    file_num = len(list(os.scandir(filedir)))
    displayfilenum(file_num, display)
    count = 0
    progress = 0
    progressbar.setRange(0, file_num)
    calculate.generate_augmentfile(images, filedir, progress, count,
                                   progressbar, savefiledir, name, form,
                                   display, quality)
    display.setText('Augment finished...')


# image shift
def translation(image: str, save: str, w, method: int, quality: int):
    img = cv2.imread(image)
    if check_validimage(img, w):
        return
    w.setText(image)
    rows, cols, colors = img.shape
    M = np.float32([[1, 0, 50], [0, 1, 50]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    random_final(save, dst, method, quality)

# image rotation at random angle
def rotation(image: str, save: str, w, method: int, quality: int):
    img = cv2.imread(image)
    if check_validimage(img, w):
        return
    w.setText(image)
    angle = round(random.uniform(0, 360),1)
    rows, cols, colors = img.shape
    x = calculate.new_height(angle, rows, cols)
    y = calculate.new_width(angle, rows, cols)
    factor = calculate.compare(y, x, rows, cols)
    M = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), angle, factor)
    dst = cv2.warpAffine(img, M, (cols, rows))
    random_final(save, dst, method, quality)

# 90 degrees rotation
def rotation90(image: str, save: str, w, method: int, quality: int, angle=90):
    img = cv2.imread(image)
    if check_validimage(img, w):
        return
    w.setText(image)
    rows, cols, colors = img.shape
    x = calculate.new_height(angle, rows, cols)
    y = calculate.new_width(angle, rows, cols)
    factor = calculate.compare(y, x, rows, cols)
    M = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), angle, factor)
    dst = cv2.warpAffine(img, M, (cols, rows))
    random_final(save, dst, method, quality)

# 180 degrees rotation
def rotation180(image: str, save: str, w, method: int, quality: int, angle=180):
    img = cv2.imread(image)
    if check_validimage(img, w):
        return
    w.setText(image)
    rows, cols, colors = img.shape
    x = calculate.new_height(angle, rows, cols)
    y = calculate.new_width(angle, rows, cols)
    factor = calculate.compare(y, x, rows, cols)
    M = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), angle, factor)
    dst = cv2.warpAffine(img, M, (cols, rows))
    random_final(save, dst, method, quality)


def affine_transformation(image: str, save: str, w, method: int, quality: int):
    img = cv2.imread(image)
    if check_validimage(img, w):
        return
    w.setText(image)
    rows, cols, colors = img.shape
    pts1, pts2 = calculate.generate(rows, cols)
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols, rows))
    random_final(save, dst, method, quality)

# choose if the augmented img do mirror processing again or not
def random_final(save, dst, method: int, quality: int):
    a = random.randrange(0, 2)
    if a == 0:
        cv2.imwrite(save, dst, [method, quality])
    elif a == 1:
        cv2.imwrite(save, np.flip(dst, 1), [method, quality])

# flip over y axis
def flip(image: str, save: str, w):
    if w is not None:
        w.setText(image)
    img = cv2.imread(image)
    if check_validimage(img, None):
        return
    else:
        new_img = np.flip(img, 1)
        cv2.imwrite(save, new_img)

# flip over x axis
def flip2(image: str, save: str, w):
    if w is not None:
        w.setText(image)
    img = cv2.imread(image)
    if check_validimage(img, None):
        return
    else:
        new_img = np.flip(img, 0)
        cv2.imwrite(save, new_img)

# check if the file is image or not
def check_validimage(image, line_edit):
    if image is None:
        if line_edit is None:
            return True
        else:
            line_edit.setText('Not image file')
            return True
    else:
        return False


def displayfilenum(file_num, label):
    if file_num > 1:
        label.setText(f'Found {file_num} files')
    elif file_num <= 1:
        label.setText(f'Found {file_num} file')
