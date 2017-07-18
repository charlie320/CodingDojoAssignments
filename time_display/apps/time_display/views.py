from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):

    context = {
    "current_time" : str(datetime.now())
    #"current_time" : "This is the time"
    }
    return render(request, 'index.html', context)
