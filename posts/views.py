from posts.forms import PostForm
from .models import Post, AddMember
from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
# add member
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from django.conf import settings
from django.core.mail import message, send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string


# Create your views here.

def post(request):
  print(request.method)

  evnt_st_dt = datetime.datetime.now()
  evnt_st_month = "Jand"
  evnt_ed_dt = datetime.datetime.now()
  todo_dt = datetime.datetime.now()

  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)

    print("POST request asce")
    if form.is_valid():
      form.save()
      evnt_st_dt = form.cleaned_data['event_start_date']
      evnt_st_month = evnt_st_dt.strftime("%B")
      evnt_st_dt = evnt_st_dt.strftime('%Y-%B-%d %H:%M:%S')
      print("strftime ", evnt_st_dt)
      
      evnt_st_dt = datetime.datetime.strptime(str(evnt_st_dt), '%Y-%B-%d %H:%M:%S')

      print("strptime ", evnt_st_dt)
      # print(evnt_st_dt.day)
      # print(evnt_st_dt.month)
      # print(evnt_st_dt.year)
      
      evnt_ed_dt = form.cleaned_data['event_end_date']
      # evnt_ed_dt = datetime.datetime.strptime(str(evnt_ed_dt), '%Y-%m-%d %H:%M:%S.s')
      todo_dt = form.cleaned_data['todo_date']
      # todo_dt = datetime.datetime.strptime(str(todo_dt), '%Y-%m-%d %H:%M:%S.s')
      
    else:
      print("form is invalid ", form.errors)
  
  form = PostForm()
  post_details = Post.objects.all()

  # myForm.fields['description']
  
  print(evnt_st_dt)

  print("view function ee asce")
  
  num_of_task = 0

  for task in post_details:
    if task.todo_title:
      num_of_task += 1


  context = {
    'form':form,
    'post_details':post_details,
    'evnt_st_dt':evnt_st_dt,
    'evnt_ed_dt':evnt_ed_dt,
    'todo_dt':todo_dt,
    'evnt_st_month':evnt_st_month,
    'num_of_task':num_of_task,
  }

  return render(request, 'posts/index.html', context)



# member add

def member_invite(request):
  print("member invite ee asce")
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')

    print("email: ",email)
    try:
      if User.objects.filter(username = username).first():
        messages.error(request, 'Username is taken')
        return redirect('/posts')

      if User.objects.filter(email = email).first():
        messages.error(request, 'Email is taken')
        print("Email is taken")
        return redirect('/posts')
      
      user_obj = User(username=username, email=email)
      user_obj.save()

      auth_token = str(uuid.uuid4)
      profile_obj = AddMember.objects.create(user=user_obj, auth_token=auth_token)

      profile_obj.save()

      print("Email send er ager line")
      send_mail_after_registration(email, auth_token)
      print("Email send howar kota")
      messages.success(request, 'Congratulations, your invitation was successfully sent!')
      return redirect('/posts')
    except Exception as e:
      print(e)


  return render(request, 'posts/index.html')

def send_mail_after_registration(email, token):
  subject = 'Please Join me on family organizer Website'
  message = F"Hi,It's a private and safe place where we can share pictures and videos and organize everyday life. http://127.0.0.1:8000"
  # message = render_to_string('accounts/email.html', {'token': token})
  email_from = settings.EMAIL_HOST_USER
  recipient_list = [email]
  send_mail(subject, message, email_from, recipient_list)

def token_send(request):
  return render(request, 'posts/token_send.html') 


def listing_todo(request):
  post_details = Post.objects.all()
  form = PostForm()


  context = {
    'post_details':post_details,
    'form':form,
  }

  return render(request, 'posts/todo_list.html', context)


# new update
def updateTask(request, pk):
  task = Post.objects.get(id=pk)
  post_details = Post.objects.all()

  print('update er pk ', pk)
  form = PostForm(instance=task)

  context = {
    'form':form,
    'post_details':post_details,
  }

  print("UpdateTask view function call hoice + ", request.method)

  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES,instance=task)
    print("updated data niye asci")
    print(request.POST) 
    try:
      # request.POST.event_start_date = timezone.now()
      
      if form.is_valid():
        form.save()
        # print(form.cleaned_data['todo_title'])
        # print(form.cleaned_data['todo_description'])
        return redirect('/posts/todo_list')
      else:
        print('data invalid')
        print(form.errors)
    except Exception as e:
      print(e)

  return render(request, 'posts/update_task.html', context)

def deleteTask(request, pk):
  item = Post.objects.get(id=pk)

  if request.method == 'POST':
    item.delete()
    return redirect('/posts/todo_list')
  
  context = {
    'item':item,
  }

  return render(request, 'posts/delete_task.html', context)