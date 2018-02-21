from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show_chat$', views.show_chat),
    url(r'^add_post$', views.add_post),
]
