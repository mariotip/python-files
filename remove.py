import os
os.chdir('C:/Users/Ing. Mario/Documents/python/animales/png')
for f in os.listdir():
    files = os.path.splitext(f)[0]
    name_large = files.split(' ')
    if len(name_large) > 1 :
        print(len(name_large))
        os.remove(files+'.png')
