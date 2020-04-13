import os
import glob

path = "./like"
files = glob.glob(path + '/*')

for i, f in enumerate(files):
    os.rename(f, os.path.join(path, 'like_' + '{0:03d}'.format(i)) + '.jpg')

path = "./neutral"
files = glob.glob(path + '/*')

for i, f in enumerate(files):
    os.rename(f, os.path.join(path, 'neutral_' + '{0:03d}'.format(i)) + '.jpg')

path = "./dislike"
files = glob.glob(path + '/*')

for i, f in enumerate(files):
    os.rename(f, os.path.join(path, 'dislike_' + '{0:03d}'.format(i)) + '.jpg')
