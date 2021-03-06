"""Logistics URL Configuration

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
from Log_web import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^signIn/$',views.signIn),
    url(r'^signUp/$',views.signUp),
    url(r'^sendPackage/$',views.sendPackage),
    url(r'^getProvince/$',views.getProvince),
    url(r'^getCity/$',views.getCity),
    url(r'^userPackage/$',views.userPackage),
    url(r'^userPackages/$',views.userPackages),
    url(r'^userInfo/$',views.userInfo),
    url(r'^user/$',views.user),
    url(r'^godown_keeper/$',views.godownKeeper),
    url(r'^admin/', admin.site.urls),
    url(r'^get_package_id/$', views.godownGetPackageId),
    url(r'^getWeight/$', views.getWeight),
    url(r'^getDistributor/$', views.getDistributor),
    url(r'^getGodown/$',views.getGodown),
    url(r'^godownkeeper_package/$',views.godownKeeperPackage),
    url(r'^distribute/$',views.distribute),
    url(r'^distriPackage/$',views.disGetPackageId),
    url(r'^distribute_package/$',views.packageDistribute),
    url(r'^company/$',views.company),
]
