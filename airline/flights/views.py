from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Flights,Passenger,Airport

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,"flights/home.html")

def index(request):
    return render(request, "flights/index.html",{
        "flights": Flights.objects.all()
    })

def flight(request, flight_id):
    flight=Flights.objects.get(pk=flight_id) #pk=primary key
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

from django.contrib.auth.decorators import login_required

@login_required
def book(request, flight_id):

    flight = Flights.objects.get(pk=flight_id)
    passenger = Passenger.objects.get(user=request.user)
    passenger.flights.add(flight)
    return redirect("flight", flight_id=flight.id)

def logout_view(request):

    logout(request)
    return redirect("index")
    

def search_flights(request):

    if request.method == "POST":

        origin_id = request.POST["origin"]
        destination_id = request.POST["destination"]

        # Prevent same airport
        if origin_id == destination_id:
            return HttpResponse("Origin and destination cannot be same")

        # Get airport objects
        origin = Airport.objects.get(pk=origin_id)
        destination = Airport.objects.get(pk=destination_id)

        # Find flights
        flights = Flights.objects.filter(origin=origin, destination=destination)

        return render(request, "flights/search_results.html", {
            "flights": flights,
            "origin": origin,
            "destination": destination
        })

def flight_detail(request, flight_id):

    flight = Flights.objects.get(pk=flight_id)
    passengers = flight.passengers.all()

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers
    })


def register(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        first = request.POST["first"]
        last = request.POST["last"]

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first,
            last_name=last
        )

        Passenger.objects.create(user=user)

        login(request, user)

        return redirect("index")

    return render(request, "flights/register.html")


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")

    return render(request, "flights/login.html")
