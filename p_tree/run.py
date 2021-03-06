# coding: utf-8
from __future__ import division, unicode_literals, print_function  # for compatibility with Python 2 and 3
import os

try:
    from dbox import prepare_photos
    from utilities import *

except:
    from .dbox import prepare_photos
    from .utilities import *

import math
import cv2
import shutil

import numpy as np
import pandas as pd

import matplotlib.mlab as mlab
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy import ndimage
from scipy import ndimage as ndi

from skimage.morphology import watershed
from skimage import data, io, filters, color, morphology, util, feature
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte
from skimage.filters import sobel
from PIL import Image
import pims
import trackpy as tp

"""
This program runs the cfus counting program using just a dropbox link to images.
"""

__author__ = 'George Pamfilis'


class CountColonies(object):

    def __init__(self, url):
        self.url = url

    def handle_directories(self):
        for f in ['./p_tree/data', './p_tree/temp', './p_tree/seed_images']:
            try:
                print('Making Directory: ',f)
                os.mkdir(f)
            except Exception as e:
                print(e)
                erase_directory_contents(f)
        return None

    def pre_fit(self, mean_diameter_pixels=41):
        print('Erasing Directory Contents')
        erase_directory_contents('./p_tree/temp/')
        erase_directory_contents('./p_tree/seed_images/')
        print('Rotating Base Image')
        rotate_images(base_image='./p_tree/data/'+os.listdir('./p_tree/data/')[0])
        file_paths = ['./p_tree/seed_images/' + f for f in os.listdir('./p_tree/seed_images/')]
        counts = []
        for file_path in file_paths[:1]:
            print(file_path)
            cut_in_quads(f_name=file_path)
            cut_in_half(f_name=file_path, orientation='horizontal')
            cut_in_half(f_name=file_path, orientation='vertical')
            cou = filter_out_colonies(file_path)
            counts.append(cou)

        for c, count in enumerate(counts):
            for i in range(len(count)):
                try:
                    plt.imsave('./p_tree/temp/bw_' + str(c) + '_' + str(i) + '.png', arr=counts[c][i])
                except Exception as e:
                    print(e)

        full_frames = pims.ImageSequence('./p_tree/temp/*.png', as_grey=True)
        frame = full_frames[0]
        f = tp.locate(frame, mean_diameter_pixels)
        f.head(), f.shape
        plt.figure()
        tp.annotate(f, frame)
        return mean_diameter_pixels

    def count_one(self, mean_diameter_pixels=11, base_image=None):
        # './p_tree/data/'+os.listdir('./p_tree/data/')[0]
        print('Count One: ',base_image)
        # self.handle_directories()
        erase_directory_contents('./p_tree/temp/')
        erase_directory_contents('./p_tree/seed_images/')
        rotate_images(base_image=base_image, angle=180, n=2)
        file_paths = ['./p_tree/seed_images/' + f for f in os.listdir('./p_tree/seed_images/')]
        counts = []
        for file_path in file_paths[:]:
            print(file_path)
            cut_in_quads(f_name=file_path)
            cut_in_half(f_name=file_path, orientation='horizontal')
            cut_in_half(f_name=file_path, orientation='vertical')
            cou = filter_out_colonies(file_path)
            counts.append(cou)

        colo = []
        for c, count in enumerate(counts):
            print('seeds: ', c)
            for i in range(len(count)):
                print('saving: ', i)
                plt.imsave('./p_tree/temp/bw_' + str(0) + '_' + str(i) + '.png', arr=counts[c][i])
            full_frames = pims.ImageSequence('./p_tree/temp/*.png', as_grey=True)
            ec = []
            for f, frame in enumerate(full_frames):
                print('reading: ', f)
                f = tp.locate(frame, mean_diameter_pixels)
                # enter mass filter
                ec.append(f.shape[0])
            print('done: ', c)
            colo.append(ec)

        final = []
        for col in colo:
            final.append(col[:1] + [sum(col[1:5])] + [sum(col[5:7])] + [sum(col[7:])])

        data = np.array(final)

        df = pd.DataFrame(data, columns=['F', 'Q', 'HH', 'HV'])
        return df

    def count_all(self, mean_diameter_pixels=11, base_images=None):
        # ['./p_tree/data/'+f for f in os.listdir('./p_tree/data/')]
        dfs = []

        for base_image in base_images:
            print(base_image)
            df = self.count_one(mean_diameter_pixels=mean_diameter_pixels, base_image=base_image)
            dfs.append(df)

        return dfs

    def main(self):
        try:
            os.mkdir('p_tree')
        except Exception as e:
            print(e)
        print('Handleling Directories')
        self.handle_directories()
        prepare_photos(self.url)
        pixel_dc = 41
        while True:
            pixel_dc = self.pre_fit(mean_diameter_pixels=pixel_dc)
            accept = input('Accept?: ')
            if accept == 'y':
                break
            else:
                pixel_dc = int(input('Pixels: '))
        print(os.listdir('./p_tree/data/'))
        dfs = self.count_all(mean_diameter_pixels=pixel_dc, base_images=['./p_tree/data/'+f for f in os.listdir('./p_tree/data/')])
        # dfs=None
        return dfs


if __name__ == '__main__':
    url = 'https://www.dropbox.com/sh/vq4wb9fd9k1fz49/AADLR3IIgj8lMWs8m9QLzdPoa?dl=1'
    cc = CountColonies(url=url)
    dfs = cc.main()
    print(dfs)
