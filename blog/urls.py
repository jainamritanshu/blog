from django.conf.urls import url, include, patterns
from django.contrib import admin
from forum.views import detail, ques_list
from login.views import *

app_name = 'forum, login'
urlpatterns = patterns( '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', ques_list),
    url(r'^home/(?P<q_id>[0-9]+)/$', detail, name='detail'),
    url(r'^register/$', register, name='register'),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page, name='logout_page'),
    url(r'^register/success/$', r_success),
)
