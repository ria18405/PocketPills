

from django.conf.urls import url
from . import views



urlpatterns = [
                url(r'^$', views.queries, name='queries'),
                url(r'^1/', views.queries_1, name='queries_1'),
                url(r'^4/', views.queries_4, name='queries_4'),
                url(r'^5/', views.queries_5, name='queries_5'),
                url(r'^3/', views.queries_3, name='queries_3'),
                url(r'^7/', views.queries_7, name='queries_7')
              ]
