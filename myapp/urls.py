from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import include

app_name = 'myapp'
 
urlpatterns = [
    path('', views.index, name='index'),
    path('complete', views.complete, name='complete')
]