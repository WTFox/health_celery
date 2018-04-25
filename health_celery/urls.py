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
from django.conf.urls import url, include
from django.contrib import admin

from health_celery.account.urls import account_patterns
from health_celery.reports.urls import reports_patterns
from health_celery.pathways.urls import pathways_patterns


urlpatterns = [
    url(r'^account/', include(account_patterns)),
    url(r'^reports/', include(reports_patterns)),
    url(r'^pathways/', include(pathways_patterns)),

    url(r'^admin/', admin.site.urls),
]
