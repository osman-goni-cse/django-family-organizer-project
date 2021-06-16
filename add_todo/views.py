from django.shortcuts import render

# Create your views here.

def add_todo(request):
  return render(request, 'add_todo/todo.html')
