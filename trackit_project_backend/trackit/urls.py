
from django.urls import path

from .views import (TrackerCreateView, TrackerListView, TrackerDetailView, TrackerDeleteView, TrackerUpdateView,
                    ApplicationCreateView, ApplicationListView)



urlpatterns = [
    path('trackers/new', TrackerCreateView.as_view(), name='tracker-create'),
    path('trackers/', TrackerListView.as_view(), name='tracker-list'),
    path('trackers/<int:pk>/', TrackerDetailView.as_view(), name='tracker-detail'),
    path('trackers/<int:pk>/delete/', TrackerDeleteView.as_view(), name='tracker-delete' ),
    path('trackers/<int:pk>/update/', TrackerUpdateView.as_view(), name='tracker-update' ),
    path('applications/new', ApplicationCreateView.as_view(), name='application-create'),
    path('applications/', ApplicationListView.as_view(), name='application-list'),

]