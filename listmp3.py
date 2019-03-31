import os
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


