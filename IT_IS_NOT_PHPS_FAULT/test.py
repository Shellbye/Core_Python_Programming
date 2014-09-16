# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'

if __name__ == '__main__':
    # http://stackoverflow.com/questions/25862715/php-variable-scope-why-temp-override-the-other
    a = 123
    b = [1, 2, 3]
    for c in b:
        print c
    print a