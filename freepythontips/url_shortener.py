from __future__ import with_statement
# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'

import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' +
                   urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


if __name__ == '__main__':
    print make_tiny("http://www.shellbye.com")