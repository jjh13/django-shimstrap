from django.conf.urls import url
from . import views

urls = [
    url(r'^url_map/$', views.serve_shim),
    url(r'^url_map/[A-Za-z0-9]+$', views.serve_shim),

    # provide a jquery override shim
    url(r'^jq-ajaxmax/$', views.serve_shim),

    # provide a require.js shim
    url(r'^require/[A-Za-z0-9]+$', views.serve_shim),
    url(r'^require/[A-Za-z0-9]+$', views.serve_shim),
]