from django.db import models
from django.contrib.auth.models import User



class Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)    
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

PRIORITY = (
    ('C' , 'Critical'),
    ('H' ,'High'),
    ('M' ,'Medium'),
    ('L' ,'Low')
)

class Application(models.Model): 
    name = models.CharField(max_length=100)
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE)

    company = models.CharField(max_length=100, blank=True )
    organization = models.CharField(max_length=100, blank=True )
    university = models.CharField(max_length=100, blank=True )
    location = models.CharField(max_length=100, blank=True )
    website = models.CharField(max_length=100, blank=True )
    link = models.CharField(max_length=100, blank=True )
    description = models.CharField(max_length=100, blank=True )
    referral = models.CharField(max_length=100, blank=True )
    contact = models.CharField( max_length = 100 , blank = True )
    notes = models.TextField( blank=True )

    priority = models.CharField(
        max_length = 1,
        choices = PRIORITY,
        blank = True
    )
    
    date_applied = models.DateField(null=True, blank=True)
    deadline = models.DateField( null=True, blank=True)
    interview_date = models.DateField( null=True, blank=True)
    start_date = models.DateField( null = True , blank = True )
    end_date = models.DateField( null = True , blank = True )

    def __str__(self):
        return self.name



class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    document_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name
