"""agenvida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mainApp.viewsets import PropositoViewSet, VinculacionViewSet,UserDetail, UserList
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from mainApp import views

admin.autodiscover()


router = DefaultRouter()
router.register(r'propositos', PropositoViewSet)
router.register(r'vinculaciones', VinculacionViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^propositos2/$', views.PropositoList.as_view()),
    url(r'^propositos2/(?P<pk>[0-9]+)/$', views.PropositoDetail.as_view()),
    url(r'^users/$', UserList.as_view()),
url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

###Sirve para poder Loguearte y desloguearte del api html
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]






