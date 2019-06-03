os.chdir('C:/Users/Ing. Mario/Documents/python/animales/png')

for f in os.listdir():

    ext = os.path.splitext(f)[-1]
    # print (os.path.splitext(f)[-1])

    files = os.path.splitext(f)[0]
    name_large = files.split(' ')
    if len(name_large) > 1 :
        print(len(name_large))
        final = files.split(' ')[0]
        if os.path.exists(final + ext):
            os.remove(files + ext)
        else:
            os.rename(f,final + ext)
