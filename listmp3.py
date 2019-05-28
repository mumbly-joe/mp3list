import os
from glob import glob
from sys import platform

print("list mp3s")

if platform == "linux" or platform == "linux2":
    print('determined that we are running on linux')
    # linux
elif platform == "darwin":
    # OS X
    print('determined that we are running on Mac OSX')
elif platform == "win32":
    # Windows...
    print('determined that we are running on WinBlows')

def findmp3s (basedir):
    allmp3s = glob (basedir + "*.mp3")
    return allmp3s

def findflacs (basedir):
    allflacs = glob (basedir + '*.flac')
    return allflacs

def findoggs (basedir):
    alloggs = glob (basedir + '*.ogg')
    return alloggs

def findallext (basedir):
    allext = glob (basedir + '*.mp3 *.ogg *.flac')
    return allext

def findalldir (basedir):
    alldir = []
    for music in glob (basedir + '*'):
        if os.path.isdir (music):
            alldir.append (music)
    return alldir
     
base_dir = "E://Media/Music/" 
mymp3s = findmp3s (base_dir)
myflacs = findflacs (base_dir)
myoggs = findoggs (base_dir)
mymusic = findallext (base_dir)

mydirs = findalldir (base_dir)

print(f"found {len(mymp3s)}")
for mp3 in mymp3s:
    print(f'found the mp3 {mp3}')

for flac in myflacs:
    print(f'found the flsc {flac}')

for ogg in myoggs:
    print(f'found the ogg {ogg}')

for files in mymusic:
    print(f'{mp3}')

count=0

for dir in mydirs:
    print(dir)

    subdirs=findmp3s(dir)
    print(count,subdirs)
    count=count+1

print('the program has ended')