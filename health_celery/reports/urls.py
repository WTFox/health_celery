"""health_celery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from health_celery.reports.views import home, reports_time_task, reports_space_task

reports_patterns = [
    url(r'^$', home, name='reports-home'),
    url(r'^time/', reports_time_task, name='reports-time-task'),
    url(r'^space/', reports_space_task, name='reports-space-task'),
]
