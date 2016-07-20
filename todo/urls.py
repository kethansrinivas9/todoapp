from django.conf.urls import url

from . import views
app_name = 'todo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^completed/$', views.completed, name='completed'),
]