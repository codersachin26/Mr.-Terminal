import os
import platform
from cmd_classes import Response
from helper_func import convert_date


""" making func which return cmd level result    """ 




def command_error():    # show error
    SRED = '\033[31m'    
    CEND = '\033[0m'
    print('Error: %s this command is not recognized %s' % (SRED,CEND))


def list_content(flag=None):          # return all content in current working dir
    res = Response()            
    if flag == '-l':
        dir_content = os.scandir()
        for entry in dir_content:
            line_info = entry.stat()
            line = f'\t{entry.name}\t\t\t Last Modified: {convert_date(line_info.st_mtime)}'
            res.content.append(line)
        return res
    else:
        content = os.listdir()
        res.content = content
        return res


def change_dir(path):
    res = Response()              # change dir 
    try:
        change = os.chdir(path)
    except FileNotFoundError:
        res.err = 'Error: dir not exists '
        return res

    return res


def pwd():                    # return present working dir path
    return os.getcwd()



def make_dir(dir_name):         # create new dir
    res = Response()
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        res.err = 'Error: %s directory already exists' % dir_name
        return res
    


def read_file(file_name=None):           # read file content
    res = Response()
    if file_name is None:
        files = list(filter(os.path.isfile, os.listdir()))
        res.content.extend(files)
        return res
    try:
        file = open(file_name)
        file_content = file.read()
        res.content.append(file_content)
        return res
    except FileNotFoundError:
        res.err = "Error: file not found "
        return res


def remove_file(file_name):              # remone file
    res = Response()
    try: 
        os.remove(file_name)
        content = f' {file_name} file successfully remove'
        res.err = None
        res.content.append(content)
        return res

    except OSError:
        res.err = f'Error: {file_name} not a valid filename'
        return res


def remone_dir(dir_name):             # remove dir
    res = Response()
    try:
        os.rmdir(dir_name)
        content = f'{dir_name} directory successfully deleted '
        res.content.append(content)
        return res
    except OSError:
        res.err = f'Error: {dir_name} directory is not empty '
        return res
        