form django import forms
from .models import TodoList

class TodoForm(forms.ModelsForm):
    class Meta:
        model=TodoList
        fields=('title','content','end_date')