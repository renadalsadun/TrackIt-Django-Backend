from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tracker, Application
from .serializers import TrackerSerializer, ApplicationSerializer



# Helper Method : saves it from calling get_object_or_404 in every method
def get_object( model , pk ):
    return get_object_or_404( model, pk = pk )



# Tracker Model
class TrackerCreateView(APIView): 
    # POST request -> Create new Tracker

    def post(self, request):
        serializer = TrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class TrackerListView(APIView):
    # GET request -> View all Trackers

    def get(self, request):
        trackers = Tracker.objects.all() 
        serializer = TrackerSerializer(trackers, many=True)
        return Response(serializer.data, status=200)



class TrackerDetailView(APIView):

    def get(self, request, pk):
        # GET the Tracker object 
        # Serialize it with the Tracker serializer
        # Return it

        tracker = get_object(Tracker , pk)
        serializer = TrackerSerializer(tracker)
        return Response(serializer.data, status=200)



class TrackerDeleteView(APIView):

    def delete(self, request, pk):
        # Get the Tracker
        # Delete the Tracker
        # Return the appropriate Responce
        tracker = get_object( Tracker, pk )
        tracker.delete()
        return Response(status=204)



class TrackerUpdateView(APIView):
    def patch(self, request, pk):
        # Get the Tracker 
        # if the update is valid 
            # Save it 
            # Return approprate Responce 
        tracker = get_object( Tracker , pk )
        serializer = TrackerSerializer(tracker, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors, status = 400)



# Application Model
class ApplicationCreateView(APIView):
    # POST request -> Create new Application

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class ApplicationListView(APIView):
    # GET request -> View all Applications

    def get(self, request):
        applications = Application.objects.all() 
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=200)

