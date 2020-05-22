import os
import platform
from cmd_classes import Response
from helper_func import convert_date
import shutil


""" making func which return cmd level result    """ 




def command_error():    # show error
    SRED = '\033[31m'    
    CEND = '\033[0m'
    print('Error: %s command is not recognized %s' % (SRED,CEND))


def list_content(arg):          # return all content in current working dir
    flag = arg[0]
    res = Response()            
    if flag == '-l':
        dir_content = os.scandir()
        for entry in dir_content:
            line_info = entry.stat()
            line = f'\t{entry.name}\t\t\t Last Modified: {convert_date(line_info.st_mtime)}'
            res.content.append(line)
        return res
    else:
        if flag is None:
            content = os.listdir()
            res.content = content
            return res
        else:
            res.err = 'Error: %s flag is not recognized in ls command' % flag
            return res


def change_dir(arg):  # change dir 
    path = arg[0]
    res = Response() 
    if path is None:
        os.chdir('/')
                     
    try:
        change = os.chdir(path)
    except FileNotFoundError:
        res.err = 'Error: dir not exists '
        return res

    return res


def pwd():                    # return present working dir path
    return os.getcwd()



def make_dir(arg):         # create new dir
    dir_name = arg[0]
    res = Response()
    try:
        os.mkdir(dir_name)
        return res
    except FileExistsError:
        res.err = 'Error: %s directory already exists' % dir_name
        return res
    


def read_file(arg):           # read file content
    file_name = arg[0]
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


def remove_file(arg):              # remone file
    file_name = arg[0]
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


def remone_dir(arg):             # remove dir
    dir_name = arg[0]
    res = Response()
    try:
        os.rmdir(dir_name)
        content = f'{dir_name} directory successfully deleted '
        res.content.append(content)
        return res
    except OSError:
        res.err = f'Error: {dir_name} directory is not empty '
        return res
        


def copy_file(arg):
    src = arg[0]
    dst = arg[1]
    res = Response()
    try:
        file_name = os.path.basename(src)
        dst = os.path.join(dst,file_name)
        shutil.copyfile(src,dst)
    except shutil.SameFileError:
        res.err = 'Source and destination represents the same file.'
    return res

