from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^profiles/', include('easy_profiles.urls')),

    (r'^admin/', include(admin.site.urls)),
)
