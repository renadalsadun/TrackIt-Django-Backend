
from django.urls import path

from .views import TrackerCreateView, TrackerListView



urlpatterns = [
    path('tracker/new', TrackerCreateView.as_view(), name='tracker-create'),
    path('trackers/', TrackerListView.as_view(), name='tracker-list'),
]