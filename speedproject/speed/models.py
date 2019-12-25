from django.db import models

# Create your models here.


class Data(models.Model):
    date = models.DateField(max_length=100)
    IpAddress = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    post = models.CharField(max_length=5)
    location = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    upload = models.CharField(max_length=100)
    download = models.CharField(max_length=100)
    ping= models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date},{self.IpAddress},{self.city},{self.post},{self.location},{self.hostname},{self.upload},{self.download}, {self.organisation}"


