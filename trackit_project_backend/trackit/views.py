from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Tracker, Application, Document
from .serializers import TrackerSerializer, ApplicationSerializer, DocumentSerializer



# Helper Method : saves it from calling get_object_or_404 in every method
def get_object( model , pk ):
    return get_object_or_404( model, pk = pk )



# Tracker Model
class TrackerCreateView(APIView): 
    # POST request -> Create new Tracker
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class TrackerListView(APIView):
    # GET request -> View all Trackers
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trackers = Tracker.objects.filter(user = request.user) 
        serializer = TrackerSerializer(trackers, many=True)
        return Response(serializer.data, status=200)



class TrackerDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # GET the Tracker object 
        # Serialize it with the Tracker serializer
        # Return it

        tracker = get_object(Tracker , pk)
        serializer = TrackerSerializer(tracker)
        return Response(serializer.data, status=200)



class TrackerDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        # Get the Tracker
        # Delete the Tracker
        # Return the appropriate Responce
        tracker = get_object( Tracker, pk )
        tracker.delete()
        return Response(status=204)



class TrackerUpdateView(APIView):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class ApplicationListView(APIView):
    # GET request -> View all Applications
    permission_classes = [IsAuthenticated]

    def get(self, request):
        applications = Application.objects.all() 
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=200)



class ApplicationDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # GET the Application object 
        # Serialize it with the Application serializer
        # Return it

        application = get_object(Application , pk)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data, status=200)



class ApplicationDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        # Get the Application
        # Delete the Application
        # Return the appropriate Responce
        application = get_object( Application, pk )
        application.delete()
        return Response(status=204)



class ApplicationUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        # Get the Application 
        # if the update is valid 
            # Save it 
            # Return approprate Responce 
        application = get_object( Application , pk )
        serializer = ApplicationSerializer(application, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors, status = 400)



#Document model
class DocumentCreateView(APIView):
    # POST request -> Create new Document
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class DocumentListView(APIView):
    # GET request -> View all Documents
    permission_classes = [IsAuthenticated]

    def get(self, request):
        documents = Document.objects.filter(user = request.user) 
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data, status=200)



class DocumentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # GET the Document object 
        # Serialize it with the Document serializer
        # Return it

        document = get_object(Document , pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data, status=200)



class DocumentDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        # Get the Document
        # Delete the Document
        # Return the appropriate Responce
        document = get_object( Document, pk )
        document.delete()
        return Response(status=204)



class DocumentUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        # Get the Document 
        # if the update is valid 
            # Save it 
            # Return approprate Responce 
        document = get_object( Document , pk )
        serializer = DocumentSerializer(document, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors, status = 400)



#Authentication
class SignUpView(APIView): 
    permission_classes = [AllowAny] 
    def post(self, request):
        # Using .get will not error if there's no username
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            validate_password(password)
        except ValidationError as err:
            return Response({'error': err.messages}, status=400)

        # Actually create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # create an access and refresh token for the user and send this in a response
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token)
            },
            status=201
        )