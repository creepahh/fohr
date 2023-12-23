from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('complain/', Complain.as_view(), name='complain'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),

]
