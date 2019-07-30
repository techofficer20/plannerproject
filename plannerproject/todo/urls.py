from django.conf.urls import url
from . import views
app_name = 'todo'
urlpatterns = [
    url('todo/', views.todo, name = 'todo'),
]