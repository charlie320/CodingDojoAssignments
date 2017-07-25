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
    if 'user_id' in request.session:
        current_user = User.objects.currentUser(request)
        friends = current_user.friends.all()
        users = User.objects.exclude(id__in=friends).exclude(id=current_user.id)

        context = {
            'users' : users,
            'friends' : friends,
        }
        return render(request, 'login_app/success.html', context)
    return redirect(reverse('landing'))

def register(request):
    print "Inside the register function"
    if request.method == "POST":
        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)
            request.session['user_id'] = user.id
            return redirect(reverse('success'))

        flashErrors(request, errors)

    return redirect(reverse('landing'))

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
