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
