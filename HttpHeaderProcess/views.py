# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'


def process_headers(headers=None):
    for line in headers.splitlines():
        key, value = line.split(":")[0], "".join(line.split(":")[1:])
        print 'httppost.setHeader("' + key + '", "' + value + '");'


if __name__ == "__main__":
    headers = '''Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip,deflate,sdch
Accept-Language:en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4
Cache-Control:max-age=0
Connection:keep-alive
Cookie:guid=14065290826431390066; EhireGuid=a0131524e3384094bbdc2dfaa6675558; 51job=cenglish%3D0; ASP.NET_SessionId=yrmfuownxodluhsi2o5cuvdm; Theme=Default; LangType=Lang=&Flag=1; HRUSERINFO=CtmID=2160323&DBID=4&MType=02&HRUID=2510808&UserAUTHORITY=1111111111&IsCtmLevle=1&UserName=cdsz500&IsStandard=0&LoginTime=08%2f12%2f2014+15%3a28%3a26&ExpireTime=08%2f12%2f2014+15%3a38%3a26&CtmAuthen=0000011000000001000110010000000011100001&BIsAgreed=true&IsResetPwd=true&CtmLiscense=1&AccessKey=93a0fc8e5f0e5b82; AccessKey=137054a2c7594d3; RememberLoginInfo=member_name=0864ED6B29B692B4C3DE0F9CD284FD09&user_name=2687703F2535E105
Host:ehire.51job.com
Referer:http://ehire.51job.com/Member/UserOffline.aspx?tokenId=ee21476d-d902-4e5d-a4ea-f9dd42d8&errorFlag=0&dbid=4&val=fdd7fafd60d07883&isRememberMe=True&Lang=&Flag=1
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36
'''
    process_headers(headers)