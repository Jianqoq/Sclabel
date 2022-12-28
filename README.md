# Sclabel
A tool which can do screenshot with fixed size, image augment, and image annotation

# Requirment
Libary: PyQt5, Numpy, Opencv, Cython, pywin32

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
If we want to crop an image with color. we will simply combine the three big columns to a whole thing and do slicing only along the first and the second axis. The example below shows us how we can crop the uppper half of the image. In this sofware, a red rectangular will be displayed and its dimension represents slicing area.
```
In: array[0: 1, 0: 2]

Out: array([[[1, 1, 1],
        [4, 4, 4]]])
```
![Image text](https://raw.githubusercontent.com/Jianqoq/Sclabel/main/Image/image2.jpg)
![Image text](https://raw.githubusercontent.com/Jianqoq/Sclabel/main/Image/b6e9515a10957967ddee00befa6ea40.png)

# Image processing(How to avoid content losing during rotation by using Opencv)
First, to rotate an image. Opencv gives us a way to do so.
```
image = cv2.imread(image_path)    # read image
rotate_angle = 90                 # define rotate angle
rows, cols, colors = image.shape  # get shape of image, here is 3D tensor
scale_factor = 1                        # define scaling factor
Matix = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), rotate_angle, scale_factor)   # get the transform matrix
final_image = cv2.warpAffine(image, Matrix, (cols, rows))                               # rotate image
```
However, it could easily cause content losing by using scale_factor with 1. To avoid this happens, we need to assign a correct factor value. Saddly. Opencv seems doesn't provide a function to solve this. Thus we need to do some simple geometrical analysis.

