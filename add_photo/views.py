from django.shortcuts import render

# Create your views here.

def add_photo(request):
  return render(request, 'add_photo/photo.html')
