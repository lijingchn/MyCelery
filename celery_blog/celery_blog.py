#!/usr/bin/env python
# encoding: utf-8

import requests
import datetime
from celery import Celery

app = Celery("celery_blog", broker="redis://localhost:6379/1")

@app.task
def fetch_url(url):
    resp = requests.get(url)
    print resp.status_code

def func(urls):
    for url in urls:
        fetch_url.delay(url)

if __name__ == "__main__":
    print datetime.datetime.now()
    func(["http://baidu.com", "https://taobao.com", "http://jd.com", "http://blog.oneapm.com/apm-tech/197.html"])
    print datetime.datetime.now()
