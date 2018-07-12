from django.conf.urls import url
from ranking import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]