from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'users.views.list_users'),
    url(r'^add_user$', 'users.views.add_user'),
    url(r'^edit_user$', 'users.views.edit_user'),
    url(r'^check_login$', 'users.views.check_login'),
    url(r'^user_switch_status$', 'users.views.user_switch_status'),
    url(r'^find_user$', 'users.views.find_user'),
)
