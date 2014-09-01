# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'


def key_to_java_def(key_string):
    keys = key_string.split()
    for key in keys:
        print "private String %s;" % key


def position_parameter_to_key_value(params):
    param = params.split(",")
    ret_param = ""
    for p in param:
        p = p.strip()
        # print p + "=" + p
        ret_param += p + "=" + "''" + ", "
    print ret_param
    pass


if __name__ == "__main__":
    key_string = '''
merchantaccount, orderid, orderexpdate, transtime, currency, amount, productcatalog,userua, productname, productdesc,
userip, identityid, identitytype, terminalid, terminaltype, other, callbackurl, fcallbackurl, paytypes
    '''
    position_parameter_to_key_value(key_string)