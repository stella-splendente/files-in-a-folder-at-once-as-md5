#-*-coding : utf-8-*-

import os
import hashlib
import glob

f = open('/Users/lucete/Desktop/hash.txt','w')

def file_md5(filename):
    md5 = hashlib.md5()
    with open(filename,'rb') as f:
        for chunk in iter(lambda: f.read(8192),b""):
            md5.update(chunk)
    return md5.hexdigest()

path = '/Users/lucete/Downloads'
array = os.listdir(path)

i=0
for path, dirs, files in os.walk(path):
    for file in files:
        flist = glob.glob(os.path.join(path, file))

        for i in flist:
            print(i,os.path.getsize(i),file_md5(i))
            f.write(i+' : '+file_md5(i)+'\n')
f.close()
