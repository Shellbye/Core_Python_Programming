#!/usr/bin/env python

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.163.com'
POP3SVR = 'pop.163.com'

origHdrs = ['From: hospital_test@163.com',
    'To: hospital_test@163.com',
    'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
sendSvr.login("hospital_test@163.com", "tt111111")
errs = sendSvr.sendmail('hospital_test@163.com',
    ('hospital_test@163.com', ), origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)    # wait for mail to be delivered

recvSvr = POP3(POP3SVR)
recvSvr.user('hospital_test@163.com')
recvSvr.pass_('tt111111')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody # assert identical
