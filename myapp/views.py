from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

from myapp.forms import ContactForm
# from django.template.context_processors import csrf


def index(request):
    f = ContactForm()
    return render(request, 'index.html', {'form1': f.as_table()})

def complete(request):
    return render(request, 'complete.html')