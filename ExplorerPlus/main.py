import os

KEY_PATH = 'path'
KEY_SIZE = 'size'


def list_file_size(root_dir):
    file_dic_list = []
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            file_path = root + os.path.sep + f
            file_dic = {KEY_PATH: file_path, KEY_SIZE: os.path.getsize(file_path)}
            file_dic_list.append(file_dic)
    return sorted(file_dic_list, key=lambda k: k[KEY_SIZE], reverse=True)


def main():
    root_dir = input("Please input the root directory: ")
    file_size_list = list_file_size(root_dir)
    for f in file_size_list:
        print(f)


if __name__ == '__main__':
    main()


