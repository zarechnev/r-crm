from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'clients.views.hello'),
    url(r'^add_edit_client$', 'clients.views.add_edit_client'),
    url(r'^get_client_info/([0-9]+)$', 'clients.views.get_client_info'),
    url(r'^rem_client$', 'clients.views.rem_client'),
    url(r'^client_switch_status$', 'clients.views.client_switch_status'),
    url(r'^find_client$', 'clients.views.find_client'),
)