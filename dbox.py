# coding: utf-8

import urllib.request
import os
from utilities import extract_zip, erase_directory_contents

"""
Explain WTF your doing
"""

__author__ = 'George Pamfilis'


def get_files(url, loc='./data/photos.zip'):
    urllib.request.urlretrieve(url, loc)
    return None


def prepare_photos(url):
    try:
        print('Creating Data Directory')
        os.mkdir('data')
    except Exception as e:
        print(e)
        print('Clearing Directory')
        erase_directory_contents(folder='./data')
    get_files(url=url)
    extract_zip(path_to_zip_file='./data/photos.zip', directory_to_extract_to='./data/')
    os.remove('./data/photos.zip')


if __name__ == '__main__':
    pass

