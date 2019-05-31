from django.shortcuts import render
from .models import User

def user_form(request):
    return render(request, 'user/index.html', {})



def submit_user(request):
    name = request.POST['name']
    password = request.POST['password']

    user = User(name=name, password=password)
    user.save()
    users = User.objects.all()
    return render(request, 'allusers/index.html', {'users': users})



def all_users(request):
    users = User.objects.all()
    if not users:
        users = {}
    return render(request, 'allusers/index.html', {'users': users})



def home(request):
    return render(request, 'home/index.html', {})
