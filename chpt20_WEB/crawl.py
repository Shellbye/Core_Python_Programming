#!/usr/bin/env python
# -*- coding:utf-8 -*-
from os import makedirs, unlink, sep
from os.path import isdir, exists, dirname, splitext, abspath
from string import replace, find, lower
from htmllib import HTMLParser
import urllib
from urlparse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO


class Retriever(object):    # download Web pages

    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)

    def filename(self, url, deffile='index.htm'):
        # 使用http协议解析url地址，将url解析为这样的五元组：(scheme, netloc, path, query, fragment)
        parsedurl = urlparse(url, 'http:', 0)
        # 将主机地址（netloc）和路径（path）合并起来作为存储文件的路径名
        path = parsedurl[1] + parsedurl[2]
        # splitext将path分割为路径与后缀名，如（/path/to/file, txt）
        ext = splitext(path)
        # 如果后缀名为空，则给当前path添加默认的名字index.htm
        if ext[1] == '':
            # 若path结尾有“/”则直接添加index.htm，否则先添加“/”
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile
        # 取出path中的目录部分（www.shellbye.com\\blog），然后与本地目录结合为一个目录('D:\\www.shellbye.com\\blog')
        ldir = dirname(abspath(path))
        # 如果不是以“/”作为目录分割符的类Unix系统，比如Windows，则需要把“”替换为相应的目录分割符
        # 因为类Unix系统的目录分割符与URI地址的分割符一样，所以可以不处理
        if sep != '/':        # os-indep. path separator
            ldir = replace(ldir, '/', sep)
        # 如果ldir目录不存在在创建
        if not isdir(ldir):      # create archive dir if nec.
            # 如果ldir存在但是不是目录则删除ldir。注，unlink即remove。
            if exists(ldir):
                unlink(ldir)
            makedirs(ldir)
        return path

    def download(self):        # download Web page
        try:
            retval = urllib.urlretrieve(self.url, self.file)
        except IOError:
            retval = ('*** ERROR: invalid URL "%s"' % self.url, )
        return retval

    def parseAndGetLinks(self):    # pars HTML, save links
        self.parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO())))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist


class Crawler(object):        # manage entire crawling process

    count = 0            # static downloaded page counter

    def __init__(self, url):
        self.q = [url]
        self.seen = []
        self.dom = urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()
        if retval[0] == '*':     # error situation, do not parse
            print retval, '... skipping parse'
            return
        Crawler.count += 1
        print '\n(', Crawler.count, ')'
        print 'URL:', url
        print 'FILE:', retval[0]
        self.seen.append(url)

        links = r.parseAndGetLinks()  # get and process links
        for eachLink in links:
            if eachLink[:4] != 'http' and find(eachLink, '://') == -1:
                eachLink = urljoin(url, eachLink)
            print '* ', eachLink,

            if find(lower(eachLink), 'mailto:') != -1:
                print '... discarded, mailto link'
                continue

            if eachLink not in self.seen:
                if find(eachLink, self.dom) == -1:
                    print '... discarded, not in domain'
                else:
                    if eachLink not in self.q:
                        self.q.append(eachLink)
                        print '... new, added to Q'
                    else:
                        print '... discarded, already in Q'
            else:
                print '... discarded, already processed'

    def go(self):                # process links in queue
        while self.q:
            url = self.q.pop()
            self.getPage(url)


def main():
    url = "http://shellbye.com"
    robot = Crawler(url)
    robot.go()


if __name__ == '__main__':
    main()
