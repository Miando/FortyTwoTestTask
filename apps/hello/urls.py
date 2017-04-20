from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^request/$', views.last_requests, name='last_requests'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^login/$', views.login, name='login'),
)
