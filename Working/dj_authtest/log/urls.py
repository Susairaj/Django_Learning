#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^po_list/$', views.po_list, name='po_list'),
    url(r'^test/$', views.test, name='test'),
    url(r'^so_list/$', views.so_list, name='so_list'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^$', views.index, name='index')
]
