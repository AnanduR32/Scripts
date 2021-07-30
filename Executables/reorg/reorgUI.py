from tkinter import *
import sys, os, re
from pathlib import Path
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

buttonPathSelectIcon = ImageTk.PhotoImage(Image.open('./images/folder.png'))

def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
resource_path('./images/folder.png')

def SubmitClick():    
    path = pathEntry.get()
    dest = PatternEntry.get()
    file_names = os.listdir(f'{path}')

    if(path[-1]=='/'):
        path = path[:-1]

    for file in file_names:
        if(bool(re.search(f'{dest}',file, re.IGNORECASE))==True):
            try:
                Path(f"{path}/{dest}/").mkdir(parents=True, exist_ok=True)
                os.rename(f"{path}/{file}",f"{path}/{dest}/{file}")
                countLabel.configure(text=f"Done!")
            except Exception as e:
                countLabel.configure(text=f"Error!")
        else:
            countLabel.configure(text=f"File does not exist!")

def pathSelect():
    path = filedialog.askdirectory()
    pathEntry.insert(0, path)
    print(path)


## Main title ## 
title = Label(root, text = "Reorganize easy!")
title.grid(row=0, column=1)

## Spacer ## 
spacer = Label(root, text = " ")

## Labels ## 
label_enterPath = Label(root, text = "Enter directory path")
label_enterPattern = Label(root, text = "Enter pattern")

label_enterPath.grid(row=1, column=0)
label_enterPattern.grid(row=2 , column=0)

countLabel = Label(root)
countLabel.grid(row=4,column=1)

## Buttons ##
button_submit = Button(root, text="Submit", padx=10, command=SubmitClick)
button_submit.grid(row=3,column=1)

button_selectPath = Button(root, image=buttonPathSelectIcon, padx=25, pady=25, height=20, width=20, border=0, command=pathSelect)
button_selectPath.grid(row=1,column=2)

## Input entry ## 
pathEntry = Entry(root, border=0.35)
PatternEntry = Entry(root, border=0.35)
# PatternEntry.insert(0, "Enter pattern")
pathEntry.grid(row=1, column=1)
PatternEntry.grid(row=2, column=1)


## Mainloop ##
root.mainloop()