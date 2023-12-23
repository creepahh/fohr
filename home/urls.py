from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('complain/', ComplainView.as_view(), name='complain'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('signup/', signup, name='signup'),

]
