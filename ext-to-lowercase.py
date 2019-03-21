import os
import argparse

# TODO: Add the ability to convert cases in the root directory only.
parser = argparse.ArgumentParser(description='A simple comand line to convert file extensions from upper case to lower case')
# parser.add_argument('directory', default=os.getcwd(), nargs='?')
parser.add_argument('--dir', '-D', action='store', default='.', help="Give the directory name.")


def convert_extension_to_lowercase(directory):
    
    for dir_name, dirs_list, files_list in os.walk(directory):
        print('processing ', dir_name)
        for file in files_list:
            file_name, file_extension = os.path.splitext(file)
            if any(letter.isupper() for letter in file_extension):
                # you should use os.path.join to get the path to make operation like renaming
                file_path = os.path.join(dir_name, file)
                file_renamed = os.path.join(dir_name, f'{file_name}{file_extension.lower()}')
                os.rename(file_path, file_renamed)
    print('Finished')

if __name__ == "__main__":
    args = parser.parse_args()
    dir = args.dir
    convert_extension_to_lowercase(dir)