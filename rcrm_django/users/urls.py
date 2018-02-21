from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_users),
    url(r'^add_user$', views.add_user),
    url(r'^edit_user$', views.edit_user),
    url(r'^check_login$', views.check_login),
    url(r'^user_switch_status$', views.user_switch_status),
    url(r'^find_user$', views.find_user),
    url(r'^auto_complete_solves_user$', views.auto_complete_solves_user),
]
