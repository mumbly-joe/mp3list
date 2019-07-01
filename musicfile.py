import os

for dirname, dirnames, filenames in os.walk('E://Media/Music/'):
      # print path to all filenames.
    for filename in filenames:
        print(os.path.join(dirname, filename))
