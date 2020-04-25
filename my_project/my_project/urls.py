
from django.contrib import admin
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
                url(r'^admin/', admin.site.urls),
                url(r'^$', views.index, name='index'),
                url(r'^queries/',include("articles.urls")),
                url(r'^login/', views.login, name='login'),
                # url(r'^queries/', views.queries, name='queries')


              ]
urlpatterns+=staticfiles_urlpatterns()