#!/usr/bin/env python
# encoding: utf-8

# call celery_notify.py

from celery_notify import notify_friends
import datetime
import time

def main(userId, messageId):
    result = notify_friends.delay(userId, messageId)
    while not result.ready():
        print result.ready()
        time.sleep(0.5)
    print "result ready : True"

if __name__ == "__main__":
    main("001","002")
