import os
import shutil

cur_dir = os.getcwd()


def dir_create():
    dir_name = input("Folder Name: ")
    full_path = os.path.join(cur_dir, dir_name)
    try:
        os.mkdir(full_path)
    except FileExistsError:
        print(f"The folder {dir_name} already exists.")
    return full_path


def dir_list():
    pathname = cur_dir
    file_list = []
    list_of_folders = os.listdir(pathname)
    for folder in list_of_folders:
        folder_path = os.path.join(pathname, folder)
        if os.path.isdir(folder_path) and not folder.startswith("."):
            file_list.append(folder_path)

    for file in file_list:
        print(file)


def dir_remove():
    destroy_file = input("Folder Name: ")
    path = cur_dir
    full_path = os.path.join(path, destroy_file)

    if os.path.isdir(full_path):  # check if directory exists
        shutil.rmtree(full_path)
    else:
        print(f"No {destroy_file} directory has been found.")
