from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tracker
from .serializers import TrackerSerializer



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
