from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    message = models.TextField(max_length=100)
    
    def __str__(self) -> str:
        return self.email