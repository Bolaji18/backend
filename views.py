from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Infos
from .models import UploadImage
from .models import UploadImage
from .models import Users
from .models import Userinfos
from django.contrib.auth import authenticate
from .forms import NewUserForm
from .forms import ads
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def new(request):
   if request.method == "POST":
       form = NewUserForm(request.POST)
       if form.is_valid():
           user = form.save()
           messages.success(request, "Registration successful")
           return HttpResponseRedirect('#')


       messages.error(request, "Unsuccessful registration")
   form= NewUserForm()
   life= "create account"
   return render(request=request, template_name="#", context={"register_form":form, 'life':life})

def user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                welcome = f"you are now logged in as {username}."
                homeplace = "rent"
                ego = "Create an ad"
                ser = Users.objects.all().values()
                ser = Users.objects.all()
                context = {
                    'Users': ser,
                    'welcome': welcome,
                    'homeplace': homeplace,
                    'ego':ego,

                }
                if request.method == "POST":
                    form = ads(request.POST)
                    if form.is_valid():
                        user = form.save
                        return HttpResponse('saved')

                form = ads()
                return render(request=request, template_name="#", context={"form": form})

                return HttpResponse(template.render(context, request))
            else:
                 messages.error(request, "invalid username or password.")

        else:
            messages.error(request, "invalid username or password")
    form = AuthenticationForm()
    create = "newaccount/"
    used = "create new user"
    life = "login"
    return render(request, "#", {"register_form":form,  'create':create, 'used':used, 'life':life})
