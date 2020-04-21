from django.db import models

# Create your models here.


class MyUsers(models.Model):


    u_name = models.TextField(max_length=50, unique=False)
    u_surname = models.TextField(max_length=50, unique=False)
    u_email = models.EmailField(unique=True)


    def __str__(self):

        return self.u_email

