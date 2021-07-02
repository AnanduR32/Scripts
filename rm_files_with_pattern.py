import sys, os, re

path = sys.argv[1]
pattern = sys.argv[2]
file_names = os.listdir(f'{path}')

for file in file_names:
    if(bool(re.search(f'{pattern}',file))==True):
        os.remove(path+'/'+file)
