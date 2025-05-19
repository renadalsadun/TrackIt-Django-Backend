
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (TrackerCreateView, TrackerListView, TrackerDetailView, TrackerDeleteView, TrackerUpdateView,
                    ApplicationCreateView, ApplicationListView, ApplicationDetailView, ApplicationDeleteView, ApplicationUpdateView,
                    DocumentCreateView, DocumentListView, DocumentDetailView, DocumentDeleteView, DocumentUpdateView,
                    SignUpView)



urlpatterns = [
    path('trackers/new/', TrackerCreateView.as_view(), name='tracker-create'),
    path('trackers/', TrackerListView.as_view(), name='tracker-list'),
    path('trackers/<int:pk>/', TrackerDetailView.as_view(), name='tracker-detail'),
    path('trackers/<int:pk>/delete/', TrackerDeleteView.as_view(), name='tracker-delete' ),
    path('trackers/<int:pk>/update/', TrackerUpdateView.as_view(), name='tracker-update' ),
    path('applications/new/', ApplicationCreateView.as_view(), name='application-create'),
    path('applications/', ApplicationListView.as_view(), name='application-list'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('applications/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='application-delete' ),
    path('applications/<int:pk>/update/', ApplicationUpdateView.as_view(), name='application-update' ),
    path('documents/new/', DocumentCreateView.as_view(), name='document-create'),
    path('documents/', DocumentListView.as_view(), name='document-list'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('documents/<int:pk>/delete/', DocumentDeleteView.as_view(), name='document-delete' ),
    path('documents/<int:pk>/update/', DocumentUpdateView.as_view(), name='document-update' ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup')


]