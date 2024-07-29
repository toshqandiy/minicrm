from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()

    def __str__(self):
        return self.full_name