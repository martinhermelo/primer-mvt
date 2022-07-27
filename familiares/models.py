from django.db import models

class Hermelo_family(models.Model):
    name= models.CharField(max_length=50)
    age= models.IntegerField()
    date_birth= models.DateField(auto_now_add=True, null=True, blank=True)
    email= models.EmailField()