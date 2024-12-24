import os
import shutil
from importlib.metadata import files
from os.path import exists

def create_folder(folder_name,path):
    if not exists(path):
        raise FileNotFoundError ("path not found")
    new_path=os.path.join(path,folder_name)
    if os.path.isdir(new_path):
        raise FileExistsError ("folder already exists")
    os.mkdir(new_path)

def create_file(file_name,path):
    if not exists(path):
        raise FileNotFoundError ("path not found")
    new_path=os.path.join(path,file_name)
    open(new_path,"w").close()

#דורס את התיקיה במידה וקיימת כבר תיקייה בשם זהה

def write_file (path,text) :
    if not exists(path):
        raise FileNotFoundError("path not found")
    with  open(path,"a") as file:
        file.write(text)
#מוסיפה ולא דורסת
def read_file(path):
    if not exists(path):
        raise FileNotFoundError("path not found")
    with open(path,"r") as file:
       return file.read()
    #יתכן שלא נשתמש
def copy_file(source_path,destination_path):
    shutil.copyfile(source_path,destination_path)

#create_file("index1.html",r"C:\Users\user1\Desktop\python\test\1")
#create_folder("1",r"C:\Users\user1\Desktop\python\test")
#write_file(r"C:\Users\user1\Desktop\python\test\1\index.html","<h1>hello world</h1>")
#print(read_file(r"C:\Users\user1\Desktop\python\test\1\index.html"))
#copy_file(r"C:\Users\user1\Desktop\python\test\1\index.html",r"C:\Users\user1\Desktop\python\test\1\index1.html")