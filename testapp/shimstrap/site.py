from django.conf.urls import url
from . import views

urls = [
    url(r'^login/$', views.serve_shim, name='login')
]