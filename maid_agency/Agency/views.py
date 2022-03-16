from email import message
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from maid_agency.decorators import *

# Create your views here.
@login_required(login_url="login")
@admin_only
def index(request):
    return render(request,'Dashboard.html')


@login_required(login_url="login")
def logoutuser(request):
    logout(request)
    messages.info(request,"Successfully Logout.")
    return redirect('login')


# views from frontend project 

def FDWs(request):
    return render(request,'FDWs.html')

def myagency(request):
    return render(request,'My_agency.html')

def myagencyedit(request):
    return render(request,'Edit_My_agency.html')


def add_FDWs(request):
    return render(request,'add_FDWs.html')

def contract(request):
    return render(request,'contracts.html')

def FDWs_profile(request):
    return render(request,'FDWs_profile.html')


def user_role(request):
    return render(request,'User_role.html')


# def users(request):
#     return render(request,'Users.html')

def Add_contract(request):
    return render(request,'Add_contract.html')