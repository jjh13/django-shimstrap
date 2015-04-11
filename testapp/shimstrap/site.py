from django.conf.urls import url
from . import views

urls = [
    url(r'^login/$', views.serve_shim, name='login')
    # provide a raw map object
    # provide a jquery override shim
    # provide a require.js shim
]