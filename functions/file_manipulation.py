import os
import configparser
import win32gui
import win32ui
import win32con
import win32api


def get_label_filename(path):
    basename = os.path.splitext(os.path.basename(path))[0]
    directory = os.path.dirname(os.path.realpath(path))
    save_location = f'{directory}\{basename}.json'
    return save_location


def h_update(win, section, item, widget):
    height = widget.text()
    win.height = height
    config = configparser.ConfigParser()
    config.read(f'{win.path}\config.ini')
    config.set(section, item, height)
    with open(f'{win.path}\config.ini', mode='w') as file:
        config.write(file)
        file.close()
    win.signal.emit(win.width, win.height)


def w_update(win, section, item, widget):
    width = widget.text()
    win.width = width
    config = configparser.ConfigParser()
    config.read(f'{win.path}\config.ini')
    config.set(section, item, width)
    with open(f'{win.path}\config.ini', mode='w') as file:
        config.write(file)
        file.close()
    win.signal.emit(win.width, win.height)


def lastpos(path, pos):
    config = configparser.ConfigParser()
    config.read(rf'{path}\config.ini')
    config.set('Saving setting', 'last_posx', str(pos.x()))
    config.set('Saving setting', 'last_posy', str(pos.y()))
    with open(rf'{path}\config.ini', mode='w') as fp:
        config.write(fp)
        fp.close()


def checkbox_update(path, key, statement):
    config = configparser.ConfigParser()
    config.read(f'{path}\config.ini')
    config.set('Saving setting', f'{key}', str(statement))
    with open(f'{path}\config.ini', mode='w') as file:
        config.write(file)
        file.close()


def readdir(self, path):
    open_dir(path, False)
    software_width, software_height = self.frameSize().width(), self.frameSize().height()
    config = configparser.ConfigParser()
    config.read(f'{path}\config.ini')
    Save_setting = ['Location', 'Image name', 'Save Location',
                    'Augment Image name', 'Augment Data load',
                    'width', 'height', 'last_posx', 'last_posy',
                    'check', 'Quality', 'Image Format', 'Label Location',
                    'Labeling Function', 'Last annotation file']
    dict = {'Location': 'C:/Users/Public/Pictures/ImageSet',
            'Image name': 'Image',
            'Save Location': 'C:/Users/Public/Pictures/Data_aug_ImageSet',
            'Augment Image name': 'AugImg',
            'Augment Data load': r'C:/Users/123/Pictures/Aug_Data',
            'width': 340,
            'height': 340,
            'last_posx': int((self.screen().size().width() - software_width) // 2),
            'last_posy': int((self.screen().size().height() - software_height) // 2),
            'check': str(True),
            'Quality': 100,
            'Image Format': 0,
            'Label Location': 'C:/Users/Public/Pictures/Data_aug_ImageSet_Label',
            'Labeling Function': str(True),
            'Last annotation file': None
            }
    index = 0
    for item in Save_setting:
        if not config.has_option('Saving setting', item):
            with open(f'{path}\config.ini', mode='w+') as file:
                key = Save_setting[index]
                if config.has_section('Saving setting'):
                    config.set('Saving setting', key, str(dict[key]))
                    config.write(file)
                else:
                    config['Saving setting'] = {key: dict[key]}
                    config.write(file)
                file.close()
        index += 1


def window_capture(filename, x, y, sizex, sizey):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((x, y), (sizex, sizey), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


def updatefilename(path, name, section, item, config_name):
    config = configparser.ConfigParser()
    config.read(rf'{path}\{config_name}')
    config.set(section, item, name)
    with open(rf'{path}\{config_name}', mode='w') as file:
        config.write(file)


def autosave(win, filename, section, item):
    config = configparser.ConfigParser()
    config.read(f'{win.path}\{win.configname}')
    config.set(section, item, filename)
    with open(f'{win.path}\{win.configname}', mode='w') as file:
        config.write(file)
        file.close()


def read_savedfile(win):
    config = configparser.ConfigParser()
    config.read(f'{win.path}\{win.configname}')
    path = config.get('Saving setting', 'last annotation file')
    return path


def open_dir(path, openfile: bool):
    if not os.path.exists(path):
        os.makedirs(path)
    os.startfile(path) if openfile else True



