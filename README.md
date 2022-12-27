# Sclabel
A tool which can do screenshot with fixed size, image augment, and image annotation

# Requirment
libary: PyQt5, Numpy, Opencv, Cython, pywin32
Interpretor: Python 3.10 or above
Operation system: windows

# Fetures
1. Take full or fixed size screenshot.
2. Image processing. Flip, mirror, rotation and shiftting.
3. Image annotation. Support rectangular shape so far.
4. Random Image augmentation.
5. Traning and validation dataset splitting.

# How does fixed size screenshot works
Image is three dimension array(three dimension tensor). For example, we have a shape of array
```
In: image = np.array([[[1, 1, 1],
                       [4, 4, 4]],
                      [[1, 1, 1],
                        [4, 4, 4]]])                 
In: image.shape

Out: (2, 2, 3)
```
2 x 2 means the image has both width and height with 2 pixels. 3 means the number of color channels(RGB normally). It means an image is consists of three 2x2 matrix. We can treat each whole column as one image with one color channel.
![Image text](https://raw.githubusercontent.com/Jianqoq/Sclabel/main/Image/image.jpg)
```
1   1   1
4   4   4

1   1   1
4   4   4
```
If we want to crop an image with color. we will simply combine the channels to a whole thing and do slicing only along the first and the second axis. The example below shows us how we can crop the uppper half of the image.
```
In: array[0: 1, 0: 2]

Out: array([[[1, 1, 1],
        [4, 4, 4]]])
```
