
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
                url(r'^admin/', admin.site.urls),
                url(r'^$', views.index, name='index'),
                url(r'^login/', views.login, name='login')
              ]
urlpatterns+=staticfiles_urlpatterns()