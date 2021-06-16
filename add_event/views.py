from django.shortcuts import render

# Create your views here.

def pop_up_event(request):
  return render(request, 'add_event/event.html')
