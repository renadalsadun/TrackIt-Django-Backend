from rest_framework import serializers
from .models import Tracker, Application, Document



class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = '__all__' 
        read_only_fields = ['user']




class ApplicationSerializer(serializers.ModelSerializer):
    documents = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Document.objects.all(),
        allow_empty = True,
        required=False
    )
    class Meta:
        model = Application
        fields = '__all__'



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
