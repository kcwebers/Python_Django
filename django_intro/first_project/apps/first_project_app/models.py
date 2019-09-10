from django.db import models
    
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    rating = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

