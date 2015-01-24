from django.conf.urls import patterns, url
#from django.contrib import admin

import file.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'approve_me_please.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', file.views.home, name='home'),

    url(r'^add/$', file.views.upload),
    url(r'^(?P<permalink>[a-zA-Z0-9]{1,10})/$', file.views.file_view),
]
