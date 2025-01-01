import os
import shutil
from importlib.metadata import files
from logging import exception
from operator import truediv
from os.path import exists
import ctypes


def create_folder(folder_name, path):
    if not exists(path):
        raise FileNotFoundError("path not found")
    new_path = os.path.join(path, folder_name)
    if os.path.isdir(new_path):
        raise FileExistsError("folder already exists")
    os.mkdir(new_path)
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ctypes.windll.kernel32.SetFileAttributesW(new_path, FILE_ATTRIBUTE_HIDDEN)


def create_file(file_name, path):
    if not exists(path):
        raise FileNotFoundError("path not found")
    new_path = os.path.join(path, file_name)
    open(new_path, "w").close()


def write_file(path, text):
    if not exists(path):
        raise FileNotFoundError("path not found")
    with  open(path, "a") as file:
        file.write(text)


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
            if os.path.isfile(path):
              os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
    for item in os.listdir(source_path):
        path = os.path.join(source_path, item)
        new_path = os.path.join(destination_path, item)
        if os.path.isfile(path):
          copy_file(path, new_path)
        elif os.path.isdir(path):
          copy_folder(path,new_path)


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
        current_file = os.path.join(path, item)
        if os.path.isfile(current_file):
            try:
                os.remove(current_file)
            except FileNotFoundError as e:
                print(e)
        elif os.path.isfile(current_file):
            try:
              shutil.rmtree(current_file)
            except exception as e:
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


def is_file_modified_after1(path1, path2):
    if not os.path.exists(path1) or not os.path.exists(path2):
        return True
    date_path1 = os.path.getmtime(path1)
    date_path2 = os.path.getmtime(path2)
    return date_path1 > date_path2


