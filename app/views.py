from django.shortcuts import render
from app.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def registration(request):


    if request.user.is_authenticated:
        return render(request, 'app/registration.html')

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = ProfileUserInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']

            profile.save()
        else:
                        # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = ProfileUserInfoForm()

    return render(request, 'app/registration.html', {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("You are not logged in!")

        else:
            print("login failed!")
            return render(request, 'app/login.html')

    else:
        return render(request, 'app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in!")
