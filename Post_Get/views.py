# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'

import urllib
import urllib2


def this_is_a_post():
    data = urllib.urlencode({"key": "value"})
    post_request = urllib2.urlopen("http://127.0.0.1:8001/polls/", data)
    print post_request.read()


def this_is_a_get():
    get_without_data = urllib2.urlopen("http://127.0.0.1:8001/polls/")
    print get_without_data.read()

    get_with_data = urllib2.urlopen("http://127.0.0.1:8001/polls/?%s" % urllib.urlencode({"key": "value"}))
    print get_with_data.read()


def get_post():
    get_post_data = urllib2.urlopen("http://127.0.0.1:8001/polls/?%s" % urllib.urlencode({"key": "value"}),
                                    urllib.urlencode({"key": "value"}))
    print get_post_data.read()

if __name__ == "__main__":
    this_is_a_get()
    print "============================================================================"
    this_is_a_post()
    print "============================================================================"
    get_post()