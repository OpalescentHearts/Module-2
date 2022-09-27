from dataclasses import dataclass
from django.shortcuts import render

# Create your views here.
def hello_view(request, name):
    return render(request, "hello.html")
