from django.shortcuts import render
from .models import Header

# Create your views here.
def header(request):
    header  = Header.objects.all()

    data = {
        'header' : header,
    }
    return render(request, 'includes/header.html', data)
