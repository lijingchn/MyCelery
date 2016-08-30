#!/usr/bin/env python
# encoding: utf-8

import requests
import datetime
import time
from celery import Celery

app = Celery("celery_notify", backend = 'redis://127.0.0.1:6379/6', broker="redis://localhost:6379/1")

@app.task
def notify_friends(userId, newsId):
    print "start to notify_friends task at {0}, userID:{1},newsID:{2}".format(datetime.datetime.now(), userId, newsId)
    time.sleep(2)
    print "task notify_friends succeed at {0}".format(datetime.datetime.now())
    return True

