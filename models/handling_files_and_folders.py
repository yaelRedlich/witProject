import os
import shutil
from importlib.metadata import files
from operator import truediv
from os.path import exists


def create_folder(folder_name, path):
    if not exists(path):
        raise FileNotFoundError("path not found")
    new_path = os.path.join(path, folder_name)
    if os.path.isdir(new_path):
        raise FileExistsError("folder already exists")
    os.mkdir(new_path)


def create_file(file_name, path):
    if not exists(path):
        raise FileNotFoundError("path not found")
    new_path = os.path.join(path, file_name)
    open(new_path, "w").close()


#דורס את קובץ במידה וקיימת כבר קובץ בשם זהה

def write_file(path, text):
    if not exists(path):
        raise FileNotFoundError("path not found")
    with  open(path, "a") as file:
        file.write(text)


#מוסיפה ולא דורסת


def read_file(path):
    if not exists(path):
        raise FileNotFoundError("path not found")
    with open(path, "r") as file:
        return file.read()


def copy_file(source_path, destination_path):
    shutil.copyfile(source_path, destination_path)


def copy_folder(source_path, destination_path):
    shutil.copytree(source_path, destination_path)


def copy_folder_without_parm(source_path, destination_path, parm):
    for item in os.listdir(destination_path):
        if item != parm:
            path = os.path.join(destination_path, item)
            os.remove(path)
    for item in os.listdir(source_path):
        path = os.path.join(source_path, item)
        new_path = os.path.join(destination_path, item)
        copy_file(path, new_path)


def find_last_created_folder(directory):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    last_created_folder = max(folders, key=lambda folder: os.path.getctime(os.path.join(directory, folder)))
    return last_created_folder


def copy_files_and_overwrite(source_dir, destination_dir):
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)
        if os.path.isdir(source_item):
            if not os.path.exists(destination_item):
                os.makedirs(destination_item)
            copy_files_and_overwrite(source_item, destination_item)
        else:
            shutil.copy2(source_item, destination_item)


def folder_is_empty(path):
    if not os.listdir(path):
        return True
    return False


def emptying_folder(path):
    for item in os.listdir(path):
        try:
            current_file = os.path.join(path, item)
            os.remove(current_file)
        except FileNotFoundError as e:
            print(e)


def read_names_all_files_in_folder(path):
    all_names = []
    for item in os.listdir(path):
        try:
            all_names.append(item)
        except FileNotFoundError as e:
            print(e)
    return all_names


def is_file_modified_after(path1, path2):
    date_path1 = os.path.getmtime(path1)
    date_path2 = os.path.getmtime(path2)
    if date_path1 > date_path2:
        return True
    else:
        return False


#create_file("index1.html",r"C:\Users\user1\Desktop\python\test\1")
#create_folder("1",r"C:\Users\user1\Desktop\python\test")
#write_file(r"C:\Users\user1\Desktop\python\test\1\index.html","<h1>hello world</h1>")
#print(read_file(r"C:\Users\user1\Desktop\python\test\1\index.html"))
#copy_file(r"C:\Users\user1\Desktop\python\test\1\index.html",r"C:\Users\user1\Desktop\python\test\1\index1.html")
#copy_folder(r"C:\Users\user1\Desktop\python\test",r"C:\Users\user1\Desktop\python\test2")
#print(read_names_all_files_in_folder(r"C:\Users\user1\Desktop\python\test\.wit\commits\commit 1"))
# print(is_file_modified_after(r"C:\Users\user1\Desktop\python\test2",r"C:\Users\user1\Desktop\python\test"))
#copy_folder_without_parm(r"C:\Users\user1\Desktop\python\source", r"C:\Users\user1\Desktop\python\dist", ".wit")
