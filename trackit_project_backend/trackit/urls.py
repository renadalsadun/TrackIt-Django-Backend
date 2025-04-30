
from django.urls import path

from .views import TrackerCreateView, TrackerListView, TrackerDetailView, TrackerDeleteView



urlpatterns = [
    path('trackers/new', TrackerCreateView.as_view(), name='tracker-create'),
    path('trackers/', TrackerListView.as_view(), name='tracker-list'),
    path('trackers/<int:pk>/', TrackerDetailView.as_view(), name='tracker-detail'),
    path('trackers/<int:pk>/delete/', TrackerDeleteView.as_view(), name='tracker-delete' )
]