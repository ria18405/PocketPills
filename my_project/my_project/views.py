
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.urls import reverse

from my_project import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, "login.html")

def index(request):
    return render(request, "index.html")

