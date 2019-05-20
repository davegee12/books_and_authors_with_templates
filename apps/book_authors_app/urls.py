from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.show),
    url(r'^add_book$', views.add_book),
    url(r'^add_author$', views.add_author),
    url(r'^book/(?P<id>\d+)$', views.view_book),
    url(r'^author/(?P<id>\d+)$', views.view_author),
    url(r'^new_book$', views.new_book),
    url(r'^new_author$', views.new_author),
]