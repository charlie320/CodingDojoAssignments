from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'username_validation_app/index.html')

def validate(request):
    print "You made it to the validate function"
    return render(request, 'username_validation_app/success.html')

def return_home(request):
    print "You made it to return home"
    return redirect('/')
