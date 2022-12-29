import cv2, tempfile, os
import numpy as np
import random
from cython_libary import calculation


def readimage(file, posx: int, posy: int, sizex: int, sizey: int, format: tuple, quality: int):
    image = cv2.imread(file)
    q = image[posy: posy + sizey, posx: posx + sizex]
    temp = tempfile.NamedTemporaryFile(suffix=format[1], delete=False)
    name = temp.name
    cv2.imwrite(name, q, [format[0], quality])
    return temp, name, q


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
    calculation.generate_augmentfile(images, filedir, progress, count, progressbar, savefiledir, name, form, display, quality)
    display.setText('Augment finished...')


def translation(image: str, save: str, w, method: int, quality: int):
    img = cv2.imread(image)
    if check_validimage(img, w):
        return
    w.setText(image)
    rows, cols, colors = img.shape
    M = np.float32([[1, 0, 50], [0, 1, 50]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    random_final(save, dst, method, quality)


def rotation(image: str, save: str, w, method: int, quality: int):
    img = cv2.imread(image)
    if check_validimage(img, w):
        return
    w.setText(image)
    angle = round(random.uniform(0, 360),1)
    rows, cols, colors = img.shape
    x = calculation.new_height(angle, rows, cols)
    y = calculation.new_width(angle, rows, cols)
    factor = calculation.compare(y, x, rows, cols)
    M = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), angle, factor)
    dst = cv2.warpAffine(img, M, (cols, rows))
    random_final(save, dst, method, quality)


def rotation90(image: str, save: str, w, method: int, quality: int, angle=90):
    img = cv2.imread(image)
    if check_validimage(img, w):
        return
    w.setText(image)
    rows, cols, colors = img.shape
    x = calculation.new_height(angle, rows, cols)
    y = calculation.new_width(angle, rows, cols)
    factor = calculation.compare(y, x, rows, cols)
    M = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), angle, factor)
    dst = cv2.warpAffine(img, M, (cols, rows))
    random_final(save, dst, method, quality)


def rotation180(image: str, save: str, w, method: int, quality: int, angle=180):
    img = cv2.imread(image)
    if check_validimage(img, w):
        return
    w.setText(image)
    rows, cols, colors = img.shape
    x = calculation.new_height(angle, rows, cols)
    y = calculation.new_width(angle, rows, cols)
    factor = calculation.compare(y, x, rows, cols)
    M = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), angle, factor)
    dst = cv2.warpAffine(img, M, (cols, rows))
    random_final(save, dst, method, quality)


def affine_transformation(image: str, save: str, w, method: int, quality: int):
    img = cv2.imread(image)
    if check_validimage(img, w):
        return
    w.setText(image)
    rows, cols, colors = img.shape
    pts1, pts2 = calculation.generate(rows, cols)
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols, rows))
    random_final(save, dst, method, quality)


def random_final(save, dst, method: int, quality: int):
    a = random.randrange(0, 2)
    if a == 0:
        cv2.imwrite(save, dst, [method, quality])
    elif a == 1:
        cv2.imwrite(save, np.flip(dst, 1), [method, quality])


def flip(image: str, save: str, w):
    if w is not None:
        w.setText(image)
    img = cv2.imread(image)
    if check_validimage(img, None):
        return
    else:
        new_img = np.flip(img, 1)
        cv2.imwrite(save, new_img)


def flip2(image: str, save: str, w):
    if w is not None:
        w.setText(image)
    img = cv2.imread(image)
    if check_validimage(img, None):
        return
    else:
        new_img = np.flip(img, 0)
        cv2.imwrite(save, new_img)


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
