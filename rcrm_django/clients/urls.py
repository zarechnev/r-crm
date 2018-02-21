from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello),
    url(r'^add_edit_client$', views.add_edit_client),
    url(r'^get_client_info/([0-9]+)$', views.get_client_info),
    url(r'^rem_client$', views.rem_client),
    url(r'^client_switch_status$', views.client_switch_status),
    url(r'^find_client$', views.find_client),
]
