# -*- coding=utf-8 -*-

import os
import math
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img




def file_name(file_dir):

    f = open('test.txt', 'w')

    for root, dirs, files in os.walk(file_dir):

        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                f.write(file + '\n')

        f.close()



if __name__ == "__main__":

    file_name('G:\Rag\RagTest\\xuelang_round1_test_a_20180709')
