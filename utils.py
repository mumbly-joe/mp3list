import os

def listdirs():

    for dirpath, dirnames, filenames in os.walk('E://Media/Music/'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            print(os.path.join(dirpath, subdirname))

def musicfile(basedir):
    filelist=[]
    for dirpath, dirnames, filenames in os.walk(basedir): #eg. basedir= E://Media/Music/
        # print path to all filenames.
        for filename in filenames:
            filelist.append(os.path.join(dirpath, filename))
    return filelist

def savelist(mylist):
    fid=open('list.txt', 'w', encoding='utf-8')
    for myfile in mylist:
        fid.writelines(myfile+'\n')
    fid.close()