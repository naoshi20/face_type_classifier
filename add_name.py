import os
import glob

path = "./bing/imgs"
files = glob.glob(path + '/*')

for i, f in enumerate(files):
    os.rename(f, os.path.join(path, os.path.basename(f)) + '.jpg')
