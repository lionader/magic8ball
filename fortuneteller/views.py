from django.shortcuts import render
from .fortuneteller import magic8ball



def show_fortune(request):
    results = magic8ball()
    return render(request, 'showfortune.html', {'result': results})

def request_fortune(request):
    return render(request, 'request.html')