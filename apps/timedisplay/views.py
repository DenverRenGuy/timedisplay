from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    context = {
        "date": datetime.datetime.now(),
        "time": datetime.datetime.now().time()
    }
    return render(request, 'timedisplay/index.html', context)
