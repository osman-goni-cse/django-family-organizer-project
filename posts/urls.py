from django.urls import path
from .views import post, member_invite, token_send, listing_todo, updateTask, deleteTask

urlpatterns = [
    # path('', post_comment_create_and_list_view, name='main-post-view'),
    path('', post, name='post'),
    path('member_invite/', member_invite, name='member_invite'),
    path('token/', token_send, name='token_send'),
    path('todo_list/', listing_todo, name='todo_list'),
    path('<auth_token>/', post, name='confirm'),

    #new url
    path('update_task/<str:pk>/', updateTask, name="update_task"),
    path('delete_task/<str:pk>/', deleteTask, name="delete_task"),

]
