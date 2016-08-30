#!/usr/bin/env python
# encoding: utf-8

import requests
import datetime

def func(urls):
    for url in urls:
        resp = requests.get(url)

if __name__ == "__main__":
    print datetime.datetime.now()
    func(["http://baidu.com", "https://taobao.com", "http://jd.com", "http://blog.oneapm.com/apm-tech/197.html"])
    print datetime.datetime.now()
