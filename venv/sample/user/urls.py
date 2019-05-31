from django.urls import path
from django.conf.urls import url
from .views import user_form, submit_user, all_users, home

app_name = 'user'

urlpatterns = [
    path('home', home, name="home"),
    path('new/', user_form, name="new"),
    path('submit', submit_user, name="submit"),
    path('all-users', all_users, name="all_users")
    
]