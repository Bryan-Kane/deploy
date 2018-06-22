from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),
    url(r'jsn/', views.jsn),
    url(r'htl/', views.htl)
]