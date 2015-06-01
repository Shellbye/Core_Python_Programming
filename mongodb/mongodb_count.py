# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'
import logging
from pymongo import *

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='mongodb.log',
                        filemode='a')
    print "========"
    client = MongoClient("192.168.3.222", 27017)
    qcwy_count = client['qcwy']['resume_15_4_23'].count()
    print "qcwy_count: " + str(qcwy_count)
    logging.info("qcwy_count: " + str(qcwy_count))
    zhilian_count = client['zhilian']['ZhilianResumeCount'].count()
    zhilian_count += client['zhilian']['ZhilianHtmlResume'].count()
    print "zhilian_count: " + str(zhilian_count)
    logging.info("zhilian_count: " + str(zhilian_count))
    yingcai_count = client['yingcai']['yingcai_resume'].count()
    print "yingcai_count: " + str(yingcai_count)
    logging.info("yingcai_count: " + str(yingcai_count))
    print "total: " + str(qcwy_count + zhilian_count + yingcai_count)
    logging.info("total: " + str(qcwy_count + zhilian_count + yingcai_count))
    logging.info("---------------------------------------------------")
