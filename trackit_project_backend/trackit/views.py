from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tracker
from .serializers import TrackerSerializer



class TrackerListAndCreateView(APIView): 
    # POST request -> Create new Tracker
    
    def post(self, request):
        serializer = TrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)#change the status if u want to what is more appropriate! 
