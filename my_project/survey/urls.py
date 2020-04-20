from django.conf.urls import include, url
from django.contrib import admin
from . import views

admin.autodiscover()
app_name='dbms'
urlpatterns = [
                url(r'^login/$', views.login, name='login')
              ]