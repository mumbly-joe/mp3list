import os

for dirname, dirnames, filenames in os.walk('E://Media/Music/'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))