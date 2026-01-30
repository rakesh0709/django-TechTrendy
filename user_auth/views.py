from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
import re


def login_(request):
    if request.method=='POST':
        username=request.POST['user_name']
        password=request.POST['_password']
        u=authenticate(username=username,password=password)
        if u:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'login_.html',{'status':True})
    return render(request ,'login_.html',{'login_':True})

import re

def is_valid_password(password):
    if not password or len(password) < 6:
        return False, "Password should be at least 6 characters long."
    has_letter = re.search(r"[A-Za-z]", password)
    has_digit = re.search(r"\d", password)
    if not has_letter or not has_digit:
        return False, "Password must include at least one letter and one number."
    return True, ""


def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirmpassword']
        if password != confirm_password:
            return render(request, 'register.html', {'password_mismatch': True})
        valid, msg = is_valid_password(password)
        if not valid:
            return render(request, 'register.html', {'password_invalid': True, 'password_invalid_msg': msg})
        # Mix of characters in pass
        try:
            u=User.objects.get(username=username)
            return render(request,'register.html',{'status':True})
        except User.DoesNotExist:
            u=User.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            username=username
        )
        u.set_password(password)
        u.save()
        return redirect('login_')
    return render(request ,'register.html',{'login_':True})


def logout_(request):
    logout(request)
    return redirect('login_')


from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    updated = request.GET.get('updated')
    return render(request,'profile.html',{'profile':True,'updated':updated})

@login_required
def profile_update(request):
    u = request.user
    if request.method == 'POST':
        first_name = request.POST.get('first_name','').strip()
        last_name = request.POST.get('last_name','').strip()
        email = request.POST.get('email','').strip()
        u.first_name = first_name
        u.last_name = last_name
        u.email = email
        u.save()
        return redirect('profile')
    return render(request, 'profile_update.html', {'user': u})


def resetpass(request):
    u=User.objects.get(username=request.user)
    if request.method=='POST':
        if 'oldpass' in request.POST:
            old_pass = request.POST['oldpass']
            verified = authenticate(username=u.username,password=old_pass)
            if verified:
                return render(request,'resetpass.html',{'verified':True})
            else:
                return render(request,'resetpass.html',{'not_verified':True})
        if 'newpass' in request.POST:
            new_pass = request.POST['newpass']
            valid, msg = is_valid_password(new_pass)
            if not valid:
                return render(request,'resetpass.html',{'verified':True,'password_invalid':True,'password_invalid_msg':msg})
            u.set_password(new_pass)
            u.save()
            return redirect('login_')
    return render(request,'resetpass.html')