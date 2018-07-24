# -*- coding=utf-8 -*-

import os
import math


def file_name(file_dir):

    for root, dirs, files in os.walk(file_dir):

        for onedir in dirs:

            last_dir = os.path.join(root, onedir)
            files = os.listdir(last_dir)
            L = []
            for file in files:
                if os.path.splitext(file)[1] == '.jpg':
                    L.append(os.path.join(last_dir, file))

            num = len(L)
            print(num)





if __name__=="__main__":

    file_name('G:\Rag\TrainOrign48\RagTrain')