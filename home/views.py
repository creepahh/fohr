from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import User


class Base(View):
    views = {}


class HomePageView(Base):
    def get(self, request):
        return render(request, "home.html", self.views)


class ComplainView(Base):

    def get(self, request):
        return render(request, "complaint.html", self.views)

    def post(self, request):
        if request.method == 'POST':
            fullname = request.POST['fullname']
            address = request.POST['address']
            email = request.POST['email']
            message = request.POST['message']
            location = request.POST['location']
            phone_number = request.POST['phone_number']

            data = Feedback.objects.create(

                fullname=fullname,
                address=address,
                email=email,
                phone_number=phone_number,
                message=message,
                location=location,

            )
            data.save()

        return render(request, "complaint.html", self.views)


class ScheduleView(Base):

    def get(self, request):
        self.views['schedules'] = Schedule.objects.all

        return render(request, "schedule.html", self.views)


class AboutView(Base):

    def get(self, request):
        return render(request, "about.html", self.views)


def signup(request):
    if request.method == "POST":
        username = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "The username is already taken")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "The email is already used")
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,

                )
                data.save()

        else:
            messages.error(request, "The passwords do not match")
            return redirect('/signup')
    return render(request, 'signup.html')
