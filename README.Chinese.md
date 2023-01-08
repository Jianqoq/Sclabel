# Sclabel
[![en](https://img.shields.io/badge/language-English-red.svg)](https://github.com/Jianqoq/Sclabel/blob/main/README.md)
一个工具，可以做固定大小的截图，图像放大，和图像注释

# 要求
模块: PyQt5, Numpy, Opencv, Cython, pywin32

编译器版本: Python 3.10 or above

操作系统: windows

# Features
1.全屏或固定尺寸截图。
2.图像处理。目前支持翻转、镜像、旋转和移动。
3.图像注释。目前支持矩形。
4.随机图像增强。
5.训练与验证资料分类。

# 如何使用
1. 截图.

按-或单击Create按钮。如果你想裁剪图像，在红框出现后左键点击即可。右键单击撤消裁剪。按ESC退出裁剪。按Enter保存裁剪后的图像。
如果你想保存全屏截图而不是裁剪图片，直接按下Enter键。

![](https://github.com/Jianqoq/Sclabel/blob/main/Image/gif.gif)

2. 设置窗口

请看下面的图片注释。Label file name与要保存的图片文件名相同，只是扩展名不同。尚不支持此位置，目前标签文件将保存在图像文件的同一目录中。

![Image text](https://github.com/Jianqoq/Sclabel/blob/main/Image/setting.png)

3. 随机数据增强
![](https://github.com/Jianqoq/Sclabel/blob/main/Image/gif7.gif)

4. 图片标注(单文件)

单击主窗口中的Annotation按钮会弹出一个新窗口。将文件夹或图片拖到输入栏即可获取对应路径。点击Confirm就会直接进入标注模式。在标注模式下,左键点击拖动就可以生成一个长方形,鼠标释放后会弹出一个对话框,然后可以键入一个新类别或者可以直接单击列表框中的一个类别。右侧显示的是标注框信息。

![](https://github.com/Jianqoq/Sclabel/blob/main/Image/GIF2.gif)

双击可以选择一个特定的框,然后就可以只调整这个框的大小。再次双击可以取消选择。你也可以通过右键单击列表中的某一个内容来删除对应的框。

![](https://github.com/Jianqoq/Sclabel/blob/main/Image/gif3.gif)
![](https://github.com/Jianqoq/Sclabel/blob/main/Image/gif4.gif)

单文件标注模式下,完成后,按Enter或+将退出标注模式，并在图像文件的同一目录下生成一个json文件。

![](https://github.com/Jianqoq/Sclabel/blob/main/Image/gif5.gif)

5. 图片标注(多文件)

对于多图像文件标注，操作类似于单个文件。只需要拖动文件夹。如果要继续标记，按Confirm键，然后单击OK按钮。如果不想要，单击Cancel，软件会读取所提供的图像。

![](https://github.com/Jianqoq/Sclabel/blob/main/Image/gif6.gif)

注意:进入标注模式后，按→键可进入下一幅图像，不保存注释文件，按+键可进入下一个文件，同时生成标注文件。按Enter键可直接退出软件并生成标注文件。

# 如何做特定大小的图片截取
图像是三维数组(三维张量)。例如，我们有一个数组的shape
```   
In: image = np.array([[[1, 1, 1],
                       [4, 4, 4]],
                      [[1, 1, 1],
                        [4, 4, 4]]])                 
In: image.shape

Out: (2, 2, 3)
```
2 x 2意味着图像的宽度和高度都是2个像素。3表示颜色通道的数量(通常为RGB)。这意味着一幅图像由三个2×2的矩阵组成。我们可以将每一大列视为一个具有一个颜色通道的图像。

![Image text](https://raw.githubusercontent.com/Jianqoq/Sclabel/main/Image/image.jpg)
```
1   1   1
4   4   4

1   1   1
4   4   4
```
如果我们想裁剪带颜色的图像。可以将三个大的列组合成一个整体，然后只沿着第一和第二轴做切片。下面的例子展示了如何裁剪图像的上半部分。
```
In: image[0: 1, 0: 2]

Out: array([[[1, 1, 1],
        [4, 4, 4]]])
```
![Image text](https://raw.githubusercontent.com/Jianqoq/Sclabel/main/Image/image2.jpg)

在该软件中，显示的红色矩形，其尺寸代表图像裁剪时的切片区域。

![Image text](https://raw.githubusercontent.com/Jianqoq/Sclabel/main/Image/b6e9515a10957967ddee00befa6ea40.png)
# 如何把标注文件转换成YOLO适合的格式
在Dataset_manipulation_example/Dataset_manipulation.py文件中，我写了一个示例文件。函数是“convert”和“convert_json2label”

第一个数字代表类名。第二个和第三个表示边界框相对于图像的中心点。第四个和第五个表示边界框相对于图像的宽度和高度。

本软件生成的Json文件包括边界框、图像宽度、图像高度和类名两点。因此，我们可以做一些计算来转换它们以满足Yolo要求。
![Image text](https://raw.githubusercontent.com/Jianqoq/Sclabel/main/Image/format.png)

在Python中，我们可以直接导入json模块来把json文件转换为字典。
```
import json
jsonfile_path = '......'
with open(jsonfile_path) as fp:
    dictionary = json.load(fp)
```
从json文件中获取信息后，我们首先从字典中获取所有信息。
```
width = int(dic['Image_width'])
height = int(dic['Image_height'])
points = ((item['Init Pos'], item['final Pos'], item['Name']) for item in dic['Label'])
```
然后，我们创建一个包含类名和相应编号的字典。稍后，我们使用for循环将所有计算结果存储到一个列表中。
```
dictionary = {
    'sdv': 1,
    'DT': 0
}
lis = []
for initpt, finalpt, name in points:
    initpoint = initpt
    finalpoint = finalpt
    initx = float(initpoint[0])
    inity = float(initpoint[1])
    finalx = float(finalpoint[0])
    finaly = float(finalpoint[1])
    label_width = abs(finalx - initx)
    label_height = abs(finaly - inity)
    center_x = format(abs(((finalx + initx)/2)/width), '.6f')
    center_y = format(abs(((finaly + inity) / 2) / height), '.6f')
    relative_width = format(label_width/width, '.6f')
    relative_height = format(label_height/height, '.6f')
    lis.append(f'{dictionary[name]} {center_x} {center_y} {relative_width} {relative_height}\n')
```
然而，我们不直接使用for循环，而是使用推导式来让它性能更强，代码更简洁。首先，我们定义一个函数calculate，并让它返回字符串。然后用列表推导式。
 ```
 def calculate(initpt, finalpt, name, width, height, classdict):
    initpoint = initpt
    finalpoint = finalpt
    initx = float(initpoint[0])
    inity = float(initpoint[1])
    finalx = float(finalpoint[0])
    finaly = float(finalpoint[1])
    label_width = abs(finalx - initx)
    label_height = abs(finaly - inity)
    center_x = format(abs(((finalx + initx) / 2) / width), '.6f')
    center_y = format(abs(((finaly + inity) / 2) / height), '.6f')
    relative_width = format(label_width / width, '.6f')
    relative_height = format(label_height / height, '.6f')
    return f'{classdict[name]} {center_x} {center_y} {relative_width} {relative_height}\n'
```

最终的代码将会非常简洁而且速度很快
```
dic = {
    'sdv': 1,
    'DT': 0
}
width = int(dic['Image_width'])
height = int(dic['Image_height'])
points = ((item['Init Pos'], item['final Pos'], item['Name']) for item in dic['Label'])
final_list = [calculate(initpt, finalpt, name, width, height, classdict) for initpt, finalpt, name in points]

```
最后，我们将列表转换为字符串，然后将结果写入文件。
```
string = ''.join(final_list)
with open(path, mode='w') as fp:
    fp.write(string)
```
# 图像处理(如何使用Opencv在旋转过程中避免内容丢失)
首先,Opencv为我们提供了一种旋转图像的方法。
```
import cv2

image_path = '......'
image = cv2.imread(image_path)    # read image
rotate_angle = 90                 # define rotate angle
rows, cols, colors = image.shape  # get shape of image, here is 3D tensor
scale_factor = 1                        # define scaling factor
Matrix = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), rotate_angle, scale_factor)   # get the transform matrix
final_image = cv2.warpAffine(image, Matrix, (cols, rows))                               # rotate image
```
但是，如果将scale_factor作为1一起使用，很容易导致内容丢失。为了避免这种情况发生，无论旋转角度是多少，我们都需要指定一个正确的因子值。遗憾的是Opencv好像没有提供一个函数来获得这个值。因此，我们需要做一些简单的几何分析。
![Image text](https://raw.githubusercontent.com/Jianqoq/Sclabel/main/Image/image3.jpg)
我们首先需要得到新的宽和新的高。然后，我们可以计算相应边的比例因子。我们通过比较这两个值来选择最小的因子。源代码可以在functions/calculation.py中找到。因此，我们更改了一些代码。
```
import cv2
from functions import calculation

image_path = '......'
image = cv2.imread(image_path)    # read image
rotate_angle = 90                 # define rotate angle
rows, cols, colors = image.shape  # get shape of image, here is 3D tensor
new_height = calculation.new_height(rotate_angle, rows, cols)     # calculate new height
new_width = calculation.new_width(rotate_angle, rows, cols)       # calculate new width
scale_factor = calculation.compare(new_height, new_width, rows, cols)                     # calculate scale factor
Matrix = cv2.getRotationMatrix2D(((cols-1)//2, (rows-1)//2), rotate_angle, scale_factor)   # get the transform matrix
final_image = cv2.warpAffine(image, Matrix, (cols, rows))                               # rotate image
```

# 如何让绘制的边界框可选择和可调节大小

首先，使用一个列表来存储长方形并在paintevent中绘制所有长方形。每次创建一个新长方形时，将所有长方形信息存储到不同列表中。在MousemoveEvent时，跟踪并使用for循环来检查鼠标是否靠近边缘。函数可以在functions/Draw.py和cython_pyx/Find_edge.pyx中找到。
```
def paintEvent(self, event):
  super().paintEvent(event)
  qp = QPainter(self)
  br2 = self.brush
  pen = QPen()
  draw.drawcurrentrect(self.pressed, self.edge, pen, qp,
                             br2, self.width, self.rectbrushcolor,
                             self.begin, self.end)
  draw.drawhisrect(pen, qp, self.rectlist, self.storecolor, self.storewidth,
                         self.storerectbrushcolor, self.storecirclewidth, self.storecirclebrushcolor,
                         self.storebegin, self.storecircleradius, self.storeend)
```

# 如何在大数据集操作时显示进度
在functions/dataset _ manipulation.py文件中，函数“print_result”可以实现此功能。

首先，我们创建一个有18个空格的列表，列表的两端各有1个括号[ 或 ]
```
In: lis = ['[' if i == 0 else ']' if i == 19 else ' ' for i in range(20)]
In: print(''.join(lis))
Out: [                  ]
```
其次，将第一个和第二个空格字符串更改为u'\u25A0'将得到如下所示的输出
```
In: lis = ['[' if i == 0 else ']' if i == 19 else ' ' for i in range(20)]
In: lis[1] = u'\u25A0'
In: lis[2] = u'\u25A0'
In: print(''.join(lis))
Out: [■■                ]
```
最后代码变成如下，40是当前任务， 100是总任务数。
```
In: print_result(40, 100)
Out: [■■■■■■            ] 40.00%
```
# 如何分割图像集以进行训练和验证

这功能可以在functions/dataset_manipulation.py文件中找到。
首先我们得到包含所有以'.png'结尾的图像文件的列表。
```
list = [file.name for file in os.scandir(origi_dir) if file.name.endswith('.png')]
```
其次，遍历整个列表，得到json文件和image文件的路径，然后移动到目标文件夹。一旦达到阈值立刻停止。
可以通过提供我们需要处理的文件总数和当前文件号来显示进度。使用类似的for循环将文件的其余部分移动到验证文件夹。
```
list = [file.name for file in os.scandir(origi_dir) if file.name.endswith('.png')]
length = len(list)              
limit = (1-ratio)*length        # get the total file numbers we need to process
for index, name in enumerate(list):
    if index <= limit:
        basename = os.path.splitext(name)[0]
        newname = f'{basename}{label_suffix}'
        label_file_path = os.path.join(origi_dir, newname)
        src = os.path.join(origi_dir, name)
        try:
            shutil.move(src, dist_trainimg_dir)
            shutil.move(label_file_path, dist_trainlabel_dir)
        except Exception as e:
            print(e)
            break
        print_result(index, limit)
```
最后，您可以通过调用“split_dataset_2_train_val”函数来简单地执行这种拆分，其中0.8是训练数据，(1-0.8)是验证数据。。“png”是一种图像格式。“txt”是标签文件格式。
```
split_dataset_2_train_val(0.8, r'C:\Users\Public\Pictures\data\DATASET',
                          r'C:\Users\Public\Pictures\VOCdevkit\images\Train',
                          r'C:\Users\Public\Pictures\VOCdevkit\labels\Train',
                          r'C:\Users\Public\Pictures\VOCdevkit\images\Val',
                          r'C:\Users\Public\Pictures\VOCdevkit\labels\Val',
                          '.png', '.txt')
```

