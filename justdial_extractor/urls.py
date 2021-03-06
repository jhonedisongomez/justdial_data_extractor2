"""justdial_extractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from crawler_manager.views import CrawlerView1,CrawlerView2,CrawlerView3,CrawlerView4, HomeView, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^form1', CrawlerView1.as_view(), name='form1'),
    url(r'^form2', CrawlerView2.as_view(), name='form2'),
    url(r'^form3', CrawlerView3.as_view(), name='form3'),
    url(r'^form4', CrawlerView4.as_view(), name='form4'),
    url(r'^logout', logout, name='logout'),
]
