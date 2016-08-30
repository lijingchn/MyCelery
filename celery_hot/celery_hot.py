#!/usr/bin/env python
# encoding: utf-8

import datetime
import time
from celery import Celery

app = Celery("celery_hot", backend = 'redis://127.0.0.1:6379/6', broker="redis://localhost:6379/1")
app.config_from_object("config")

@app.task
def hot_papers():
    print "start to get hot_papers at {0}".format(time.ctime())
    time.sleep(2)
    print "task get hot_papers succed at {0}".format(time.ctime())
    return True

