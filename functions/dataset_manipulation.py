import json
import shutil
from Image_process import *
from file_manipulation import *


# Do mirror for the flipped imageset
def print_result(current, total):
    lis = ['[' if i == 0 else ']' if i == 19 else ' ' for i in range(20)]
    index = int(current/total*20)
    percentage = format(current*100 / total, '.2f')
    if 0 <= index < 20:
        pass
    else:
        index = 20
    if index > 0:
        for i in range(index-2):
            lis[i+1] = u'\u25A0'
            string = ''.join(lis)
            print(f'\r{string} {percentage}%', end='', flush=True)
    else:
        string = ''.join(lis)
        print(f'\r{string} {percentage}%', end='', flush=True)


def mirror(Savelocation, Image_dir):
    open_dir(Savelocation)
    directory = os.listdir(Image_dir)
    length = len(directory)
    for index, file in enumerate(directory):
        path = os.path.join(Image_dir, file)
        savepath = os.path.join(Savelocation, file)
        flip(path, savepath, None)
        print_result(index + 1, length)


def flip(Savelocation, Image_dir):
    open_dir(Savelocation)
    directory = os.listdir(Image_dir)
    length = len(directory)
    for index, file in enumerate(directory):
        path = os.path.join(Image_dir, file)
        savepath = os.path.join(Savelocation, file)
        flip2(path, savepath, None)
        print_result(index+1, length)


dictionary = {
    'DB': 1,
    'DT': 0
}


# Convertion
def convert(dic):
    width = int(dic['Image_width'])
    height = int(dic['Image_height'])
    points = ((item['Init Pos'], item['final Pos'], item['Name']) for item in dic['Label'])
    string = ''
    for initpt, finalpt, name in points:
        print(initpt, finalpt, name)
        initpoint = initpt
        finalpoint = finalpt
        initx = int(initpoint[0])
        inity = int(initpoint[1])
        finalx = int(finalpoint[0])
        finaly = int(finalpoint[1])
        label_width = abs(finalx - initx)
        label_height = abs(finaly - inity)
        center_x = format(abs(((finalx + initx)/2)/width), '.6f')
        center_y = format(abs(((finaly + inity) / 2) / height), '.6f')
        relative_width = format(label_width/width, '.6f')
        relative_height = format(label_height/height, '.6f')
        string = string + f'{dictionary[name]} {center_x} {center_y} {relative_width} {relative_height}\n'
    return string


def convert_mirror(dic):
    width = int(dic['Image_width'])
    height = int(dic['Image_height'])
    points = ((item['Init Pos'], item['final Pos'], item['Name']) for item in dic['Label'])
    string = ''
    for initpt, finalpt, name in points:
        initpoint = initpt
        finalpoint = finalpt
        initx = int(initpoint[0])
        inity = int(initpoint[1])
        finalx = int(finalpoint[0])
        finaly = int(finalpoint[1])
        label_width = abs(finalx - initx)
        label_height = abs(finaly - inity)
        center_x = format(abs(((finalx + initx)/2)/width-1), '.6f')
        center_y = format(abs(((finaly + inity) / 2) / height), '.6f')
        relative_width = format(label_width/width, '.6f')
        relative_height = format(label_height/height, '.6f')
        string = string + f'{dictionary[name]} {center_x} {center_y} {relative_width} {relative_height}\n'
    return string

def convert_flip(dic):
    width = int(dic['Image_width'])
    height = int(dic['Image_height'])
    points = ((item['Init Pos'], item['final Pos'], item['Name']) for item in dic['Label'])
    string = ''
    for initpt, finalpt, name in points:
        initpoint = initpt
        finalpoint = finalpt
        initx = int(initpoint[0])
        inity = int(initpoint[1])
        finalx = int(finalpoint[0])
        finaly = int(finalpoint[1])
        label_width = abs(finalx - initx)
        label_height = abs(finaly - inity)
        center_x = format(abs(((finalx + initx)/2)/width), '.6f')
        center_y = format(abs(((finaly + inity) / 2) / height-1), '.6f')
        relative_width = format(label_width/width, '.6f')
        relative_height = format(label_height/height, '.6f')
        string = string + f'{dictionary[name]} {center_x} {center_y} {relative_width} {relative_height}\n'
    return string

def convert_flipmirror(dic):
    width = int(dic['Image_width'])
    height = int(dic['Image_height'])
    points = ((item['Init Pos'], item['final Pos'], item['Name']) for item in dic['Label'])
    string = ''
    for initpt, finalpt, name in points:
        initpoint = initpt
        finalpoint = finalpt
        initx = int(initpoint[0])
        inity = int(initpoint[1])
        finalx = int(finalpoint[0])
        finaly = int(finalpoint[1])
        label_width = abs(finalx - initx)
        label_height = abs(finaly - inity)
        center_x = format(abs(((finalx + initx)/2)/width-1), '.6f')
        center_y = format(abs(((finaly + inity) / 2) / height-1), '.6f')
        relative_width = format(label_width/width, '.6f')
        relative_height = format(label_height/height, '.6f')
        string = string + f'{dictionary[name]} {center_x} {center_y} {relative_width} {relative_height}\n'
    return string

