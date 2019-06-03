import os
# import request
os.chdir('C:/Users/Ing. Mario/Documents/python/animales/png')
for f in os.listdir():
    # name_files = os.path.(f)
    # dts = str(name_files) + '.jpg'
    # os.path.splitext("sample.txt")[0]
    # print(str(f).split('.')[0])
    files = os.path.splitext(f)[0]
    name_large = files.split(' ')
    if len(name_large) > 1 :
        print(len(name_large))
        os.remove(files+'.png')

    # else
    #     os.rename(f,final+'.jpg')

    # final = files.split(' ')[0]
    # if os.path.exists(final+'.jpg'):
    # else:
    #     print('el archivo no existe')
