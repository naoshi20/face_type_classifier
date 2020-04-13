import os
import glob

path = "./bing/その他"
files = glob.glob(path + '/*')

for i, f in enumerate(files):
    os.rename(f, os.path.join(path, 'others_' + '{0:03d}'.format(i)))

path = "./bing/ルフィ"
files = glob.glob(path + '/*')

for i, f in enumerate(files):
    os.rename(f, os.path.join(path, 'ruffy_' + '{0:03d}'.format(i)))

path = "./bing/ゾロ"
files = glob.glob(path + '/*')

for i, f in enumerate(files):
    os.rename(f, os.path.join(path, 'zoro_' + '{0:03d}'.format(i)))
