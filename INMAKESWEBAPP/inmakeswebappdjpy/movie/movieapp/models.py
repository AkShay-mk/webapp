from django.db import models

class movie(models.Model):
    name=models.CharField(max_length=120)
    desc=models.TextField()
    year=models.IntegerField()
    imag=models.ImageField(upload_to='gal')
    def __str__(self):
        return self.name
    
    