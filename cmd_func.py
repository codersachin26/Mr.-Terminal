import os
import platform
from help_func import convert_date


""" making func which return cmd level result    """ 




def command_error():
    SRED = '\033[31m'    # Warning color
    CEND = '\033[0m'
    print('%s this command is not recognized %s' % (SRED,CEND))


def list_content(flag=None):          # return all content in current working dir
    info = {}             # hold func related data     
    content = []           # func content
    if flag == '-l':
        dir_content = os.scandir()
        for entry in dir_content:
            if entry.is_file():
                line_info = entry.stat()
                line = f'\t\t{entry.name}\t\t Last Modified: {convert_date(line_info.st_mtime)}'
                content.append(line)
        info['content'] = content
        info['err'] = False
        return info
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



def make_dir(dir_name):         # create new dir
    info = {}
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        err = '%s directory already exists' % dir_name
        info['err'] = err
    

