import os
# os.rename(r'1.txt',r'2.txt')

path = 'files' + '/'
files = os.listdir(path)

for file in files:
    filename = file.split('.')[0]
    ext = file.split('.')[1]
    new_filename = filename.split('_')[0] + '.' + ext
    old_fullpath = path + filename + '.' + ext
    new_fullpath =  path + new_filename
    os.rename(old_fullpath,new_fullpath)
