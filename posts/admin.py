from django.contrib import admin
from .models import Post, AddMember
# Register your models here.
admin.site.register(AddMember) # member er jonno

@admin.register(Post)
class ImageAdmin(admin.ModelAdmin):
  list_display = ['id', 'photo', 'text', 'event_title', 'todo_title', 'todo_description','event_start_date', 'event_end_date','todo_date']
