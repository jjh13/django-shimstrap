from django.conf.urls import include, url
from django.contrib import admin
import shimstrap.site

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax-strap/', include(shimstrap.site.urls))
]
