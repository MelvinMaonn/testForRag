# -*- coding=utf-8 -*-

import os
import math
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img




def file_name(file_dir):



    #L=[]
    for root, dirs, files in os.walk(file_dir):
        '''
        for file in files:  
            if os.path.splitext(file)[1] == '.jpeg':  
                L.append(os.path.join(root, file))  
    return L  
        '''
        for onedir in dirs:
            global c_num
            c_num += 1
            #print(os.path.join(root, onedir))
            last_dir = os.path.join(root, onedir)
            files = os.listdir(last_dir)
            L = []
            for file in files:
                if os.path.splitext(file)[1] == '.jpg':
                    L.append(os.path.join(last_dir, file))

            num = len(L)
            expansion_num = math.ceil(400 / num)
            #print(num)

            #os.makedirs('G:\Rag\TrainSet2\\' + str(c_num))
            for file in L:
                img = load_img(file)  # 这是一个PIL图像
                x = img_to_array(img)  # 把PIL图像转换成一个numpy数组，形状为(3, 150, 150)
                x = x.reshape((1,) + x.shape)  # 这是一个numpy数组，形状为 (1, 3, 150, 150)

                i = 0
                for batch in datagen.flow(x, batch_size=1, save_to_dir='G:\Rag\TrainSet2\\'+str(c_num), save_prefix='1', save_format='jpg'):
                    i += 1
                    if i > expansion_num:
                        break  # 否则生成器会退出循环



if __name__=="__main__":
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='constant',
        cval=0)

    c_num = 0
    file_name('G:\Rag\TrainOrign48\RagTrain')
    #file_name('G:\Rag\\train\\xuelang_round1_train_part2_20180705')
    #file_name('G:\Rag\\train\\xuelang_round1_train_part3_20180709')