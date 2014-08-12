# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'

import os


def rename_files(dir_path):
    # check if it's a legal directory
    if os.path.isdir(dir_path):
        files = os.listdir(dir_path)
        for f in files:
            # for a single file, check if it is a file or a directory
            current_file = dir_path + os.sep + f
            if os.path.isdir(current_file):
                rename_files(current_file)
            elif os.path.isfile(current_file):
                os.rename(current_file, current_file + ".jpg")
            else:
                pass


if __name__ == "__main__":
    rename_files("c:\\pic")