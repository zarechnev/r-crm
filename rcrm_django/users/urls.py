from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'users.views.list_users'),
    url(r'^add_user$', 'users.views.add_user'),
    url(r'^rem_user$', 'users.views.rem_user'),
    url(r'^check_login$', 'users.views.check_login')
)
