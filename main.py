# coding=utf-8
import os
import shutil


def get_folder(extension):
    folders = {
        "PDF": "PDF",
        "WORD": "WORD",
        "TEXT": "TEXT",
        "ZIP": "ZIP",
        "RAR": "RAR",
        "WEBP": "PDF",
        "XLSX": "EXCEL"
    }
    return folders.get(extension.upper())


user_dir = os.path.expanduser('~')
dir_list = ["PDF", "WORD", "TXT", "ZIP", "RAR", "EXCEL"]  # to change if you prefer other directory to clean
parent_dir = os.path.join(user_dir, "OneDrive", "Documents")  # to change if you prefer other directory to clean
list_dir = os.listdir(parent_dir)
target_directory = os.path.join(user_dir, "Documents")

for dir_name in set(dir_list):
    path = os.path.join(target_directory, dir_name)
    if not os.path.exists(path):
        os.mkdir(path)

for file_name in list_dir:
    file_path = os.path.join(parent_dir, file_name)
    if os.path.isfile(file_path):
        file_extension = file_name.split('.')[-1].upper()
        folder_name = get_folder(file_extension)

        if folder_name is not None:
            dest_path = os.path.join(target_directory, folder_name, file_name)
            shutil.move(file_path, dest_path)
            print("These files are been moved " + file_name)
        else:
            print("The file " + file_name + " has not extension recognized in " + parent_dir)
