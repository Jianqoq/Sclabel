import json
import shutil
from Image_process import *
from file_manipulation import *

# ======================================================================================================================
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
# ======================================================================================================================

def mirror(Savelocation, Image_dir):
    open_dir(Savelocation, False)
    directory = os.listdir(Image_dir)
    length = len(directory)
    for index, file in enumerate(directory):
        path = os.path.join(Image_dir, file)
        savepath = os.path.join(Savelocation, file)
        flip(path, savepath, None)
        print_result(index + 1, length)


def flip(Savelocation, Image_dir):
    open_dir(Savelocation, False)
    directory = os.listdir(Image_dir)
    length = len(directory)
    for index, file in enumerate(directory):
        path = os.path.join(Image_dir, file)
        savepath = os.path.join(Savelocation, file)
        flip2(path, savepath, None)
        print_result(index+1, length)


# ======================================================================================================================
def convert(dic, classdict, mode):
    width = int(dic['Image_width'])
    height = int(dic['Image_height'])
    points = ((item['Init Pos'], item['final Pos'], item['Name']) for item in dic['Label'])
    final_list = [calculate(initpt, finalpt, name, width, height, classdict, mode) for initpt, finalpt, name in points]
    return ''.join(final_list)


def calculate(initpt, finalpt, name, width, height, classdict, mode: str):
    initpoint = initpt
    finalpoint = finalpt
    initx = float(initpoint[0])
    inity = float(initpoint[1])
    finalx = float(finalpoint[0])
    finaly = float(finalpoint[1])
    di = {
        'normal': (format(abs(((finalx + initx) / 2) / width), '.6f'),
                   format(abs(((finaly + inity) / 2) / height), '.6f')),
        'mirror': (format(abs(((finalx + initx) / 2) / width - 1), '.6f'),
                   format(abs(((finaly + inity) / 2) / height), '.6f')),
        'flip':   (format(abs(((finalx + initx) / 2) / width), '.6f'),
                   format(abs(((finaly + inity) / 2) / height - 1), '.6f')),
        'flip_mirror': (format(abs(((finalx + initx) / 2) / width - 1), '.6f'),
                        format(abs(((finaly + inity) / 2) / height - 1), '.6f')),
    }
    label_width = abs(finalx - initx)
    label_height = abs(finaly - inity)
    center_x, center_y = di[mode]
    relative_width = format(label_width / width, '.6f')
    relative_height = format(label_height / height, '.6f')
    return f'{classdict[name]} {center_x} {center_y} {relative_width} {relative_height}\n'
# ======================================================================================================================


# Convert Json file to yolov5 format labeling txt file
def convert_json2label(path: str, savepath: str, classdict: dict, mode: str):
    directory = os.listdir(path)
    for index, file in enumerate(directory):
        if file.endswith('.json'):
            file_path = os.path.join(path, file)
            basename = os.path.splitext(os.path.basename(file_path))[0]
            with open(file_path) as fp:
                q = json.load(fp)
                with open(rf'{savepath}\{basename}.txt', mode='w') as fp2:
                    fp2.write(convert(q, classdict, mode))
        print_result(index + 1, len(directory))


def split_dataset_2_train_val(ratio: float, origi_dir: str, dist_trainimg_dir: str, dist_trainlabel_dir: str,
                              dist_valimg_dir: str, dist_vallabel_dir: str, image_suffix: str, label_suffix: str):
    real_length = [file.name for file in os.scandir(origi_dir) if file.name.endswith(image_suffix)]
    length = len(real_length)
    limit = ratio*length
    for index, name in enumerate(real_length):
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
            print_result(index + 1, limit)
        else:
            pass
    real_length2 = [file.name for file in os.scandir(origi_dir) if file.name.endswith(image_suffix)]
    for index, name in enumerate(real_length2):
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
        print_result(index + 1, len(real_length2))
    else:
        pass
    print('\nFile Transfer Successfully!')
# ======================================================================================================================

def rename(dir, dst, name, suffix, start):
    open_dir(dir, False)
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


