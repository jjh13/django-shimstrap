from django.conf.urls import include, url
from django.contrib import admin
from shimstrap.urls import ajax_url
from testapp.views import test_ajax_page

import shimstrap.site

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax-strap/', include(shimstrap.site.urls)),

    ajax_url(r'^test-request/$', test_ajax_page, 'test-request'),
    ajax_url(r'^request-for-id/[0-9]+$', test_ajax_page, 'request-for-id'),
]
