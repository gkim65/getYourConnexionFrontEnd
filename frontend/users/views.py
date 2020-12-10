from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError

from application.models import IncomeModel



def index(request):
    return render(request, 'users/index.html',)

def login_view(request):
    if request.method == "POST":
        # Try to log in user
        username = request.POST["username"]
        password = request.POST["password"]
        if password == "" or username == "":
            return render(request, "users/login.html", {
                "message" : "No empty fields"
            })
        user = authenticate(request, username=username, password=password)

        # Check if the authentication was successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:homepage"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password"
            })
    
    # If it turns out user is already logged in but is trying to log in again redirect to user's homepage
    if request.method == "GET" and request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:homepage"))

    # Just give back log in page if none of the above is true
    else:
        return render(request, "users/login.html",{})

def logout_view(request):
    # Easy Django library to help out with logging out
    logout(request)
    return HttpResponseRedirect(reverse("users:index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Check that password matches the confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password == "" or username == "" or confirmation =="" or email == "":
            return render(request, "users/register.html", {
                "message" : "No empty fields"
            })
        if password != confirmation:
            return render(request, "users/register.html", {
                "message" : "Passwords must match"
            })

        # Try to create new user
        try:
            user = User.objects.create_user(username,email,password)
            user.save()
        except IntegrityError:
            return render(request, "users/register.html", {
                "message": "Username already taken."
            })
        # If user was successfully created, log them in and then go to application:index for income qualifying questions
        login(request,user)
        i = IncomeModel(
        username = request.user,
        Have_a_W2 = False,
        annual_Income = '[0]',
        family =  1)
        i.save()
        return HttpResponseRedirect(reverse("application:index"))
    
    # If a user is already logged in and they are trying to make a new account, just return them to homepage
    if request.method == "GET" and request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:homepage"))
    else:
        return render(request, "users/register.html",{})

def homepage(request):
    if request.user.is_authenticated:
        user = request.user
        income = IncomeModel.objects.filter(username=user).last()
        return render(request, "users/homepage.html", {"income" : income.annual_Income})
    else:
        return HttpResponseRedirect(reverse("users:login"))

def contact(request):
    return render(request, "users/contact.html")

def about(request):
    return render(request, "users/about.html")