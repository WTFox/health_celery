# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from health_celery.account.jobs import time_task, space_task


# Create your views here.
def home(request):
    html = "<html><body>Welcome to the Account home page!</body></html>"
    return HttpResponse(html)


def account_time_task(request):
    n = 100
    time_task.delay(n)
    return HttpResponse("{'result': 'SUCCESS'}")


def account_space_task(request):
    space_task.delay()
    return HttpResponse("{'result': 'SUCCESS'}")
