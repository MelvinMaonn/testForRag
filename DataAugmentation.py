from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='constant',
        cval=0)

img = load_img('G:\dw\J01_2018.06.13 13_25_43.jpg')  # 这是一个PIL图像
x = img_to_array(img)  # 把PIL图像转换成一个numpy数组，形状为(3, 150, 150)
x = x.reshape((1,) + x.shape)  # 这是一个numpy数组，形状为 (1, 3, 150, 150)

# 下面是生产图片的代码
# 生产的所有图片保存在 `preview/` 目录下
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='G:\dw4', save_prefix='吊纬', save_format='jpeg'):
    i += 1
    if i > 50:
        break  # 否则生成器会退出循环