from django.urls import path
from . import views


app_name = 'button'
urlpatterns = [
    path('', views.index, name='startpage'),
    path('l_on_of', views.l_on_of, name='l_on_of'),
    path('api', views.api, name='api'),
]