
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.urls import reverse

from my_project import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def login(request):
    # if(request.method=="POST"):
    #     form=AuthenticationForm(data=request.POST)
    #     return redirect('articles:queries')
    # else:
    #     form=AuthenticationForm()
    return render(request, "login.html")

def index(request):
    return render(request, "index.html")


# def queries(request):
#     if request.method=='POST':
#
#         print("post request")
#     return render(request, "queries.html")