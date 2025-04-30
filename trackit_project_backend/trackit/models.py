from django.db import models
from django.contrib.auth.models import User



class Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)    
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name