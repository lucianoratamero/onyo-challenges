# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
]

if 'bob' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^api/v0/bob/', include('bob.urls', namespace='bob')),
    )
