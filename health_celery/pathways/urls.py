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

from health_celery.pathways.views import home, pathways_time_task, pathways_space_task

pathways_patterns = [
    url(r'^$', home, name='pathways-home'),
    url(r'^time/', pathways_time_task, name='pathways-time-task'),
    url(r'^space/', pathways_space_task, name='pathways-space-task'),
]
