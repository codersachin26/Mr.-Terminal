import os
import platform
from help_func import convert_date


""" making func which return cmd level result    """ 


def list_content(flag=None):
    info = {}
    content = []     # return all content in current working dir
    if flag == '-l':
        dir_content = os.scandir()
        for entry in dir_content:
            if entry.is_file():
                info = entry.stat()
                line = f'\t\t{entry.name}\t\t Last Modified: {convert_date(info.st_mtime)}'
                content.append(line)
        info['content'] = content
        info['err'] = False
        return content
    else:
        content = os.listdir()
        info['err'] = False
        info['content'] = content
        return info


def change_dir(path):
    info = {}              # change dir 
    try:
        change = os.chdir(path)
    except FileNotFoundError:
        err = ' file not found '
        info['err'] = err
        return info
    info['err'] = False
    info['content'] = False
    return info


def pwd():                    # return present working dir path
    return os.getcwd()



def make_dir(dir_name):
    info = {}
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        err = '%s directory already exists' % dir_name
        info['err'] = err
    