import sys, os, re
from pathlib import Path

if(__name__=='__main__'):
    path = sys.argv[1]
    dest = sys.argv[2]
    file_names = os.listdir(f'{path}')

    if(path[-1]=='/'):
        path = path[:-1]

    Path(f"{path}/{dest}/").mkdir(parents=True, exist_ok=True)

    for file in file_names:
        if(bool(re.search(f'{dest}',file, re.IGNORECASE))==True):
            try:
                os.rename(f"{path}/{file}",f"{path}/{dest}/{file}")
            except Exception as e:
                print(e.args)