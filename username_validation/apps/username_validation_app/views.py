from django.shortcuts import render, redirect, HttpResponse
from .models import User
# Create your views here.

def index(request):

    return render(request, 'username_validation_app/index.html')

def validate(request):
    request.session['name'] = request.POST['username']
    myResponse = User.userManager.login(request.POST['username'])
    print myResponse

    return render(request, 'username_validation_app/success.html')

def return_home(request):
    # print "You made it to return home"
    return redirect('/')
