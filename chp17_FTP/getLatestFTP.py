#!/usr/bin/env python

import ftplib
import os
import socket

HOST = '121.42.11.154'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'ftp_test.txt'


def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror), e:
        print e
        print 'ERROR: cannot reach "%s"' % HOST
        return
    print '*** Connected to host "%s"' % HOST

    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return
    print '*** Logged in as "anonymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s" folder' % DIRN
        f.quit()
        return
    print '*** Changed to "%s" folder' % DIRN

    try:
        f.retrlines('RETR %s' % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        if os.path.exists(FILE): os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to CWD' % FILE
    f.quit()
    return


if __name__ == '__main__':
    main()
