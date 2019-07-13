from django.shortcuts import render
from .models import TodoList
from .forms import TodoForm

from django.views import generic

class Todo_board(generic.TemplateView):
    def get(self,request,*args,**kwargs): 
        template_name='todo_board/todo_list.html'
        todo_list=TodoList.objects.all()
        form=TodoForm
        return render(request, template_name,{"todo_list":todo_list, "form" : form})
# Create your views here.
