from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'courses_app/index.html')

def add(request):
    print("you made it to the add page")
    return render(request, 'courses_app/confirm_remove.html')

def remove(request):
    print("you made it to the remove app")
    return render(request, 'courses_app/confirm_remove.html')


def confirm_remove(request):
    print ("you made it to the confirm_remove app")
    return redirect('/')
