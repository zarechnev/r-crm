from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello),
    url(r'^users$', views.users),
    url(r'^clients$', views.clients),
    url(r'^tasks$', views.tasks),
]
