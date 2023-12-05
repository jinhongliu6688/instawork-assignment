from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=250)
    
    def __str__(self):
        return self.email