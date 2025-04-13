from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.paginator import Paginator

from job_nest_app.models import GeneralInfo, UserMadePost

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world!")
    context={}
    return render(request,"index.html",context)
    
    #return render(request,"index.html",context)
