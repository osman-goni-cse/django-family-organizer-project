from django import forms
from .models import Post
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.forms import ModelForm, Textarea
from datetime import datetime

class PostForm(forms.ModelForm):

  event_start_date = forms.DateTimeField(
    widget=DateTimePicker(
      options={
          'useCurrent': True,
          'collapse': False,
          
          'defaultDate':'2021-06-20 23:59:59', 
      },
      attrs={
          # <i class="fas fa-calendar-day"></i>
          'append': 'fas fa-calendar-day',
          'icon_toggle': True,

      }
    ),
  )

  event_end_date = forms.DateTimeField(
    widget=DateTimePicker(
      options={
          'useCurrent': True,
          'collapse': False,

          'defaultDate':'2021-06-20 23:59:59',
      },
      attrs={
          'append': 'fas fa-calendar-day',
          'icon_toggle': True,
      }
    ),
  )

  todo_date = forms.DateTimeField(
    widget=DateTimePicker(
      options={
          'useCurrent': True,
          'collapse': False,

          'defaultDate':'2021-06-20 23:59:59',
      },
      attrs={
          'append': 'fas fa-calendar-day',
          'icon_toggle': True,
      }
    ),
  )
  
  class Meta:
    model = Post
    fields = '__all__'
    labels = {'photo':'Image'}
    widgets = {
      'text': Textarea(attrs={'placeholder':"What's on your mind?",'cols':40,'rows': 4,}),
      'event_title': Textarea(attrs={'placeholder':"Event Title",'cols':63,'rows': 2,'class':'form-control'}),
      'todo_title': Textarea(attrs={'placeholder':"I want to do...",'cols':63,'rows': 2,'class':'form-control'}),
      'todo_description': Textarea(attrs={'placeholder':"Description of your task",'cols':63,'rows': 2,'class':'form-control'}),
    }
