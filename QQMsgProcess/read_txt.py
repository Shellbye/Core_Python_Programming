# -*- coding:utf-8 -*-
__author__ = 'shellbye'
import re

from models import QQMsg
from models import Sms
from models import ErrorLog


def tencent():
    if not QQMsg.table_exists():
        QQMsg.create_table()
    else:
        QQMsg.drop_table()
        QQMsg.create_table()
    print "Please input the QQ txt msg src:"
    file_src = raw_input()
    read_and_store_tencent(file_src)


def read_and_store_tencent(txt_file):
    f = open(txt_file, mode='r')
    line_id = None
    line_number = 0
    for current_line in f:
        try:
            line_number += 1

            # this line is empty
            if len(current_line) == 1:
                continue

            # this line is time line
            pattern = re.compile(r"^\d{4}(-\d\d){2} \d\d(:\d\d){2}")
            if pattern.match(current_line):
                line_date, line_time, line_user = current_line.split(" ")[0:3]
                new_msg = QQMsg(msg_date=line_date, msg_time=line_date + " " + line_time, msg_user=line_user)
                new_msg.save()
                line_id = new_msg.get_id()
                continue

            # this line is a content

            if line_id is None:
                continue
            msg = QQMsg.get(id=line_id)
            msg.msg_content += current_line
            msg.save()
        except Exception, e:
            ErrorLog(error_line=line_number, error_function="read_and_store_tencent", error_msg=e).save()


def short_message():
    if not Sms.table_exists():
        Sms.create_table()
    else:
        Sms.drop_table()
        Sms.create_table()
    print "Please input the sms file src:"
    file_src = raw_input()
    read_and_store_sms(file_src)


def read_and_store_sms(sms_file):
    f = open(sms_file, mode='r')
    line_id = None
    line_number = 0
    for current_line in f:
        try:
            line_number += 1
            if len(current_line) <= 1:
                continue

            # this line is a new sms
            if current_line.strip().startswith("sms"):
                # split may contain more than we want because of the comma in content
                spited = current_line.split(",")
                direction, name, phone, date_time, content = spited[1], spited[2], spited[3], spited[5], spited[7],
                date_time = deal_with_sms_date_time(date_time)

                # the position of name and phone may exchange due to the direction
                if direction == "submit":
                    pass
                else:
                    name, phone = phone, name
                sp_list = [direction, name, phone, date_time, content]
                tp_list = []
                for a in sp_list:
                    tp_list.append(a.strip())
                new_sms = Sms(sms_direction=tp_list[0], sms_name=tp_list[1], sms_phone=tp_list[2],
                              sms_date=tp_list[3][:10], sms_time=tp_list[3], sms_content=tp_list[4])
                new_sms.save()
                line_id = new_sms.get_id()
                continue

            # this line is a continue content
            if line_id is None:
                continue
            sms = Sms.get(id=line_id)
            sms.sms_content += current_line
            sms.save()
        except Exception, e:
            ErrorLog(error_line=line_number, error_function="read_and_store_sms", error_msg=e).save()


def deal_with_sms_date_time(date_time):
    date = date_time[:10]
    time = date_time[11:]
    time_list = date.split(".")
    time_list += time.split(":")
    return time_list[0] + "-" + \
        time_list[1].replace(" ", "0") + "-" + \
        time_list[2].replace(" ", "0") + " " + \
        time_list[3].replace(" ", "0") + ":" + \
        time_list[4].replace(" ", "0")


if __name__ == '__main__':
    # tencent()
    short_message()