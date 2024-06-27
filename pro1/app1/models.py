from django.db import models

# Create your models here.
class Laptop(models.Model):
    lid = models.IntegerField(primary_key=True)
    laptop_name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.lid}----{self.laptop_name}-----{self.price}"