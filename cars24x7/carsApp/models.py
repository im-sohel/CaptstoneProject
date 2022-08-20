from django.db import models

class AppoinMentData(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, primary_key=True, unique=True)
    mobile = models.IntegerField()
    date = models.CharField(max_length=100)
    
    def __str__(self):
     return f"{self.name}, {self.email}, {self.mobile}, {self.date}"