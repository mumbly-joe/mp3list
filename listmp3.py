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


base_dir = "E://Media/Music/" 
mymp3s = findmp3s (base_dir)
print(f"found {len(mymp3s)}")
for mp3 in mymp3s:
    print(f'found the mp3 {mp3}')



print('the program has ended')