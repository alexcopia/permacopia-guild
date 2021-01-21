from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<int:guild_id>/', views.guildDetails, name='detail'),
]
