from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from flights.models import Airport
# Create your views here.

from flights.models import Airport

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    airports = Airport.objects.all()

    return render(request, "users/user.html", {
        "airports": airports
    })
    
def login_view(request):
    if request.method=="POST":
        username= request.POST["username"]
        password= request.POST["password"]
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username or password"
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
        "message": "Logged out successfully"
    })


