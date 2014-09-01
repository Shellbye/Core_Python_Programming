# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'


def key_to_java_def(key_string):
    keys = key_string.split()
    for key in keys:
        print "private String %s;" % key


if __name__ == "__main__":
    key_string = '''
school
start_time
end_time
train_content
achieve

    '''
    key_to_java_def(key_string)