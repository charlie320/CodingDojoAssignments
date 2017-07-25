from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import bcrypt
#from .models import User

# Create your views here.
def flashErrors(request, errors):
    for error in errors:
        messages.error(request. error)

def index(request):
    return render(request, 'login_app/index.html')

def success(request):
    print "Inside the success function"
    pass

def register(request):
    print "Inside the register function"
    return redirect('/')

def login(request):
    print "Inside the login function"
    return redirect('/')

def logout(request):
    print "Inside the logout function"
    pass

def addFriend(request, id):
    print "Inside the addFriend function"
    pass

def removeFriend(request, id):
    print "Inside the removeFriend function"
    pass
