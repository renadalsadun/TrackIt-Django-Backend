
from django.urls import path

from .views import TrackerListAndCreateView



urlpatterns = [
    path('tracker/new', TrackerListAndCreateView.as_view(), name='tracker-create')
]