import os
import shutil

def replace_public_directory():
    from_path = "./static"
    to_path = "./public/"
    if os.path.exists(to_path):
        print("Deleting public directory")
        shutil.rmtree(to_path)
    copy_directory_recursively(from_path, to_path)


def copy_directory_recursively(from_dir, to_dir):
    if os.path.exists(from_dir) == False:
        raise FileNotFoundError(f"Directory {from_dir} does not exist")
    if os.path.isfile(from_dir):
        raise NotADirectoryError(f"{from_dir} is not a directory")
    
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)

    filelist = os.listdir(from_dir)
    for file in filelist:
        full_source_path = os.path.join(from_dir, file)
        full_dest_path = os.path.join(to_dir, file)
        if os.path.isdir(full_source_path):
            print (f"Making directory {full_dest_path} and recursing into it")
            copy_directory_recursively(full_source_path, full_dest_path)
        else:
            print (f"Copying file {full_source_path} to {full_dest_path}")
            shutil.copy(full_source_path, full_dest_path)