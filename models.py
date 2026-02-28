from django.db import models
class contact(models.Model):
  name = models.CharField(max_length=100)
  phone = models.CharField()
  email = models.EmailField()
  message = models.CharField(max_length=100)

  def __str__(self):
    return self.name

# Create your models here.
