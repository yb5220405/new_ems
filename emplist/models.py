from django.db import models
class Emp(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    salary=models.DecimalField(max_digits=7,decimal_places=2)
    headpci=models.ImageField(upload_to="ps")
# Create your models here.
