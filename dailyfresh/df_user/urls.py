from django.conf.urls import include, url
from . import views

urlpatterns=[
    url(r'^register$', views.register),
    url(r'^register_handle$', views.register_handle),
    url(r'^login$', views.login),
    url(r'^check/uname$', views.uname_repeated),
    url(r'^login_handle$', views.login_handle),
    url(r'^info$', views.user_info),
]