import numpy as np
from PIL import Image
from io import BytesIO
import h5py
import os
import random


img_size = (128, 128)

filenames = os.listdir("./trimed") #dataというフォルダにある画像を読み込み
num_files = len(filenames) #画像数を把握し
num_train = int(num_files / 10 * 7)
num_test = num_files - num_train
imgs = []
labels = []
for i in range(num_files):
    imgname = filenames[i]
    try:
        originalImg = Image.open("./trimed/" + imgname)
        resizeImg = originalImg.resize(img_size)
        w, h = resizeImg.size
        pixels = []

        img = []
        for y in range(h):
            pixels = []
            for x in range(w):
                pixel = []
                color = resizeImg.getpixel((x, y))
                pixel.append(color[0])
                pixel.append(color[1])
                pixel.append(color[2])
                pixels.append(pixel)
            img.append(pixels)
        imgs.append(img)

        character = imgname.split("_")[-2]
        print(character)
        if character == "like":
            labels.append(0)
        if character == "neutral":
            labels.append(1)
        if character == "dislike":
            labels.append(2)

    except:
        print("read error:", imgname)
        num_files -= 1
        continue

imgs_array = np.array(imgs)
label_array = np.array(labels)

im_labels = list(zip(imgs, labels))
#print(im_labels[0:1])

random.sample(im_labels, len(im_labels)) # 重複なし。　random.shuffle()はNoneを返す。
im_labels = sorted(im_labels, key=lambda k: random.random())
#print(im_labels[0:1])
#print(im_labels)
x_train = []
y_train = []
x_test = []
y_test = []

for i in range(num_train):
    x_train.append(im_labels[i][0])
    y_train.append(im_labels[i][1])

for i in range(num_test):
    x_test.append(im_labels[i+2][0])
    y_test.append(im_labels[i+2][1])

print(len(x_train),len(y_train),len(x_test),len(y_test))

classes = [0, 1, 2]


with h5py.File('datasets/train_faces_' + str(img_size[0]) +'.h5', 'w') as f:
    f.create_dataset('train_set_x', data=x_train)
    f.create_dataset('train_set_y', data=y_train)

with h5py.File('datasets/test_faces_' + str(img_size[0]) +'.h5', 'w') as f:
    f.create_dataset('test_set_x', data=x_test)
    f.create_dataset('test_set_y', data=y_test)
    f.create_dataset('list_classes', data=classes)


#画像とラベルの一致を確認。
im1 = x_train[3]
im2 = Image.new("RGB", (h,w))
for y in range(h):
    for x in range(w):
        r = im1[x][y][0]
        g = im1[x][y][1]
        b = im1[x][y][2]
        im2.putpixel((x,y),(r,g,b))
im2.show()
label = y_train[3]
print("This image represents " + str(label) + ".")
