from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^films/$', views.films, name='films'),
    url(r'^films/(?P<film_id>\d+)/$', views.film, name='film'),
    url(r'^new_film/$', views.new_film, name='new_film'),
]