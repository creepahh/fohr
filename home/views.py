from django.shortcuts import render
from django.views.generic import View
from .models import *


class Base(View):
    views = {}


class HomePage(Base):
    def get(self, request):
        return render(request, "home.html", self.views)


class Complain(Base):

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
