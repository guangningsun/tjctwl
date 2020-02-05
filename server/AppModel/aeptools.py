#!/usr/bin/python
# encoding=utf-8
import time
import datetime
import binascii
import base64
import json
#import urllib2
import urllib
import hmac 
#import urlparse
from hashlib import sha1

import sys


if sys.version_info[0] == 2:
    # Python2
    from urllib import urlencode
    from urllib import quote
    from urlparse import urlparse
    import urllib2
    reload(sys)
    sys.setdefaultencoding('utf-8')    #注意，windows下命令行运行中文可能会乱码，需要先运行命令chcp 65001，设置控制台字符集为utf-8
else:
    # Python3
    from urllib.parse import urlencode  
    from urllib.parse import quote
    from urllib.parse import urlparse
    import urllib.request as urllib2


#key、application、timestamp、body为字符串
#param为list，结构如下
#param=[['deviceId', '1'], ['deviceName', 'test']]
def signature(key, application, timestamp, param, body):
    code = "application:" + application + "\n" + "timestamp:" + timestamp + "\n"
    for v in param:
        code += str(v[0]) + ":" + str(v[1]) + "\n"
    if (body is not None) and (body.strip()) :
        code += body + '\n'
    print("param=" + str(param))
    print("body=" + str(body))
    print("code=" + str(code))
    #print(binascii.b2a_hex(code))
    return base64.b64encode(hash_hmac(key, code, sha1))
    
def hash_hmac(key, code, sha1): 
    hmac_code = hmac.new(key.encode(), code.encode(), sha1) 
    print("hmac_code=" + str(hmac_code.hexdigest()))
    return hmac_code.digest()


def getTimeOffset(url):
    request = urllib2.Request(url)
    start = int(time.time() * 1000)
    response = urllib2.urlopen(request)
    end = int(time.time() * 1000)
    
    if response is not None:
        return int(int(response.headers['x-ag-timestamp']) - (end + start) / 2);
    else:
        return 0


baseUrl = 'https://ag-api.ctwing.cn'
timeUrl = 'https://ag-api.ctwing.cn/echo'

#sdk = 'GIT: a4fb7fca'
sdk = 0
Accept = 'gzip,deflate'
Content_Type = 'application/json; charset=UTF-8'
User_Agent = 'Telecom API Gateway Java SDK'
offset = getTimeOffset(timeUrl)


def sendSDKRequest(path, head, param, body, version, application, MasterKey, key, method = None, isNeedSort = True, isNeedGetTimeOffset = False):
    paramList=[]
    for key_value in param:
        paramList.append([key_value, param[key_value]])
    print("paramList=" + str(paramList))
    if (MasterKey is not None) and (MasterKey.strip()) :
        paramList.append(['MasterKey',MasterKey])
    if isNeedSort:
        paramList = sorted(paramList)
    
    headers = {}
    if (MasterKey is not None) and (MasterKey.strip()) :
        headers['MasterKey'] = MasterKey
    headers['application'] = application
    headers['Date'] = str(datetime.datetime.now())
    headers['version'] = version

    temp = dict(param.items())
    if (MasterKey is not None) and (MasterKey.strip()) :
        temp['MasterKey'] = MasterKey
    
    url_params = urlencode(temp)
    
    url = baseUrl + path 
    if (url_params is not None) and (url_params.strip()) :
        url = url + '?' + url_params
    print("url=" + str(url))
    global offset
    if isNeedGetTimeOffset:
        offset = getTimeOffset(timeUrl)
    timestamp = str(int(time.time()*1000) + offset)
    headers['timestamp'] = timestamp
    sign = signature(key, application, timestamp, paramList, body)
    headers['signature'] = sign
    
    headers.update(head)
    
    print("headers : %s" % (str(headers)))
    
    
    if (body is not None) and (body.strip()) :
        request = urllib2.Request(url = url, headers=headers, data=body.encode('utf-8'))
    else :
        request = urllib2.Request(url = url, headers=headers)
    if (method is not None) :
        request.get_method=lambda : method
    response = urllib2.urlopen(request)
    if('response' in vars()):
        print("response.code: %d" % (response.code))
        return response
    else:
        return None


if __name__ == '__main__':
    SECRET_ID = "un2puu02Ml"
    APPLICATION_ID = "AMQROxaUNh"
    VERSION = "20181031202055"
    MasterKey = "ffd9c7a217004acc87f2df46c348e8d2"
    path = "/aep_product_management/product"
    param = {"productId": "10035737"}
    body = ''
    res = sendSDKRequest(path,{"sdk":0},param,body,VERSION,APPLICATION_ID,None,SECRET_ID)
    print (json.loads(res.read()))
    
