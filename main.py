import os
import shutil
from tkinter import *
path = "C:/Users/21263/Downloads"
files =os.listdir(path)

def Orgenize():
    for file in files:
        filename,extension=os.path.splitext(file)
        extension=extension[1:]

        if file.endswith(".mp4") or file.endswith(".mkv"):
            shutil.move(path+"/"+file,path+"/video")
        else:
            if os.path.exists(path+'/'+extension):
              shutil.move(path+"/"+file,path+"/"+extension+"/"+file)
            else:
              os.makedirs(path+"/"+extension)
              shutil.move(path+"/"+file,path+"/"+extension+"/"+file)

if __name__=="__main__":
    root = Tk()

    root.title("File Orgenizer")

    orgeniz=Button(root,padx=40,pady=16,bd=8,fg="black",text="Orgenize",command=lambda:Orgenize()).grid(row=1,column=0)

    root.mainloop()
