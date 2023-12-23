from django.shortcuts import render
from django.views.generic import View


class Base(View):
    views = {}


class HomePage(Base):
    def get(self, request):
        return render(request, "home.html", self.views)

