from django.conf.urls import url
from cal import views

app_name = 'cal'
urlpatterns = [
    #url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), # here
]