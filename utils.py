import os

def listdirs():

    for dirpath, dirnames, filenames in os.walk('E://Media/Music/'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            print(os.path.join(dirpath, subdirname))

def musicfile():

    for dirpath, dirnames, filenames in os.walk('E://Media/Music/'):
      # print path to all filenames.
        for filename in filenames:
            print(os.path.join(dirpath, filename))