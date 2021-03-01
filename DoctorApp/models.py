from django.db import models

# Create your models here.
class Doctor(models.Model):

    gender=(
        ('Male','male'),
        ('Female','female'),
        ('Others','others')
    )


    Doctor_name = models.CharField( max_length=50)
    Doctor_age = models.IntegerField()
    Gender = models.CharField(max_length=10,choices = gender)
    Created_at = models.DateField( auto_now_add=True)
    Updated_at = models.DateField( auto_now=True)
   
    def __str__(self):
        return self.Doctor_name
    

    
