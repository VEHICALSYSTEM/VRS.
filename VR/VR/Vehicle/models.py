from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=20, null=True)
    msg = models.TextField(max_length=40, null=True)

    def _str_(self):
        return self.email

# Create your models here.
