"""FamilyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# notun add socila project teke
from django.conf import settings
from django.conf.urls.static import static

# from registration import views
from registration.views import user_signup, user_login, user_logout
from core_project.views import home
from add_event.views import pop_up_event
from add_todo.views import add_todo
from add_photo.views import add_photo
from add_location.views import add_location
from event_calendar import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_signup, name="register"),
    path('login/', user_login, name="login"),
    path('home/', home, name="home"),
    path('logout/', user_logout, name="logout"),

    path('pop_up_event/', pop_up_event, name="pop_up_event"),

    path('add_todo/', add_todo, name="add_todo"),
    path('add_photo/', add_photo, name="add_photo"),
    path('add_location/', add_location, name="add_location"),

    path('calendar/', views.calendar, name='calendar'),
    path('add_event/', views.add_event, name='add_event'),
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    
    path('posts/', include('posts.urls')),
    
]

# social project teke
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
