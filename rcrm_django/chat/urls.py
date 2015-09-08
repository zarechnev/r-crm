from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^show_chat$', 'chat.views.show_chat'),
    url(r'^add_post$', 'chat.views.add_post')
)
