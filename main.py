# -*- coding: utf-8
__author__ = 'shellbye'
if __name__ == "__main__":
    a = u"数据挖掘"
    print a
    b = u"http://www.lagou.com/jobs/list_" \
        + a + u"?kd=" \
        + a + u"&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=label%2Clabel&lc=&workAddress=&city=全国&requestId=&pn=" \
        + unicode(1)
    print b