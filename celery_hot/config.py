#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime
from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    "hot_paper":{
        "task":"celery_hot.hot_papers",
        "schedule":timedelta(seconds=20),
    },
}
