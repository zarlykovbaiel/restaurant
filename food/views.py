from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import response


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def blood(request):
    return render(request, "blood.html")


def menu(request):
    starters = Starter.objects.all()
    salads = Salad.objects.all()
    specialtys = Specialty.objects.all()
    return render(request, "menu.html", {'starters': starters, 'salads': salads, 'specialtys': specialtys})


def booktable(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        date = request.POST["date"]
        persons = request.POST["persons"]
        message = request.POST["message"]
        print(name, email, phone, date, persons, message)
        ins = Table(name=name, email=email, phone=phone, date=date, persons=persons, message=message)
        ins.save()
        print('data save in db')
        return render(request, 'booktable.html')
    else:
        return render(request, 'booktable.html')


def Event(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        date = request.POST["date"]
        event = request.POST["event"]
        persons = request.POST["persons"]

        print(name, phone, date, event, persons)
        var = Program(name=name, phone=phone, date=date, event=event, persons=persons)
        var.save()
        print("data save in db")
        return render(request, 'home.html')
    else:
        return render(request, 'Event.html')


def Contact1(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        var = response(name=name, phone=phone, email=email, subject=subject, message=message)
        var.save()
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


def form(request):
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
        form = contactform()
        return render(request, 'form.html', {'form': form})