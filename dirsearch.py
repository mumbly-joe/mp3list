import os

from glob import glob
from sys import platform

base_dir = "E://Media/Music/"
dirname = ()
filename = ()

for base_dir, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        print(os.path.join(dirname, filename))