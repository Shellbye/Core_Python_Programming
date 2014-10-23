__author__ = 'shellbye'
import re


def delete_leading_no(file_location=None, new_file=None, number_count=1):
    if not file_location:
        return
    if not new_file:
        new_file = file_location + "-new"
    f = open(file_location, 'r')
    f2 = open(new_file, 'w')
    pattern = re.compile(r"^\d{%s}" % number_count)
    for line in f.readlines():
        if pattern.match(line):
            f2.write(line[number_count:])

if __name__ == "__main__":
    delete_leading_no(file_location="/home/shellbye/old_file.txt", number_count=3)