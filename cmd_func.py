import os
import platform


""" making func which return cmd level result    """ 


def list_content():                 # return all content in current working dir
    content = os.listdir()
    return content


def change_dir(path):              # change dir 
    try:
        change = os.chdir(path)
    except FileNotFoundError:
        return False
    return True


def pwd():
    return os.getcwd()
