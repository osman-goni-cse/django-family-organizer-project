from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # member er jonno


# Create your models here.

class Post(models.Model):
  text = models.TextField(max_length=5000, blank=True)
  photo = models.ImageField(upload_to="myimage", blank=True)

  event_title = models.TextField(max_length=5000, blank=True)
  event_start_date = models.DateTimeField(blank=True, default=timezone.now())
  event_end_date = models.DateTimeField(blank=True, default=timezone.now())

  todo_title = models.TextField(max_length=5000, blank=True)
  todo_description = models.TextField(max_length=5000, blank=True)
  todo_date = models.DateTimeField(blank=True, default=timezone.now())

  created = models.DateTimeField(auto_now_add=True)


  class Meta:
    ordering = ('-created',)


# member add er jonno

class AddMember(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  auth_token = models.CharField(max_length=100)
  is_verified = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.username

  