# Convert Json file to yolov5 format labeling txt file
def convert_json2label(path0, savepath):
    directory = os.scandir(path0)
    for file in directory:
        if file.name.endswith('.json'):
            file_path = os.path.join(path0, file.name)
            basename = os.path.splitext(os.path.basename(file_path))[0]
            with open(file_path) as fp:
                q = json.load(fp)
                string = convert(q)
                with open(rf'{savepath}\{basename}.txt', mode='w') as fp2:
                    fp2.write(string)


def conver_json2txt_mirror(path, savepath):
    directory = os.listdir(path)
    length = len(directory)
    open_dir(savepath)
    for index, file in enumerate(directory):
        if file.endswith('.json'):
            file_path = os.path.join(path, file)
            basename = os.path.splitext(os.path.basename(file_path))[0]
            with open(file_path) as fp:
                q = json.load(fp)
                string = convert_mirror(q)
                with open(rf'{savepath}\{basename}.txt', mode='a') as fp2:
                    fp2.write(string)
        print_result(index+1, length)


def conver_json2txt_flip(path, savepath):
    directory = os.listdir(path)
    length = len(directory)
    open_dir(savepath)
    for index, file in enumerate(directory):
        if file.endswith('.json'):
            file_path = os.path.join(path, file)
            basename = os.path.splitext(os.path.basename(file_path))[0]
            with open(file_path) as fp:
                q = json.load(fp)
                string = convert_flip(q)
                with open(rf'{savepath}\{basename}.txt', mode='a') as fp2:
                    fp2.write(string)
        print_result(index+1, length)

def conver_json2txt_flipmirror(path, savepath):
    directory = os.listdir(path)
    length = len(directory)
    open_dir(savepath)
    for index, file in enumerate(directory):
        if file.endswith('.json'):
            file_path = os.path.join(path, file)
            basename = os.path.splitext(os.path.basename(file_path))[0]
            with open(file_path) as fp:
                q = json.load(fp)
                string = convert_flipmirror(q)
                with open(rf'{savepath}\{basename}.txt', mode='w+') as fp2:
                    fp2.write(string)
        print_result(index+1, length)


#conver_json2txt_flipmirror(r'C:\Users\Public\Pictures\json', r'C:\Users\Public\Pictures\flip_mirror')

TRAIN_DATA_RATIO = 0.2
origi_dir = r'C:\Users\Public\Pictures\flip'
dist_dir = r'C:\Users\Public\Pictures\dsit'
suffix = '.txt'


def split_dataset_2_train_val(ratio: float, origi_dir: str, dist_trainimg_dir: str, dist_trainlabel_dir: str,
                              dist_valimg_dir: str, dist_vallabel_dir: str, image_suffix: str, label_suffix: str):
    real_length = set([file.name for file in os.scandir(origi_dir) if file.name.endswith(image_suffix)])
    length = len(real_length)
    limit = (1-ratio)*length
    count = 0
    for name in real_length:
        if count <= limit:
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
            print_result(count, limit)
            count += 1
        else:
            pass
    real_length2 = [file.name for file in os.scandir(origi_dir) if file.name.endswith(image_suffix)]
    for name in real_length2:
        basename = os.path.splitext(name)[0]
        newname = f'{basename}{label_suffix}'
        label_file_path = os.path.join(origi_dir, newname)
        src = os.path.join(origi_dir, name)
        try:
            shutil.move(src, dist_valimg_dir)
            shutil.move(label_file_path, dist_vallabel_dir)
        except Exception as e:
            print(e)
            break
        print_result(count, len(real_length2))
    else:
        pass
    print('\nFile Transfer Successfully!')


def rename(dir, dst, name, suffix, start):
    open_dir(dir)
    file_list = os.listdir(dir)
    length = len(file_list)
    count = 0
    for index, file in enumerate(file_list):
        if file.endswith(suffix):
            file_path = os.path.join(dir, file)
            src = file_path
            num = start + count
            newname = f'{name}{num}{suffix}'
            dsti = os.path.join(dst, newname)
            os.rename(src, dsti)
            count += 1
        print_result(index+1, length)


#rename(r'C:\Users\Public\Pictures\flip_mirror', r'C:\Users\Public\Pictures\data\lABEL', 'Image', '.txt', 1883)


split_dataset_2_train_val(0.8, r'C:\Users\Public\Pictures\data\DATASET',
                          r'C:\Users\Public\Pictures\VOCdevkit\images\Val',
                          r'C:\Users\Public\Pictures\VOCdevkit\labels\Val',
                          r'C:\Users\Public\Pictures\VOCdevkit\images\Train',
                          r'C:\Users\Public\Pictures\VOCdevkit\labels\Train',
                          '.png', '.txt')

