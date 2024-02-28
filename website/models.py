from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='yyy')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=50, blank=True)
    phone_num = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

    class Meta:
        ordering: ['first_name', 'lasr_name']



