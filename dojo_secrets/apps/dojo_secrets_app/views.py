from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):

    return render(request, 'dojo_secrets_app/index.html')

def register(request):
    print "Inside the views register function"

    if request.method == "POST":
        form_data = request.POST

        check = User.objects.validate(form_data)
        if check:
            print check
            return redirect('/')

        user = User.objects.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = form_data['password']
        )
        request.session['user_id'] = user.id
        print user
        return redirect('/success')

    return redirect('/')

def login(request):
    print "Inside the login function."

    if request.method == "POST":
        form_data = request.POST

        check = User.objects.login(form_data)

        if type(check) == type(User()):
            request.session['user_id'] = check.id
            return redirect('/success')

    return redirect('/')

def success(request):
    print "Inside the success route."

    if 'user_id' in request.session:
        user_id = request.session['user_id']

        context = {
            'current_user': User.objects.get(id=user_id)
        }
        return render(request, 'dojo_secrets_app/success.html', context)
    return redirect('/')

def logout(request):
    print "Inside the logout function."
    request.session.pop('user_id')
    return redirect('/')
