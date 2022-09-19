from dataclasses import fields
from.models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea

class TaskForm (ModelForm):
    model = Task
    fields = ["title", "task"]
    widgets = {"title": TextInput (attrs = {'class':'form - control', 'placeholder': 'Введите название'}),
                   "task": Textarea(attrs = {'class':'form - control', 'placeholder': 'Введите описание'}),
                   }