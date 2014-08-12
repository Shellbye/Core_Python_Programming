# -*- coding:utf-8 -*-
__author__ = 'shellbye'

import datetime

import peewee

db = peewee.MySQLDatabase(host='192.168.2.222', user='haier', passwd='123456', database='test')


class QQMsg(peewee.Model):
    msg_date = peewee.DateField()
    msg_time = peewee.DateTimeField()
    msg_user = peewee.TextField()
    msg_content = peewee.TextField(default="")

    class Meta:
        database = db


class Sms(peewee.Model):
    sms_direction = peewee.CharField()
    sms_name = peewee.CharField()
    sms_phone = peewee.CharField()
    sms_date = peewee.DateField()
    sms_time = peewee.DateTimeField()
    sms_content = peewee.TextField(default="")

    class Meta:
        database = db


class ErrorLog(peewee.Model):
    error_time = peewee.DateTimeField(default=datetime.datetime.now)
    error_function = peewee.CharField(default=None)
    error_line = peewee.IntegerField(default=0)
    error_msg = peewee.TextField(default=None)

    class Meta:
        database = db
